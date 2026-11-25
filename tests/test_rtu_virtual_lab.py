import os
import sqlite3
import tempfile
import unittest
import uuid

import models

_test_directory = tempfile.TemporaryDirectory()
models.DB_PATH = os.path.join(_test_directory.name, "initial.db")

import app as lab_app


class RtuVirtualLabTests(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(_test_directory.name, f"{uuid.uuid4().hex}.db")
        models.DB_PATH = self.db_path
        models.init_db()
        lab_app.app.config.update(TESTING=True)
        self.client = lab_app.app.test_client()

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def register(self, client, username):
        models.create_student(username, f"Student {username}", f"ROLL-{username}", "test-hash")
        with client.session_transaction() as browser_session:
            browser_session.clear()
            browser_session["username"] = username
            browser_session["authenticated"] = True
        return client.get("/rtu-lab")

    def test_lab_opens_without_sign_in_and_all_experiments_load(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/rtu-lab")
        self.assertEqual(self.client.get("/login").location, "/rtu-lab")
        lab_page = self.client.get("/rtu-lab")
        self.assertEqual(lab_page.status_code, 200)
        self.assertIn(b"Guest session", lab_page.data)
        self.assertNotIn(b"Sign in", lab_page.data)

        self.register(self.client, "student_a")

        root = self.client.get("/")
        self.assertEqual(root.status_code, 302)
        self.assertEqual(root.location, "/rtu-lab")
        for route in ("/srs", "/uml", "/workbench", "/traceability", "/teacher"):
            with self.subTest(route=route):
                self.assertEqual(self.client.get(route).status_code, 200)

        for experiment_id in range(1, 8):
            with self.subTest(experiment_id=experiment_id):
                result = self.client.get(f"/rtu-lab/experiment/{experiment_id}")
                self.assertEqual(result.status_code, 200)

        user = models.get_user_by_username("student_a")
        self.assertTrue(user["password_hash"])

        self.client.get("/logout")
        self.assertEqual(self.client.get("/rtu-lab").status_code, 200)
        self.assertIn(b"Guest session", self.client.get("/rtu-lab").data)

    def test_guest_work_isolated_and_code_runner_stays_private(self):
        first_guest = lab_app.app.test_client()
        second_guest = lab_app.app.test_client()
        self.assertEqual(first_guest.get("/rtu-lab").status_code, 200)
        self.assertEqual(second_guest.get("/rtu-lab").status_code, 200)

        with first_guest.session_transaction() as first_session:
            first_guest_id = first_session["guest_id"]
        with second_guest.session_transaction() as second_session:
            second_guest_id = second_session["guest_id"]
        self.assertNotEqual(first_guest_id, second_guest_id)

        saved = first_guest.post("/api/rtu/document/save", json={
            "experiment_id": 2,
            "doc_type": "srs",
            "title": "Guest SRS",
            "content": {"title": "Guest project"}
        })
        self.assertEqual(saved.status_code, 200)
        result = second_guest.get("/api/rtu/document/2/srs")
        self.assertIsNone(result.get_json()["document"])

        response = first_guest.post("/api/tests/run", json={})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/rtu-lab")

    def test_private_work_is_scoped_to_signed_in_student(self):
        self.register(self.client, "student_a")
        saved = self.client.post("/api/rtu/document/save", json={
            "experiment_id": 2,
            "doc_type": "srs",
            "title": "Private SRS",
            "content": {"title": "Private project"}
        })
        self.assertEqual(saved.status_code, 200)

        other_client = lab_app.app.test_client()
        self.register(other_client, "student_b")
        result = other_client.get("/api/rtu/document/2/srs")
        self.assertEqual(result.status_code, 200)
        self.assertIsNone(result.get_json()["document"])

        own_result = self.client.get("/api/rtu/document/2/srs")
        self.assertEqual(own_result.get_json()["document"]["title"], "Private SRS")

    def test_completion_requires_checklist_quiz_and_saved_outputs(self):
        self.register(self.client, "student_a")
        blocked = self.client.post("/api/rtu/experiment/complete", json={"experiment_id": 1})
        self.assertEqual(blocked.status_code, 400)
        self.assertTrue(blocked.get_json()["missing"])

        invalid_quiz = self.client.post("/api/rtu/quiz/submit", json={
            "experiment_id": 1,
            "answers": {}
        })
        self.assertEqual(invalid_quiz.status_code, 400)

        checklist = self.client.post("/api/rtu/checklist/update", json={
            "experiment_id": 1,
            "completed": [0, 1, 2, 3, 4]
        })
        self.assertEqual(checklist.status_code, 200)

        quiz_data = lab_app.get_rtu_experiment_by_id(1)["quiz"]
        quiz = self.client.post("/api/rtu/quiz/submit", json={
            "experiment_id": 1,
            "answers": {str(index): question["correct"] for index, question in enumerate(quiz_data)}
        })
        self.assertEqual(quiz.status_code, 200)
        still_blocked = self.client.post("/api/rtu/experiment/complete", json={"experiment_id": 1})
        self.assertEqual(still_blocked.status_code, 400)
        self.assertIn("Save the sdlc choice document.", still_blocked.get_json()["missing"])

        self.client.post("/api/rtu/document/save", json={
            "experiment_id": 1,
            "doc_type": "sdlc_choice",
            "title": "SDLC Model",
            "content": {"model": "agile"}
        })
        self.client.post("/api/rtu/diagram/save", json={
            "experiment_id": 1,
            "diagram_type": "sdlc_model",
            "diagram_name": "Agile SDLC",
            "diagram_code": "graph LR\nA --> B"
        })
        demo = self.client.post("/api/rtu/demo/oop", json={})
        self.assertEqual(demo.status_code, 200)
        completed = self.client.post("/api/rtu/experiment/complete", json={"experiment_id": 1})
        self.assertEqual(completed.status_code, 200)
        self.assertEqual(completed.get_json()["status"], "COMPLETED")

    def test_guided_step_position_is_saved_and_restored(self):
        self.register(self.client, "student_a")
        response = self.client.post("/api/rtu/step/current", json={
            "experiment_id": 3,
            "step_num": 5
        })
        self.assertEqual(response.status_code, 200)
        page = self.client.get("/rtu-lab/experiment/3")
        self.assertIn(b"Viewing Step 5 of 8", page.data)

    def test_guest_save_and_srs_export_validation(self):
        response = self.client.post("/api/rtu/document/save", json={
            "experiment_id": 2,
            "doc_type": "srs",
            "title": "SRS",
            "content": {}
        })
        self.assertEqual(response.status_code, 200)

        fresh_guest = lab_app.app.test_client()
        fresh_guest.get("/rtu-lab")
        response = fresh_guest.get("/rtu-lab/export/srs-pdf")
        self.assertEqual(response.status_code, 400)

        self.register(self.client, "student_a")
        saved = self.client.post("/api/rtu/document/save", json={
            "experiment_id": 2,
            "doc_type": "srs",
            "title": "SRS",
            "content": {"title": "Test Project"}
        })
        self.assertEqual(saved.status_code, 200)
        response = self.client.get("/rtu-lab/export/srs-pdf")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/pdf")

    def test_legacy_user_schema_migrates_without_deleting_profiles(self):
        legacy_path = os.path.join(_test_directory.name, f"legacy-{uuid.uuid4().hex}.db")
        connection = sqlite3.connect(legacy_path)
        connection.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, role TEXT NOT NULL, name TEXT NOT NULL)"
        )
        connection.execute(
            "INSERT INTO users (username, role, name) VALUES ('old_student', 'student', 'Old Student')"
        )
        connection.commit()
        connection.close()

        models.DB_PATH = legacy_path
        models.init_db()
        user = models.get_user_by_username("old_student")
        self.assertEqual(user["name"], "Old Student")
        self.assertIsNone(user["password_hash"])
        self.assertIsNone(user["roll_no"])
        os.remove(legacy_path)

    def test_legacy_profile_session_cannot_access_student_records(self):
        models.save_document_record("student1", 2, "srs", "Old private SRS", {"title": "Private"})
        with self.client.session_transaction() as browser_session:
            browser_session["username"] = "student1"
            browser_session["name"] = "Legacy"
        response = self.client.get("/rtu-lab")
        self.assertEqual(response.status_code, 200)
        document = self.client.get("/api/rtu/document/2/srs").get_json()["document"]
        self.assertIsNone(document)


if __name__ == "__main__":
    unittest.main()
