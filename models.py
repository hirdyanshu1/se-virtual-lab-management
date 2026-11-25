"""
Database & Models Module (SQLite3)
LabPilot AI — Software Engineering Virtual Lab

Uses lightweight standard library sqlite3 for zero-configuration,
single-file database persistence.
"""

import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "labpilot.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        role TEXT NOT NULL,
        name TEXT NOT NULL,
        roll_no TEXT,
        password_hash TEXT
    )
    """)

    user_columns = {row["name"] for row in cursor.execute("PRAGMA table_info(users)")}
    if "roll_no" not in user_columns:
        cursor.execute("ALTER TABLE users ADD COLUMN roll_no TEXT")
    if "password_hash" not in user_columns:
        cursor.execute("ALTER TABLE users ADD COLUMN password_hash TEXT")

    # 2. Experiments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS experiments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        objective TEXT NOT NULL,
        source_code_c TEXT,
        source_code_py TEXT,
        default_requirements TEXT,
        default_uml TEXT,
        default_tests TEXT
    )
    """)

    # 3. Submissions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        experiment_code TEXT NOT NULL,
        srs_json TEXT,
        uml_code TEXT,
        test_json TEXT,
        score INTEGER DEFAULT 0,
        mistake_dna_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 4. RTU Student Progress table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_username TEXT NOT NULL,
        experiment_id INTEGER NOT NULL,
        status TEXT DEFAULT 'NOT_STARTED',
        current_step INTEGER DEFAULT 1,
        completed_steps_json TEXT DEFAULT '[]',
        checklist_json TEXT DEFAULT '[]',
        quiz_score INTEGER DEFAULT 0,
        quiz_total INTEGER DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(student_username, experiment_id)
    )
    """)

    # 5. RTU Saved Diagrams table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saved_diagrams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_username TEXT NOT NULL,
        experiment_id INTEGER NOT NULL,
        diagram_type TEXT NOT NULL,
        diagram_name TEXT NOT NULL,
        diagram_code TEXT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(student_username, experiment_id, diagram_type)
    )
    """)

    # 6. RTU Practical Documents table (SRS, Data Dictionary, Tasks)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS practical_documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_username TEXT NOT NULL,
        experiment_id INTEGER NOT NULL,
        doc_type TEXT NOT NULL,
        title TEXT NOT NULL,
        content_json TEXT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(student_username, experiment_id, doc_type)
    )
    """)

    # 7. RTU Quiz Attempts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_username TEXT NOT NULL,
        experiment_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        max_score INTEGER NOT NULL,
        answers_json TEXT NOT NULL,
        attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 8. RTU Experiment Submissions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS experiment_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_username TEXT NOT NULL,
        experiment_id INTEGER NOT NULL,
        status TEXT DEFAULT 'SUBMITTED',
        notes TEXT,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(student_username, experiment_id)
    )
    """)

    # Seed Default Users
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, role, name) VALUES ('student1', 'student', 'Rahul Sharma')")
        cursor.execute("INSERT INTO users (username, role, name) VALUES ('teacher1', 'teacher', 'Prof. Sunita Rao')")

    # Seed Experiment 1: Triangle Classification
    cursor.execute("SELECT COUNT(*) FROM experiments WHERE code = 'EXP-01'")
    if cursor.fetchone()[0] == 0:
        triangle_c = """#include <stdio.h>

int main() {
    int a, b, c;
    if (scanf("%d %d %d", &a, &b, &c) != 3) {
        printf("ERROR\\n");
        return 1;
    }

    if (a <= 0 || b <= 0 || c <= 0) {
        printf("NOT_A_TRIANGLE\\n");
        return 0;
    }

    if ((a + b <= c) || (a + c <= b) || (b + c <= a)) {
        printf("NOT_A_TRIANGLE\\n");
        return 0;
    }

    if (a == b && b == c) {
        printf("EQUILATERAL\\n");
    } else if (a == b || b == c || a == c) {
        printf("ISOSCELES\\n");
    } else {
        printf("SCALENE\\n");
    }

    return 0;
}"""

        triangle_py = """import sys

def main():
    try:
        raw = sys.stdin.read().split()
        if len(raw) < 3:
            print("ERROR")
            return
        a = int(raw[0])
        b = int(raw[1])
        c = int(raw[2])
    except Exception:
        print("ERROR")
        return

    if a <= 0 or b <= 0 or c <= 0:
        print("NOT_A_TRIANGLE")
        return

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("NOT_A_TRIANGLE")
        return

    if a == b == c:
        print("EQUILATERAL")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")

if __name__ == "__main__":
    main()"""

        default_reqs = json.dumps([
            {"id": "REQ-01", "text": "The system shall accept three positive integer values representing the side lengths of a triangle.", "type": "Functional", "priority": "Must-Have"},
            {"id": "REQ-02", "text": "The system shall output 'EQUILATERAL' if all three sides are equal.", "type": "Functional", "priority": "Must-Have"},
            {"id": "REQ-03", "text": "The system shall output 'ISOSCELES' if exactly two sides are equal.", "type": "Functional", "priority": "Must-Have"},
            {"id": "REQ-04", "text": "The system shall output 'SCALENE' if all three sides have different lengths.", "type": "Functional", "priority": "Must-Have"},
            {"id": "REQ-05", "text": "The system shall output 'NOT_A_TRIANGLE' if the sum of any two sides is less than or equal to the third side.", "type": "Functional", "priority": "Must-Have"},
            {"id": "REQ-06", "text": "The system shall validate inputs and respond within 100 milliseconds.", "type": "Non-Functional", "priority": "Should-Have"}
        ])

        default_uml = """classDiagram
    class TriangleValidator {
        +int sideA
        +int sideB
        +int sideC
        +bool isValid()
        +string classify()
    }
    class TestDriver {
        +runTestCase()
        +displayResult()
    }
    TestDriver --> TriangleValidator : tests"""

        default_tests = json.dumps([
            {"id": "TC-01", "name": "Equilateral Triangle", "input": "5 5 5", "expected": "EQUILATERAL", "target_req": "REQ-02"},
            {"id": "TC-02", "name": "Isosceles Triangle", "input": "5 5 8", "expected": "ISOSCELES", "target_req": "REQ-03"},
            {"id": "TC-03", "name": "Scalene Triangle", "input": "3 4 5", "expected": "SCALENE", "target_req": "REQ-04"},
            {"id": "TC-04", "name": "Boundary: Triangle Inequality Fail", "input": "1 2 3", "expected": "NOT_A_TRIANGLE", "target_req": "REQ-05"},
            {"id": "TC-05", "name": "Boundary: Negative Side Length", "input": "-1 4 5", "expected": "NOT_A_TRIANGLE", "target_req": "REQ-01"},
            {"id": "TC-06", "name": "Boundary: Zero Side Length", "input": "0 4 4", "expected": "NOT_A_TRIANGLE", "target_req": "REQ-01"}
        ])

        cursor.execute("""
        INSERT INTO experiments (code, title, category, objective, source_code_c, source_code_py, default_requirements, default_uml, default_tests)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'EXP-01',
            'Triangle Classification & Boundary Value Analysis',
            'Black-Box Testing & OOAD',
            'Design an SRS, UML Class Diagram, and boundary-value test suite to verify a triangle classification algorithm.',
            triangle_c,
            triangle_py,
            default_reqs,
            default_uml,
            default_tests
        ))

    conn.commit()
    conn.close()

# =====================================================================
# RTU VIRTUAL LAB HELPER FUNCTIONS
# =====================================================================

def get_or_create_user(username, name="Student", role="student"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("INSERT INTO users (username, role, name) VALUES (?, ?, ?)", (username, role, name))
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
    user_dict = dict(row)
    conn.close()
    return user_dict

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def create_student(username, name, roll_no, password_hash):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, role, name, roll_no, password_hash) VALUES (?, 'student', ?, ?, ?)",
            (username, name, roll_no, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        conn.rollback()
        return False
    finally:
        conn.close()

def update_student_profile(username, name, roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name = ?, roll_no = ? WHERE username = ? AND role = 'student'",
        (name, roll_no, username)
    )
    conn.commit()
    updated = cursor.rowcount == 1
    conn.close()
    return updated

def get_student_progress(username, exp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_progress WHERE student_username = ? AND experiment_id = ?", (username, exp_id))
    row = cursor.fetchone()
    conn.close()
    if row:
        data = dict(row)
        try:
            data["completed_steps"] = json.loads(data.get("completed_steps_json") or "[]")
        except Exception:
            data["completed_steps"] = []
        try:
            data["checklist"] = json.loads(data.get("checklist_json") or "[]")
        except Exception:
            data["checklist"] = []
        return data
    return {
        "student_username": username,
        "experiment_id": exp_id,
        "status": "NOT_STARTED",
        "current_step": 1,
        "completed_steps": [],
        "checklist": [],
        "quiz_score": 0,
        "quiz_total": 0
    }

def update_step_progress(username, exp_id, step_num, is_completed=True, total_steps=8):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_progress WHERE student_username = ? AND experiment_id = ?", (username, exp_id))
    row = cursor.fetchone()
    
    completed_steps = []
    status = "IN_PROGRESS"
    if row:
        try:
            completed_steps = json.loads(row["completed_steps_json"] or "[]")
        except Exception:
            completed_steps = []
        status = row["status"]

    if is_completed:
        if step_num not in completed_steps:
            completed_steps.append(step_num)
    else:
        if step_num in completed_steps:
            completed_steps.remove(step_num)

    completed_steps.sort()
    if status != "COMPLETED":
        status = "IN_PROGRESS"

    cursor.execute("""
    INSERT INTO student_progress (student_username, experiment_id, status, current_step, completed_steps_json, updated_at)
    VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id) DO UPDATE SET
        status = ?,
        current_step = ?,
        completed_steps_json = ?,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, status, step_num, json.dumps(completed_steps), status, step_num, json.dumps(completed_steps)))
    
    conn.commit()
    conn.close()
    return {"status": status, "completed_steps": completed_steps, "current_step": step_num}

