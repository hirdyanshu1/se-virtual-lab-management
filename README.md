# LabPilot AI — Interactive Software Engineering Virtual Laboratory

> A practical-first learning platform for university Software Engineering labs. Connects IEEE 830 Requirements (SRS), OOAD Design (Mermaid.js UML), and Code Execution (C/C++ & Python) with automated feedback and Mistake DNA diagnosis.

---

## 🛠️ Technology Stack (Simple & Grounded)
* **Backend:** Python 3 (Flask)
* **Database:** SQLite3 (`labpilot.db` — native standard library)
* **Code Execution:** MinGW GCC (`gcc.exe`) for C/C++ & Python interpreter
* **Frontend:** HTML5, CSS3, JavaScript (Bootstrap 5, FontAwesome)
* **Diagrams:** Mermaid.js (client-side text-to-UML rendering)

---

## 🚀 Quick Start (Running the Lab)

1. **Option A (One-Click):**
   Double-click `run.bat` in this folder.

2. **Option B (Command Line):**
   ```bash
   cd labpilot_ai
   python app.py
   ```

3. Open your web browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## 📂 Core Laboratory Modules

### 1. Smart SRS Builder (`/srs`)
* Interactive table to formulate Functional and Non-Functional requirements following IEEE 830.
* Real-time ambiguity detection flags subjective words (`fast`, `user-friendly`, `secure`, `approximate`).
* Computes Quality Index score (A/B/C/D) and provides specific improvement advice.

### 2. Interactive UML Studio (`/uml`)
* Text-to-UML editor using Mermaid.js syntax.
* Live SVG vector rendering for Class diagrams, Use-Case diagrams, and Sequence diagrams.
* Checks consistency between classes and SRS requirements.

### 3. Software Testing Workbench (`/workbench`)
* Real compilation and execution of C code (`triangle.c`) using MinGW GCC or Python (`triangle.py`).
* Tests input against boundary values:
  * Equilateral: `5 5 5`
  * Isosceles: `5 5 8`
  * Scalene: `3 4 5`
  * Triangle Inequality Failure: `1 2 3`
  * Boundary Negatives: `-1 4 5`
  * Boundary Zeros: `0 4 4`
* Reports stdout comparison, execution time (ms), and pass/fail metrics.

### 4. Traceability Matrix (`/traceability`)
* Bi-directional mapping: `REQ-ID` ➔ `UML Class` ➔ `Test Case IDs`.
* Detects uncovered requirements and calculates V&V test coverage percentage.

### 5. Teacher Portal & Mistake DNA (`/teacher`)
* Rubric-based scoring breakdown (SRS Clarity 30%, UML 30%, Testing 40%).
* Cohort-wide error pattern analytics (e.g. 74% students missing boundary tests).
* Viva Voce question generator for examiners.

## Guest access and RTU practicals

The application opens directly to the RTU Virtual Lab. Sign-in is temporarily
disabled; each browser receives a separate guest identity, and practical documents,
diagrams, checklists, quiz attempts, and completion records are scoped to that
identity. Guest progress is tied to the browser's session cookie and may be lost
when cookies are cleared or the server's session key changes. Do not expose this
temporary guest mode to the public internet.

The RTU Virtual Lab includes seven guided experiments. Guided-step position and
completion checklists are saved as students work. An experiment can only be
completed after its checklist, quiz, and required saved practical outputs are
present. Saved diagrams can be downloaded as PNG. The Experiment 7 workspace
saves its task schedule in LabPilot; it does not generate a native ProjectLibre
project file. The legacy code-execution workbench remains unavailable to guest
sessions.

For deployments beyond local classroom use, set `LABPILOT_SECRET_KEY` to a
private, persistent random value before starting Flask. Without it, the app
creates a per-process key and signing sessions will expire when the app restarts.
