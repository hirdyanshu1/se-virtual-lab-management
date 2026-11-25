"""
LabPilot AI — Interactive Software Engineering Virtual Laboratory
Main Application Server (Flask)

Features:
- Original LabPilot AI core: SRS builder, UML studio, GCC C test runner, Traceability matrix
- RTU Software Engineering Virtual Lab (B.Tech 3rd Semester, 7 Practicals)
- Step-by-step interactive guidance, SQLite persistence, self-assessment quizzes, and ReportLab PDF exports
"""

import os
import json
import sqlite3
import re
import secrets
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file

# Import core engine modules
import models
from engine.srs_checker import analyze_srs_document
from engine.code_runner import run_test_suite
from engine.traceability import generate_traceability_matrix
from engine.ai_copilot import diagnose_mistake_dna, generate_experiment_hints

# Import RTU curriculum modules
from engine.rtu_data import (
    RTU_EXPERIMENTS,
    get_rtu_experiment_by_id,
    get_all_rtu_experiments_summary
)
from engine.pdf_generator import (
    create_srs_pdf_buffer,
    create_experiment_report_pdf
)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("LABPILOT_SECRET_KEY") or os.urandom(32)

# Ensure database is initialized
models.init_db()

# ---------------------------------------------------------------------
# Student Profile & Session Management
# ---------------------------------------------------------------------
def get_current_student():
    """Return the signed-in student or this browser's isolated guest identity."""
    if session.get("authenticated") is True:
        username = session.get("username")
        if username:
            user = models.get_user_by_username(username)
            if user and user["role"] == "student":
                return {
                    "username": user["username"],
                    "name": user["name"],
                    "roll_no": user["roll_no"] or "",
                    "is_guest": False
                }
        session.clear()

    guest_id = session.get("guest_id")
    if isinstance(guest_id, str) and re.fullmatch(r"[a-f0-9]{32}", guest_id):
        return {
            "username": f"guest_{guest_id}",
            "name": "Guest",
            "roll_no": "",
            "is_guest": True
        }
    return None

@app.context_processor
def inject_student_profile():
    return {"current_student": get_current_student()}

@app.before_request
def require_student_session():
    if request.endpoint == "static":
        return None
    guest_route = (
        request.endpoint in ("dashboard", "student_login", "student_logout")
        or request.path.startswith("/rtu-lab")
        or request.path.startswith("/api/rtu/")
    )
    student = get_current_student()
    if student and (not student["is_guest"] or guest_route):
        return None
    if guest_route:
        session["guest_id"] = secrets.token_hex(16)
        return None
    return redirect(url_for("rtu_dashboard"))

@app.route("/login", methods=["GET", "POST"])
def student_login():
    return redirect(url_for("rtu_dashboard"))

@app.route("/profile", methods=["POST"])
def update_profile():
    student = get_current_student()
    name = request.form.get("name", "").strip()
    roll_no = request.form.get("roll_no", "").strip()
    if not name or not roll_no:
        return "Full name and roll number are required.", 400
    models.update_student_profile(student["username"], name, roll_no)
    return redirect(request.referrer or url_for("rtu_dashboard"))

@app.route("/logout")
def student_logout():
    session.clear()
    return redirect(url_for("student_login"))

# ---------------------------------------------------------------------
# Original LabPilot AI Core Routes (Preserved 100%)
# ---------------------------------------------------------------------
def get_experiment_data(code="EXP-01"):
    conn = models.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM experiments WHERE code = ?", (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

@app.route("/")
def dashboard():
    return redirect(url_for("rtu_dashboard"))

@app.route("/srs")
def srs_builder():
    exp = get_experiment_data("EXP-01")
    default_reqs = exp["default_requirements"] if exp else "[]"
    return render_template(
        "srs_builder.html",
        active_page="srs",
        default_requirements=default_reqs
    )

@app.route("/api/srs/analyze", methods=["POST"])
def api_analyze_srs():
    data = request.get_json() or {}
    requirements = data.get("requirements", [])
    report = analyze_srs_document(requirements)
    return jsonify(report)

@app.route("/uml")
def uml_studio():
    exp = get_experiment_data("EXP-01")
    default_uml = exp["default_uml"] if exp else ""
    return render_template(
        "uml_studio.html",
        active_page="uml",
        default_uml=default_uml
    )