def set_current_step(username, exp_id, step_num):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO student_progress (student_username, experiment_id, status, current_step, updated_at)
    VALUES (?, ?, 'IN_PROGRESS', ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id) DO UPDATE SET
        current_step = ?,
        status = CASE WHEN status = 'COMPLETED' THEN status ELSE 'IN_PROGRESS' END,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, step_num, step_num))
    conn.commit()
    conn.close()

def update_checklist_progress(username, exp_id, checklist_list):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO student_progress (student_username, experiment_id, status, checklist_json, updated_at)
    VALUES (?, ?, 'IN_PROGRESS', ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id) DO UPDATE SET
        checklist_json = ?,
        status = CASE WHEN status = 'COMPLETED' THEN status ELSE 'IN_PROGRESS' END,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, json.dumps(checklist_list), json.dumps(checklist_list)))
    conn.commit()
    conn.close()

def set_experiment_completed(username, exp_id, is_completed=True):
    conn = get_connection()
    cursor = conn.cursor()
    new_status = "COMPLETED" if is_completed else "IN_PROGRESS"
    cursor.execute("""
    INSERT INTO student_progress (student_username, experiment_id, status, updated_at)
    VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id) DO UPDATE SET
        status = ?,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, new_status, new_status))
    conn.commit()
    conn.close()
    return new_status

def get_all_rtu_progress(username, total_experiments=7):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_progress WHERE student_username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()

    progress_map = {}
    completed_count = 0
    in_progress_count = 0

    for r in rows:
        exp_id = r["experiment_id"]
        status = r["status"]
        try:
            completed_steps = json.loads(r["completed_steps_json"] or "[]")
        except Exception:
            completed_steps = []
        progress_pct = round((len(completed_steps) / 8.0) * 100)
        if status == "COMPLETED":
            progress_pct = 100
            completed_count += 1
        elif status == "IN_PROGRESS":
            in_progress_count += 1

        progress_map[exp_id] = {
            "status": status,
            "current_step": r["current_step"],
            "completed_steps": completed_steps,
            "progress_percent": progress_pct,
            "quiz_score": r["quiz_score"],
            "quiz_total": r["quiz_total"]
        }

    overall_percent = round((completed_count / float(total_experiments)) * 100) if total_experiments > 0 else 0

    return {
        "progress_map": progress_map,
        "completed_count": completed_count,
        "in_progress_count": in_progress_count,
        "total_experiments": total_experiments,
        "overall_percent": overall_percent
    }

def save_diagram_record(username, exp_id, diagram_type, diagram_name, diagram_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO saved_diagrams (student_username, experiment_id, diagram_type, diagram_name, diagram_code, updated_at)
    VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id, diagram_type) DO UPDATE SET
        diagram_name = ?,
        diagram_code = ?,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, diagram_type, diagram_name, diagram_code, diagram_name, diagram_code))
    conn.commit()
    conn.close()

def get_saved_diagram(username, exp_id, diagram_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM saved_diagrams 
    WHERE student_username = ? AND experiment_id = ? AND diagram_type = ?
    """, (username, exp_id, diagram_type))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def save_document_record(username, exp_id, doc_type, title, content_data):
    conn = get_connection()
    cursor = conn.cursor()
    content_json = json.dumps(content_data) if not isinstance(content_data, str) else content_data
    cursor.execute("""
    INSERT INTO practical_documents (student_username, experiment_id, doc_type, title, content_json, updated_at)
    VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id, doc_type) DO UPDATE SET
        title = ?,
        content_json = ?,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, doc_type, title, content_json, title, content_json))
    conn.commit()
    conn.close()

def get_document_record(username, exp_id, doc_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM practical_documents 
    WHERE student_username = ? AND experiment_id = ? AND doc_type = ?
    """, (username, exp_id, doc_type))
    row = cursor.fetchone()
    conn.close()
    if row:
        d = dict(row)
        try:
            d["content"] = json.loads(d["content_json"])
        except Exception:
            d["content"] = d["content_json"]
        return d
    return None

def save_quiz_attempt(username, exp_id, score, max_score, answers_dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO quiz_attempts (student_username, experiment_id, score, max_score, answers_json, attempted_at)
    VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, (username, exp_id, score, max_score, json.dumps(answers_dict)))
    
    # Also update student_progress table
    cursor.execute("""
    INSERT INTO student_progress (student_username, experiment_id, quiz_score, quiz_total, updated_at)
    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(student_username, experiment_id) DO UPDATE SET
        quiz_score = ?,
        quiz_total = ?,
        updated_at = CURRENT_TIMESTAMP
    """, (username, exp_id, score, max_score, score, max_score))
    
    conn.commit()
    conn.close()

def get_quiz_attempt(username, exp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM quiz_attempts 
    WHERE student_username = ? AND experiment_id = ? 
    ORDER BY id DESC LIMIT 1
    """, (username, exp_id))
    row = cursor.fetchone()
    conn.close()
    if row:
        d = dict(row)
        try:
            d["answers"] = json.loads(d["answers_json"])
        except Exception:
            d["answers"] = {}
        return d
    return None

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully at", DB_PATH)