@app.route("/workbench")
def workbench():
    exp = get_experiment_data("EXP-01")
    return render_template(
        "test_workbench.html",
        active_page="workbench",
        source_code_c=exp["source_code_c"] if exp else "",
        source_code_py=exp["source_code_py"] if exp else "",
        default_tests=exp["default_tests"] if exp else "[]"
    )

@app.route("/api/tests/run", methods=["POST"])
def api_run_tests():
    data = request.get_json() or {}
    language = data.get("language", "c")
    code = data.get("code", "")
    test_cases = data.get("test_cases", [])

    results = run_test_suite(language, code, test_cases)
    return jsonify(results)

@app.route("/api/dna/diagnose", methods=["POST"])
def api_diagnose_dna():
    data = request.get_json() or {}
    test_results = data.get("test_results", {})
    srs_results = data.get("srs_results", {})

    diagnosis = diagnose_mistake_dna(srs_results, test_results)
    return jsonify(diagnosis)

@app.route("/traceability")
def traceability():
    exp = get_experiment_data("EXP-01")
    reqs = json.loads(exp["default_requirements"]) if exp else []
    tests = json.loads(exp["default_tests"]) if exp else []
    uml_classes = ["TriangleValidator", "TestDriver"]

    matrix_data = generate_traceability_matrix(reqs, uml_classes, tests)
    return render_template(
        "traceability.html",
        active_page="traceability",
        matrix_data=matrix_data
    )

@app.route("/teacher")
def teacher_portal():
    return render_template("teacher.html", active_page="teacher")

# ---------------------------------------------------------------------
# RTU B.Tech Software Engineering Virtual Lab Routes
# ---------------------------------------------------------------------
@app.route("/rtu-lab")
def rtu_dashboard():
    student = get_current_student()
    experiments = get_all_rtu_experiments_summary()
    progress_data = models.get_all_rtu_progress(student["username"], total_experiments=len(experiments))
    
    return render_template(
        "rtu/dashboard.html",
        active_page="rtu_lab",
        experiments=experiments,
        progress_data=progress_data
    )

@app.route("/rtu-lab/experiment/<int:exp_id>")
def rtu_experiment_view(exp_id):
    student = get_current_student()
    exp = get_rtu_experiment_by_id(exp_id)
    if not exp:
        return redirect(url_for("rtu_dashboard"))
    
    progress = models.get_student_progress(student["username"], exp_id)
    return render_template(
        "rtu/experiment_view.html",
        active_page="rtu_lab",
        exp=exp,
        progress=progress
    )

# ---------------------------------------------------------------------
# RTU Virtual Lab REST APIs
# ---------------------------------------------------------------------
@app.route("/api/rtu/step/update", methods=["POST"])
def api_rtu_step_update():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
        step_num = int(data.get("step_num"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment and step are required."}), 400
    exp = get_rtu_experiment_by_id(exp_id)
    if not exp or step_num < 1 or step_num > len(exp["steps"]):
        return jsonify({"success": False, "error": "Experiment or step not found."}), 404
    is_completed = data.get("is_completed", True)
    if not isinstance(is_completed, bool):
        return jsonify({"success": False, "error": "is_completed must be true or false."}), 400

    res = models.update_step_progress(student["username"], exp_id, step_num, is_completed, len(exp["steps"]))
    return jsonify({"success": True, **res})

@app.route("/api/rtu/step/current", methods=["POST"])
def api_rtu_current_step():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
        step_num = int(data.get("step_num"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment and step are required."}), 400
    exp = get_rtu_experiment_by_id(exp_id)
    if not exp or step_num < 1 or step_num > len(exp["steps"]):
        return jsonify({"success": False, "error": "Experiment or step not found."}), 404
    models.set_current_step(student["username"], exp_id, step_num)
    return jsonify({"success": True, "current_step": step_num})

@app.route("/api/rtu/checklist/update", methods=["POST"])
def api_rtu_checklist_update():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment is required."}), 400
    exp = get_rtu_experiment_by_id(exp_id)
    completed = data.get("completed")
    if not exp or not isinstance(completed, list):
        return jsonify({"success": False, "error": "Invalid experiment checklist."}), 400
    if any(type(index) is not int or index < 0 or index >= len(exp["checklist"]) for index in completed):
        return jsonify({"success": False, "error": "Checklist item is out of range."}), 400

    completed = sorted(set(completed))
    models.update_checklist_progress(student["username"], exp_id, completed)
    return jsonify({"success": True, "completed": completed})

@app.route("/api/rtu/diagram/save", methods=["POST"])
def api_rtu_diagram_save():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment is required."}), 400
    diagram_type = data.get("diagram_type")
    diagram_name = data.get("diagram_name")
    diagram_code = data.get("diagram_code")
    if (not get_rtu_experiment_by_id(exp_id) or not isinstance(diagram_type, str)
            or not diagram_type.strip() or len(diagram_type) > 64
            or not isinstance(diagram_name, str) or not diagram_name.strip()
            or len(diagram_name) > 120 or not isinstance(diagram_code, str)
            or not diagram_code.strip() or len(diagram_code) > 100000):
        return jsonify({"success": False, "error": "Diagram details are missing or invalid."}), 400

    models.save_diagram_record(student["username"], exp_id, diagram_type, diagram_name, diagram_code)
    return jsonify({"success": True, "message": "Diagram saved successfully."})

@app.route("/api/rtu/diagram/<int:exp_id>/<diagram_type>", methods=["GET"])
def api_rtu_diagram_get(exp_id, diagram_type):
    student = get_current_student()
    if not get_rtu_experiment_by_id(exp_id):
        return jsonify({"success": False, "error": "Experiment not found."}), 404
    row = models.get_saved_diagram(student["username"], exp_id, diagram_type)
    return jsonify({"success": True, "diagram": row})

@app.route("/api/rtu/document/save", methods=["POST"])
def api_rtu_document_save():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment is required."}), 400
    doc_type = data.get("doc_type")
    title = data.get("title")
    content = data.get("content")
    if (not get_rtu_experiment_by_id(exp_id) or not isinstance(doc_type, str)
            or not doc_type.strip() or len(doc_type) > 64
            or not isinstance(title, str) or not title.strip() or len(title) > 120
            or not isinstance(content, (dict, list, str))
            or len(json.dumps(content)) > 200000):
        return jsonify({"success": False, "error": "Document details are missing or invalid."}), 400

    models.save_document_record(student["username"], exp_id, doc_type, title, content)
    return jsonify({"success": True, "message": "Document saved successfully."})

@app.route("/api/rtu/document/<int:exp_id>/<doc_type>", methods=["GET"])
def api_rtu_document_get(exp_id, doc_type):
    student = get_current_student()
    if not get_rtu_experiment_by_id(exp_id):
        return jsonify({"success": False, "error": "Experiment not found."}), 404
    doc = models.get_document_record(student["username"], exp_id, doc_type)
    return jsonify({"success": True, "document": doc})

@app.route("/api/rtu/demo/oop", methods=["POST"])
def api_rtu_oop_demo():
    class User:
        def __init__(self, username, name, role):
            self.username = username
            self.name = name
            self.role = role

    class Student(User):
        def __init__(self, username, name, roll_no):
            super().__init__(username, name, "student")
            self.roll_no = roll_no
            self.completed_experiments = []

        def enroll(self, experiment_code):
            self.completed_experiments.append(experiment_code)
            return f"Student {self.name} ({self.roll_no}) completed {experiment_code}."

    student = Student("rahul01", "Rahul Sharma", "22EBKCS042")
    output = "\n".join((
        student.enroll("RTU-SE-01"),
        f"Object attributes: {student.__dict__}"
    ))
    current_student = get_current_student()
    models.save_document_record(
        current_student["username"],
        1,
        "oop_demo",
        "Python OOP Demonstration Output",
        {"output": output}
    )
    return jsonify({"success": True, "output": output})

@app.route("/api/rtu/quiz/submit", methods=["POST"])
def api_rtu_quiz_submit():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment is required."}), 400
    submitted_answers = data.get("answers", {}) # { "0": 1, "1": 2, ... }

    exp = get_rtu_experiment_by_id(exp_id)
    if not exp or "quiz" not in exp or not isinstance(submitted_answers, dict):
        return jsonify({"success": False, "error": "Invalid experiment."}), 400

    score = 0
    total = len(exp["quiz"])
    results = []

    for idx, q in enumerate(exp["quiz"]):
        selected = submitted_answers.get(str(idx))
        if selected is None:
            selected = submitted_answers.get(idx)
        try:
            selected = int(selected)
        except (TypeError, ValueError):
            return jsonify({"success": False, "error": f"Answer question {idx + 1} before submitting."}), 400
        if selected < 0 or selected >= len(q["options"]):
            return jsonify({"success": False, "error": f"Answer for question {idx + 1} is invalid."}), 400

        is_correct = selected == q["correct"]
        if is_correct:
            score += 1
        
        results.append({
            "question_index": idx,
            "selected": selected,
            "correct": q["correct"],
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })

    models.save_quiz_attempt(student["username"], exp_id, score, total, submitted_answers)
    return jsonify({
        "success": True,
        "score": score,
        "max_score": total,
        "results": results
    })

def get_missing_completion_requirements(username, exp):
    exp_id = exp["id"]
    progress = models.get_student_progress(username, exp_id)
    missing = []

    expected_checks = set(range(len(exp["checklist"])))
    if set(progress["checklist"]) != expected_checks:
        missing.append("Complete every item in the practical checklist.")
    if not models.get_quiz_attempt(username, exp_id):
        missing.append("Submit the self-assessment quiz.")

    required_diagrams = {
        1: ["sdlc_model"],
        3: ["dfd_level_0", "dfd_level_1"],
        4: ["structure_chart"],
        5: ["structural_class", "structural_object", "structural_component", "structural_deploy", "structural_pkg"],
        6: ["behavioural_usecase", "behavioural_activity", "behavioural_sequence", "behavioural_state"]
    }.get(exp_id, [])
    for diagram_type in required_diagrams:
        if not models.get_saved_diagram(username, exp_id, diagram_type):
            missing.append(f"Save the {diagram_type.replace('_', ' ')} diagram.")

    required_documents = {
        1: ["sdlc_choice", "oop_demo"],
        2: ["srs"],
        3: ["data_dictionary"],
        7: ["gantt_schedule"]
    }.get(exp_id, [])
    for doc_type in required_documents:
        if not models.get_document_record(username, exp_id, doc_type):
            missing.append(f"Save the {doc_type.replace('_', ' ')} document.")
    return missing

@app.route("/api/rtu/experiment/complete", methods=["POST"])
def api_rtu_experiment_complete():
    student = get_current_student()
    data = request.get_json() or {}
    try:
        exp_id = int(data.get("experiment_id"))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "A valid experiment is required."}), 400
    exp = get_rtu_experiment_by_id(exp_id)
    if not exp:
        return jsonify({"success": False, "error": "Experiment not found."}), 404
    missing = get_missing_completion_requirements(student["username"], exp)
    if missing:
        return jsonify({
            "success": False,
            "error": "Complete the required activities before finishing this experiment.",
            "missing": missing
        }), 400
    new_status = models.set_experiment_completed(student["username"], exp_id, is_completed=True)
    return jsonify({"success": True, "status": new_status})

# ---------------------------------------------------------------------
# ReportLab PDF Export Routes
# ---------------------------------------------------------------------
@app.route("/rtu-lab/export/srs-pdf")
def export_srs_pdf():
    student = get_current_student()
    doc_record = models.get_document_record(student["username"], 2, "srs")
    if not doc_record or not isinstance(doc_record.get("content"), dict):
        return "Save a valid SRS document before exporting the PDF.", 400
    srs_data = doc_record["content"]
    
    pdf_buffer = create_srs_pdf_buffer(
        srs_data,
        student_name=student["name"],
        roll_no=student["roll_no"]
    )
    
    filename = f"IEEE_830_SRS_{student['roll_no']}.pdf"
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf"
    )

@app.route("/rtu-lab/export/report-pdf/<int:exp_id>")
def export_experiment_report_pdf(exp_id):
    student = get_current_student()
    progress = models.get_student_progress(student["username"], exp_id)
    
    pdf_buffer = create_experiment_report_pdf(
        exp_id,
        student_name=student["name"],
        roll_no=student["roll_no"],
        progress_data=progress
    )
    if not pdf_buffer:
        return "Experiment not found", 404

    filename = f"RTU_SE_Exp{exp_id}_Report_{student['roll_no']}.pdf"
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf"
    )

# ---------------------------------------------------------------------
# Server Startup
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 65)
    print("🚀 LabPilot AI — RTU Software Engineering Virtual Lab Server")
    print("👉 Running at: http://127.0.0.1:5000")
    print("=" * 65)
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
