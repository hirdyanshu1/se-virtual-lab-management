"""
RTU B.Tech 3rd Semester Software Engineering Virtual Lab Data Module
LabPilot AI — Interactive Educational Platform

Contains complete syllabus definitions, theory, procedures, guided steps,
worked examples, templates, quizzes, and viva questions for all 7 RTU experiments.
"""

RTU_EXPERIMENTS = [
    {
        "id": 1,
        "code": "RTU-SE-01",
        "title": "Study and Demonstration of SDLC, Function-Oriented Design and Object-Oriented Design",
        "category": "SDLC & Design Paradigms",
        "duration": "2 Hours",
        "difficulty": "Beginner",
        "short_desc": "Understand Software Development Life Cycle (SDLC) models, compare Structured Analysis/Design (SA/SD) with Object-Oriented Design (OOD), and execute demonstration test cases.",
        "learning_objectives": [
            "Understand the fundamental stages of SDLC from requirements to maintenance.",
            "Compare Waterfall, Agile, Spiral, and Prototyping process models with practical trade-offs.",
            "Understand Structured Analysis & Structured Design (SA/SD) and functional decomposition.",
            "Master Object-Oriented Design principles (Classes, Objects, Encapsulation, Inheritance, Association).",
            "Learn boundary test case design and execute Python demonstration programs.",
            "Understand Computer-Aided Software Engineering (CASE) tools, VS Code, Git, and GitHub."
        ],
        "theory_sections": [
            {
                "heading": "1. What is SDLC & Why is it Required?",
                "content": """
**Software Development Life Cycle (SDLC)** is a systematic, structured process for building high-quality software that meets or exceeds customer expectations within cost and time estimates.

Without an SDLC process, software projects often face scope creep, frequent bugs, missed deadlines, and unmaintainable code.

### Core Stages of SDLC:
1. **Requirement Analysis:** Gathering user needs, defining scope, and drafting the Software Requirements Specification (SRS).
2. **System Design:** Architectural planning, High-Level Design (HLD), Low-Level Design (LLD), database schemas, and UML models.
3. **Implementation (Coding):** Writing source code in chosen programming languages (e.g., Python, C/C++) adhering to coding guidelines.
4. **Testing:** Verifying requirements via Black-box, White-box, Unit, Integration, and System testing.
5. **Deployment:** Releasing the application to production or staging environments for end-user adoption.
6. **Maintenance:** Corrective, adaptive, perfective, and preventive changes over the product's operational lifespan.
"""
            },
            {
                "heading": "2. Comparative Study of SDLC Models",
                "content": """
| SDLC Model | Definition & Workflow | Key Advantages | Disadvantages | Real-World Example |
| :--- | :--- | :--- | :--- | :--- |
| **Waterfall Model** | Linear-sequential flow. Each phase must complete before the next begins. | Simple to manage, rigid milestones, well-documented. | Inflexible to changing requirements; working software delivered late. | Banking Transaction Engine, Medical pacemaker firmware. |
| **Agile (Scrum)** | Iterative and incremental development delivered in 2–4 week sprints. | Highly flexible, continuous customer feedback, early working software. | Requires disciplined teams; hard to predict final cost upfront. | Web/Mobile apps, SaaS platforms, LabPilot AI development. |
| **Spiral Model** | Risk-driven model combining iterative prototyping with Waterfall phases. | Excellent risk management, realistic budgeting, early feedback. | Costly, complex to manage, requires risk evaluation expertise. | Military defense systems, Spacecraft trajectory software. |
| **Prototyping** | Building an early scaled-down mock model to clarify vague requirements. | Clear user communication, minimizes requirement misunderstandings. | Can lead to throwaway code, scope creep, false user expectations. | E-commerce UI redesign, new interactive educational tools. |
"""
            },
            {
                "heading": "3. Function-Oriented Design (SA/SD) vs. Object-Oriented Design (OOD)",
                "content": """
### A. Function-Oriented Design (Structured Analysis / Structured Design)
* Focuses on **functions and data transformations**.
* Uses **top-down decomposition**: A complex problem is broken into smaller functions/subroutines.
* Core tools: Data Flow Diagrams (DFDs), Structure Charts, Data Dictionaries.
* *LabPilot Example:* The system is broken into `Authentication`, `SRS_Management`, `Test_Execution`, and `Progress_Evaluation`.

### B. Object-Oriented Design (OOD)
* Focuses on **real-world entities (objects) that encapsulate both state (data) and behavior (functions)**.
* Core principles:
  * **Class:** Blueprint or template (e.g., `class Student`, `class TestCase`).
  * **Object:** Concrete instance with identity (e.g., `student1 = Student(name="Rahul")`).
  * **Encapsulation:** Binding data and methods into a single unit while hiding internal implementation.
  * **Inheritance:** Deriving new classes from parent classes to promote reusability (e.g., `Teacher` and `Student` inherit from `User`).
  * **Polymorphism:** Performing a single action in different ways (e.g., `execute()` method behaves differently for C vs Python test runners).
  * **Association / Aggregation:** Describing relationships between classes (e.g., `VirtualLab` *has-a* collection of `Experiment` objects).
"""
            },
            {
                "heading": "4. Software Engineering CASE & Configuration Tools",
                "content": """
Modern software engineers rely on dedicated tools across the lifecycle:
* **Diagramming / CASE Tools:** Draw.io, Visual Paradigm, Mermaid.js for architectural diagrams and DFDs.
* **Configuration Management:** **Git** (version tracking) and **GitHub** (remote collaboration, pull requests, issue tracking).
* **Code Analysis & Linters:** **Pylint** and Flake8 for Python code quality, PEP 8 compliance, and vulnerability checks.
* **Integrated Development Environment (IDE):** Visual Studio Code (VS Code) with extensions for language runtimes, debugging, and terminal execution.
"""
            }
        ],
        "procedure": [
            "Review the primary SDLC stages and choose an appropriate model for the LabPilot Virtual Lab project.",
            "Decompose the LabPilot system into functional modules (Function-Oriented SA/SD).",
            "Model the core entities as Object-Oriented classes (Student, Teacher, Experiment, TestCase).",
            "Formulate 4 standard boundary test cases (Valid Login, Invalid Login, Empty Input, Code Runner Execution).",
            "Execute the provided Python demonstration program and analyze its object-oriented output.",
            "Complete the guided checklist, attempt the self-assessment quiz, and save your experiment report."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Select SDLC Model for LabPilot AI",
                "instruction": "Analyze the project requirements and decide whether Waterfall or Agile is best suited for an educational web platform with evolving lab experiments.",
                "example": "Agile (Scrum) is chosen because educational requirements evolve with university feedback and sprints allow bi-weekly feature deployments.",
                "expected_output": "Agile Scrum selected with 2-week sprint cycles."
            },
            {
                "step_num": 2,
                "title": "Deconstruct System into Functional Modules",
                "instruction": "Perform functional decomposition (Structured Design) to identify top-level modules and their sub-functions.",
                "example": "LabPilot System -> [Auth Module, SRS Module, UML Studio, Test Workbench, Progress Tracker].",
                "expected_output": "Hierarchical module list displaying top-down functional decomposition."
            },
            {
                "step_num": 3,
                "title": "Define Object-Oriented Classes & Attributes",
                "instruction": "Identify entities, class attributes, and methods in Python syntax representing Student, Experiment, and TestCase.",
                "example": "Class `Student(User)` with attributes `roll_no`, `semester`, and methods `submit_experiment()`.",
                "expected_output": "Well-defined classes with encapsulated attributes and public methods."
            },
            {
                "step_num": 4,
                "title": "Design Black-Box Test Cases",
                "instruction": "Draft a test case table for student authentication specifying Test ID, Scenario, Input, and Expected Output.",
                "example": "TC-01: Valid user & password -> Redirect to Dashboard; TC-02: Incorrect password -> Display 'Invalid credentials'.",
                "expected_output": "Test case matrix covering positive, negative, and empty field scenarios."
            },
            {
                "step_num": 5,
                "title": "Run Demonstration Python Script",
                "instruction": "Execute the embedded Python OOP script demonstrating inheritance and encapsulation for LabPilot.",
                "example": "Run `python -c` or click 'Execute Demonstration' to observe class instantiation and method execution.",
                "expected_output": "Console output showing `Student Rahul Sharma enrolled in RTU-SE-01` and test validation."
            },
            {
                "step_num": 6,
                "title": "Inspect CASE & Git Configuration",
                "instruction": "Learn how Git commands (`git init`, `git add`, `git commit`, `git push`) track modifications to software engineering deliverables.",
                "example": "`git commit -m 'feat: added RTU experiment 1 module'`",
                "expected_output": "Understanding of local commit vs remote repository version control."
            },
            {
                "step_num": 7,
                "title": "Take Self-Assessment Quiz",
                "instruction": "Answer the 5 multiple choice questions testing your grasp on SDLC, SA/SD, and OOD principles.",
                "example": "Select radio buttons and click 'Submit Quiz' to view immediate scoring and rationale.",
                "expected_output": "Quiz score >= 80% recorded in your student progress tracker."
            },
            {
                "step_num": 8,
                "title": "Review Viva Voce Questions & Complete Experiment",
                "instruction": "Read through key viva voce questions and check off the experiment completion requirements.",
                "example": "Prepare answers for 'Difference between Verification & Validation' and 'Why Spiral model is risk-driven'.",
                "expected_output": "Experiment status updated to COMPLETED with printable report."
            }
        ],
        "worked_example": {
            "title": "LabPilot AI Architectural Decomposition",
            "content": """
### Structured Analysis Breakdown (Function-Oriented):
* **1.0 User Authentication Subsystem**
  * 1.1 Student Registration & Validation
  * 1.2 Credential Verification & Session Initialization
* **2.0 Virtual Laboratory Subsystem**
  * 2.1 Experiment Catalog Provider
  * 2.2 Interactive Guided Step Controller
  * 2.3 Code Execution Worker (GCC & Python)
* **3.0 Assessment & Progress Subsystem**
  * 3.1 Quiz Evaluation & Scoring
  * 3.2 Diagram & SRS Document Archiver

### Object-Oriented Python Model:
```python
class User:
    def __init__(self, username, name, role):
        self.username = username
        self.name = name
        self.role = role

class Student(User):
    def __init__(self, username, name, roll_no):
        super().__init__(username, name, role="student")
        self.roll_no = roll_no
        self.completed_experiments = []

    def complete_experiment(self, exp_id):
        if exp_id not in self.completed_experiments:
            self.completed_experiments.append(exp_id)
        return f"Experiment {exp_id} marked complete for {self.name}."

# Demonstration
s1 = Student("rahul01", "Rahul Sharma", "22EBKCS042")
print(s1.complete_experiment("RTU-SE-01"))
```
"""
        },
        "quiz": [
            {
                "question": "Which SDLC model is most suitable for projects where requirements are well-understood, stable, and unlikely to change?",
                "options": ["Agile Scrum", "Waterfall Model", "Spiral Model", "Evolutionary Prototyping"],
                "correct": 1,
                "explanation": "Waterfall is linear-sequential and excels when requirements are completely fixed and documented upfront."
            },
            {
                "question": "In Object-Oriented Design, what is the concept of bundling data and the methods that operate on that data called?",
                "options": ["Inheritance", "Polymorphism", "Encapsulation", "Cohesion"],
                "correct": 2,
                "explanation": "Encapsulation restricts direct access to an object's internal components and binds data with methods."
            },
            {
                "question": "What is the primary distinguishing characteristic of the Spiral Model?",
                "options": ["Zero documentation", "Heavy emphasis on Risk Analysis at every cycle", "No customer involvement", "Linear execution without loops"],
                "correct": 1,
                "explanation": "The Spiral model is fundamentally risk-driven, evaluating and mitigating technical and financial risks in each loop."
            },
            {
                "question": "Structured Analysis and Structured Design (SA/SD) organizes software systems primarily based on:",
                "options": ["Objects and class hierarchies", "Functions and data flow transformations", "Hardware network nodes", "Database foreign keys only"],
                "correct": 1,
                "explanation": "SA/SD uses functional decomposition to break systems into functions and data streams (DFDs and structure charts)."
            },
            {
                "question": "Which CASE tool capability is provided by Git?",
                "options": ["Automatic UI layout generation", "Software Configuration Management & Version Control", "UML Diagram compiler", "SQL Database indexing"],
                "correct": 1,
                "explanation": "Git is a distributed Version Control and Configuration Management tool tracking source code revisions."
            }
        ],
        "viva_questions": [
            {
                "q": "What is the difference between Verification and Validation?",
                "a": "Verification asks 'Are we building the product right?' (reviews, walkthroughs, static checks). Validation asks 'Are we building the right product?' (testing dynamic software against actual user requirements)."
            },
            {
                "q": "Why is the Waterfall model rarely used for modern commercial software?",
                "a": "Because real-world user requirements change rapidly during development. Waterfall does not accommodate changes easily, and working software is only available at the very end."
            },
            {
                "q": "What is meant by Functional Decomposition?",
                "a": "The process of taking a complex high-level system and breaking it down into smaller, self-contained functional sub-routines until each module performs a single atomic task."
            },
            {
                "q": "Explain the difference between a Class and an Object with an example.",
                "a": "A Class is a blueprint (e.g., `Car` defining attributes `color`, `speed`). An Object is a specific physical instance created from that blueprint (e.g., `my_car = Car(color='Red', speed=120)`)."
            },
            {
                "q": "What is a CASE tool? Give two examples.",
                "a": "Computer-Aided Software Engineering (CASE) tools automate software lifecycle tasks. Examples: Draw.io / Visual Paradigm (for UML/DFD design), and Git/GitHub (for configuration management)."
            }
        ],
        "checklist": [
            "Studied core SDLC stages and lifecycle comparisons",
            "Understood Function-Oriented vs Object-Oriented design paradigms",
            "Inspected CASE tools and version control fundamentals",
            "Executed the OOP Python demonstration code",
            "Completed the 5-question Self-Assessment Quiz with score recorded"
        ]
    },
    {
        "id": 2,
        "code": "RTU-SE-02",
        "title": "Develop Software Requirements Specification (SRS) using IEEE Template",
        "category": "Requirements Engineering",
        "duration": "3 Hours",
        "difficulty": "Intermediate",
        "short_desc": "Master IEEE 830 standard specifications, classify Functional vs Non-Functional requirements, and generate a downloadable, professionally formatted SRS document.",
        "learning_objectives": [
            "Understand the structure and importance of an SRS document per IEEE Std 830-1998.",
            "Distinguish between Functional Requirements (FR) and Non-Functional Requirements (NFR).",
            "Write clear, unambiguous, verifiable, and traceable requirement statements using 'shall' syntax.",
            "Specify external interface, hardware, software, and operational constraints.",
            "Use the interactive SRS builder to add, edit, validate, and export an official PDF specification."
        ],
        "theory_sections": [
            {
                "heading": "1. What is an SRS & Why is it Critical?",
                "content": """
A **Software Requirements Specification (SRS)** is a formal agreement between the client and the development team describing *what* the system will do without specifying *how* it will be implemented internally.

### Key Characteristics of a Great SRS (IEEE 830):
* **Correct:** Every requirement reflects a real user need.
* **Unambiguous:** Every statement has exactly one interpretation (avoids words like 'fast', 'user-friendly', 'optimal').
* **Complete:** Covers all operational modes, inputs, outputs, error conditions, and constraints.
* **Consistent:** No two requirements contradict each other.
* **Verifiable:** There exists a finite, practical test method to prove compliance.
* **Traceable:** Each requirement has a unique identifier (e.g., `FR-01`, `NFR-01`) that maps to design and test cases.
"""
            },
            {
                "heading": "2. Standard IEEE 830 SRS Document Outline",
                "content": """
```
1. INTRODUCTION
   1.1 Purpose
   1.2 Scope
   1.3 Definitions, Acronyms, and Abbreviations
   1.4 References
   1.5 Overview
2. OVERALL DESCRIPTION
   2.1 Product Perspective
   2.2 Product Functions
   2.3 User Characteristics
   2.4 General Constraints
   2.5 Assumptions and Dependencies
3. SPECIFIC REQUIREMENTS
   3.1 External Interface Requirements (UI, Hardware, Software, Comm)
   3.2 Functional Requirements (FR-01, FR-02, ...)
   3.3 Non-Functional Requirements (Performance, Security, Reliability)
   3.4 Design Constraints
```
"""
            },
            {
                "heading": "3. Functional vs. Non-Functional Requirements",
                "content": """
### Functional Requirements (FR):
Define specific behaviors, computations, data manipulation, and functions that the software must perform.
* *FR-01:* The system shall allow students to register using a unique Roll Number and Email.
* *FR-02:* The system shall compile and execute C source code against user-specified test inputs within 10 seconds.
* *FR-03:* The system shall generate a visual Requirements Traceability Matrix linking requirements to test outcomes.

### Non-Functional Requirements (NFR):
Specify quality attributes, performance benchmarks, and environmental constraints.
* *NFR-01 (Performance):* The server shall respond to page navigation requests within 500 milliseconds under a load of 50 concurrent students.
* *NFR-02 (Security):* Student passwords shall be hashed using SHA-256 before storing in the SQLite database.
* *NFR-03 (Availability):* The virtual lab shall maintain 99.5% uptime during university operating hours.
"""
            }
        ],
        "procedure": [
            "Open the Interactive SRS Builder workspace.",
            "Fill out the Project Title, Purpose, and Scope for the LabPilot Virtual Lab.",
            "Define at least 4 Functional Requirements using standard IEEE 'The system shall...' modal phrasing.",
            "Define at least 2 measurable Non-Functional Requirements (performance time, security, or usability metric).",
            "Specify Hardware (CPU, RAM) and Software (Python 3, Modern Browser, GCC) environment constraints.",
            "Run the automated Quality & Ambiguity validation checker.",
            "Save the document to the SQLite database and export the official IEEE SRS PDF."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Define Project Scope & Purpose",
                "instruction": "Specify the title and high-level purpose of the Software Engineering Virtual Lab.",
                "example": "Title: LabPilot AI; Purpose: To provide interactive online practicals for RTU 3rd Semester SE students.",
                "expected_output": "Section 1.1 Purpose and 1.2 Scope drafted."
            },
            {
                "step_num": 2,
                "title": "Formulate User Authentication Functional Requirements",
                "instruction": "Add functional requirements covering student registration, role validation, and session login.",
                "example": "FR-01: The system shall authenticate student credentials against stored records.",
                "expected_output": "Requirement added with ID FR-01 and Must-Have priority."
            },
            {
                "step_num": 3,
                "title": "Formulate Experiment & Code Execution Requirements",
                "instruction": "Add functional requirements specifying the code runner, diagram editor, and progress tracker.",
                "example": "FR-02: The system shall compile student C code and execute boundary test cases.",
                "expected_output": "FR-02 and FR-03 saved in specification table."
            },
            {
                "step_num": 4,
                "title": "Formulate Measurable Non-Functional Requirements",
                "instruction": "Add performance and security criteria with measurable numbers (e.g. milliseconds, encryption type).",
                "example": "NFR-01: The system shall execute test cases and return outputs within 3 seconds.",
                "expected_output": "Measurable non-functional requirements entered."
            },
            {
                "step_num": 5,
                "title": "Set Operating & Hardware Constraints",
                "instruction": "Define client browser requirements, minimum RAM, and operating system compatibility.",
                "example": "Hardware: 2GB RAM minimum; Software: Windows 10/11, Python 3.10+, Chrome/Firefox.",
                "expected_output": "Environment prerequisites documented."
            },
            {
                "step_num": 6,
                "title": "Run Automated Ambiguity Checker",
                "instruction": "Click 'Validate Ambiguity' to ensure no vague terms like 'fast' or 'user-friendly' are present.",
                "example": "The rule checker verifies that all requirements contain verifiable metric thresholds.",
                "expected_output": "Ambiguity report with Quality Score >= 85%."
            },
            {
                "step_num": 7,
                "title": "Export IEEE Formatted PDF Document",
                "instruction": "Click 'Export Official PDF' to generate and download the complete SRS file via ReportLab.",
                "example": "Download file: `LabPilot_AI_SRS_Document.pdf`.",
                "expected_output": "Clean multi-page IEEE formatted PDF downloaded to student machine."
            },
            {
                "step_num": 8,
                "title": "Attempt Quiz and Finalize Submission",
                "instruction": "Answer the assessment quiz and mark Experiment 2 complete.",
                "example": "Review quiz questions on IEEE 830 standards and submit.",
                "expected_output": "Experiment 2 marked as COMPLETED."
            }
        ],
        "worked_example": {
            "title": "Sample IEEE 830 Requirements Table for LabPilot",
            "content": """
| ID | Requirement Statement | Category | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **FR-01** | The system shall allow students to sign in using their unique university Roll Number. | Functional | Must-Have | Verified against SQLite `users` table. |
| **FR-02** | The system shall provide an interactive text-to-UML canvas rendering SVG diagrams. | Functional | Must-Have | Mermaid.js renders valid SVG within 500ms. |
| **FR-03** | The system shall compile C code via MinGW GCC and execute test cases with `stdin` pipes. | Functional | Must-Have | Execution times out after 10 seconds maximum. |
| **NFR-01** | The system shall render all laboratory experiment pages in less than 400 milliseconds. | Performance | Should-Have | Measured on standard localhost browser. |
| **NFR-02** | All student diagram submissions and progress states shall be persisted in SQLite. | Reliability | Must-Have | Zero data loss across server restarts. |
"""
        },
        "quiz": [
            {
                "question": "Which organization publishes the recognized standard 830 for Software Requirements Specifications?",
                "options": ["ISO", "IEEE", "ACM", "W3C"],
                "correct": 1,
                "explanation": "IEEE Std 830-1998 is the IEEE Recommended Practice for Software Requirements Specifications."
            },
            {
                "question": "Which of the following is considered an UNACCEPTABLE requirement statement in an SRS?",
                "options": [
                    "The system shall respond to database queries within 250 milliseconds.",
                    "The user interface should be very user-friendly and aesthetically pleasing.",
                    "The system shall accept passwords containing at least 8 characters.",
                    "The backup process shall execute daily at 02:00 AM UTC."
                ],
                "correct": 1,
                "explanation": "'User-friendly and aesthetically pleasing' is completely subjective, non-measurable, and cannot be scientifically tested."
            },
            {
                "question": "What is the primary difference between Functional and Non-Functional requirements?",
                "options": [
                    "FR specifies system behaviors/services; NFR specifies quality attributes/constraints.",
                    "FR is written by programmers; NFR is written by users.",
                    "FR is optional; NFR is always mandatory.",
                    "FR covers hardware; NFR covers software only."
                ],
                "correct": 0,
                "explanation": "Functional requirements define what the system does, while Non-Functional requirements define how well it performs (security, speed, reliability)."
            },
            {
                "question": "What standard modal verb is mandated by IEEE standards to indicate a mandatory requirement?",
                "options": ["May", "Might", "Shall", "Could"],
                "correct": 2,
                "explanation": "In IEEE and ISO standards, 'SHALL' denotes a mandatory requirement, whereas 'SHOULD' denotes a recommendation."
            },
            {
                "question": "Requirements traceability ensures that:",
                "options": [
                    "All code has author comments.",
                    "Every requirement can be tracked forward to design and testing, and backward to its business origin.",
                    "The software can be tracked via GPS.",
                    "Git commits happen every hour."
                ],
                "correct": 1,
                "explanation": "Traceability links each requirement ID to its design elements, source code modules, and test cases."
            }
        ],
        "viva_questions": [
            {
                "q": "What is IEEE 830?",
                "a": "IEEE 830 is the internationally accepted standard guideline that defines the format, content, and quality qualities for writing a Software Requirements Specification (SRS)."
            },
            {
                "q": "Why is it dangerous to write ambiguous requirements in an SRS?",
                "a": "Ambiguity causes developers to build what they assume rather than what the user wanted, resulting in expensive rework, failed acceptance tests, and budget overruns."
            },
            {
                "q": "What is the difference between a User Requirement and a System Requirement?",
                "a": "User requirements are high-level statements in plain language for clients. System requirements are detailed technical specifications describing system services and operational constraints for developers."
            },
            {
                "q": "Give two examples of Non-Functional Requirements.",
                "a": "1. Performance: 'Page load time must be under 1 second'. 2. Security: 'All sensitive data must be encrypted with AES-256 at rest'."
            },
            {
                "q": "What is a Requirement Traceability Matrix (RTM)?",
                "a": "A grid table that maps user requirements to test cases to guarantee that every requirement has at least one test case verifying it (ensuring 100% test coverage)."
            }
        ],
        "checklist": [
            "Studied IEEE 830 structure and core requirement quality factors",
            "Formulated at least 4 Functional Requirements using 'shall' phrasing",
            "Formulated at least 2 measurable Non-Functional Requirements",
            "Executed the automated ambiguity and quality checker",
            "Exported and saved the official SRS PDF document"
        ]
    },
    {
        "id": 3,
        "code": "RTU-SE-03",
        "title": "Develop Data Flow Diagram (DFD) Model (Level 0, Level 1 and Data Dictionary)",
        "category": "Data Flow Modeling",
        "duration": "3 Hours",
        "difficulty": "Intermediate",
        "short_desc": "Design Level 0 Context DFDs, decompose into Level 1 functional processes with Data Stores, compile a formal Data Dictionary, and export diagrams.",
        "learning_objectives": [
            "Understand Data Flow Diagrams (DFDs) and standard symbols (Yourdon & DeMarco / Gane & Sarson).",
            "Model a Level 0 Context Diagram identifying external entities, main system boundary, and I/O data flows.",
            "Decompose the context process into a balanced Level 1 DFD with numbered sub-processes and data stores.",
            "Learn DFD rules: Black holes, Miracles, Grey holes, and direct entity-to-store prohibitions.",
            "Construct a comprehensive Data Dictionary specifying data items, types, lengths, and descriptions.",
            "Use the interactive visual DFD canvas to render, modify, and save diagrams."
        ],
        "theory_sections": [
            {
                "heading": "1. What is a DFD & Why is it Used?",
                "content": """
A **Data Flow Diagram (DFD)** is a graphical representation of the flow of data through an information system. It models process transformations, external data origins/destinations, and data storage points without depicting sequential control logic (like loops or conditional jumps).

### Standard DFD Elements (Gane & Sarson / Yourdon):
1. **External Entity (Terminator):** Source or destination of data outside the system boundary (represented as a Rectangle).
2. **Process:** An operation that transforms incoming data into outgoing data (represented as a Rounded Rectangle or Circle).
3. **Data Flow:** Directed arrow depicting data packets moving between entities, processes, and stores.
4. **Data Store:** Repository where data is stored at rest (represented as Open-ended parallel lines or Cylinder).
"""
            },
            {
                "heading": "2. DFD Hierarchy (Decomposition)",
                "content": """
* **Level 0 DFD (Context Diagram):** High-level view showing the entire system as a single central process connected to external entities. Establishes the project scope and system boundaries.
* **Level 1 DFD:** Breaks down the central Level 0 process into major high-level sub-processes (1.0, 2.0, 3.0), showing how data moves into data stores (D1, D2).
* **Level 2 DFD:** Further decomposes a single Level 1 process into detailed sub-tasks (e.g., process 2.1, 2.2, 2.3).
* **Balancing Rule:** All input and output data flows that enter or exit the system in Level 0 *must* appear entering or exiting in Level 1.
"""
            },
            {
                "heading": "3. Critical DFD Rules & Errors to Avoid",
                "content": """
1. **No Entity-to-Entity Flow:** An external entity cannot directly send data to another external entity within the DFD (must go through a process).
2. **No Entity-to-Data Store Flow:** An external entity cannot directly read from or write to a data store without an intermediate process.
3. **No Store-to-Store Flow:** Data cannot move between two data stores without a process managing the transfer.
4. **Black Hole Error:** A process with input flows but no output flows.
5. **Miracle Error:** A process with output flows but no input flows.
6. **Grey Hole Error:** A process whose outputs cannot realistically be generated from its inputs.
"""
            }
        ],
        "procedure": [
            "Identify the external entities interacting with the LabPilot virtual lab (Student, Teacher, External Compiler).",
            "Construct the Level 0 Context Diagram depicting the single 'LabPilot AI System' process and primary data flows.",
            "Decompose the context process into 4 Level 1 functional processes: 1.0 Authentication, 2.0 SRS Management, 3.0 Test Execution, and 4.0 Progress Management.",
            "Connect processes to 4 corresponding data stores: D1 Users, D2 SRS Documents, D3 Test Suites, and D4 Progress Database.",
            "Construct a complete Data Dictionary table specifying key data elements.",
            "Verify DFD balancing and export the diagrams as PNG/SVG."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Identify External Entities & Data Flows",
                "instruction": "Identify who sends data to LabPilot and who receives reports.",
                "example": "Student sends login credentials and lab submissions; Teacher sends experiment assignments and grades.",
                "expected_output": "Entities: Student, Teacher; Flows: Credentials, Submissions, Evaluation."
            },
            {
                "step_num": 2,
                "title": "Draft Level 0 Context Diagram",
                "instruction": "Render the Level 0 diagram using the interactive Mermaid/Canvas studio.",
                "example": "Central process: `(LabPilot System)` connected via bidirectional arrows to `[Student]` and `[Teacher]`.",
                "expected_output": "Valid Level 0 context diagram rendered."
            },
            {
                "step_num": 3,
                "title": "Perform Level 1 Functional Decomposition",
                "instruction": "Decompose the single system process into 4 logical sub-processes with proper numbering (1.0 to 4.0).",
                "example": "1.0 Auth, 2.0 SRS Engine, 3.0 Code Runner, 4.0 Assessment Tracker.",
                "expected_output": "Processes 1.0, 2.0, 3.0, 4.0 configured."
            },
            {
                "step_num": 4,
                "title": "Integrate Data Stores (D1 to D4)",
                "instruction": "Connect processes to persistent repositories where data is saved.",
                "example": "D1 User DB, D2 SRS Specs, D3 Test Results, D4 Student Progress.",
                "expected_output": "Data stores mapped with read/write arrow flows."
            },
            {
                "step_num": 5,
                "title": "Verify DFD Consistency & Balancing",
                "instruction": "Ensure no black holes, miracles, or direct entity-to-store connections exist.",
                "example": "Validate that all inputs from Level 0 are accounted for in Level 1.",
                "expected_output": "Zero DFD violations detected."
            },
            {
                "step_num": 6,
                "title": "Compile the Data Dictionary Table",
                "instruction": "Define names, data types, descriptions, and formats for primary data elements.",
                "example": "Student_ID (Integer), Source_Code (Text), Test_Status (Enum: PASS/FAIL).",
                "expected_output": "Structured Data Dictionary table completed."
            },
            {
                "step_num": 7,
                "title": "Save Diagrams and Data Dictionary",
                "instruction": "Save the completed diagrams into SQLite and export diagram images.",
                "example": "Click 'Save Diagrams' to persist Level 0 and Level 1 definitions.",
                "expected_output": "Diagram data persisted in `saved_diagrams` table."
            },
            {
                "step_num": 8,
                "title": "Take DFD Quiz & Complete Practical",
                "instruction": "Attempt the self-assessment quiz on DFD rules and submit.",
                "example": "Complete the 5 multiple choice questions.",
                "expected_output": "Experiment 3 marked COMPLETED."
            }
        ],
        "worked_example": {
            "title": "LabPilot DFD Level 0 & Level 1 Architecture",
            "content": """
### Level 0 Context Diagram (Mermaid Syntax):
```mermaid
graph LR
    Student["External Entity: Student"]
    Teacher["External Entity: Teacher"]
    System(("0.0 LabPilot Virtual Lab System"))

    Student -->|1. Login Credentials| System
    Student -->|2. SRS & UML Data| System
    Student -->|3. Test Code & Inputs| System
    System -->|4. Test Results & Hints| Student
    System -->|5. Progress Dashboard| Student

    Teacher -->|6. Assignment Rubrics| System
    System -->|7. Student Submissions| Teacher
    Teacher -->|8. Grades & Feedback| System
```

### Level 1 DFD Architecture:
* **Process 1.0: User Authentication** (Interacts with `D1: Users DB`)
* **Process 2.0: SRS & UML Workspace** (Interacts with `D2: Specs & Diagrams DB`)
* **Process 3.0: Testing & Code Execution** (Interacts with `D3: Test Suites DB`)
* **Process 4.0: Progress & Grading** (Interacts with `D4: Submissions DB`)
"""
        },
        "quiz": [
            {
                "question": "What is the primary purpose of a Level 0 DFD (Context Diagram)?",
                "options": [
                    "To show detailed class methods and variables.",
                    "To show the entire system as a single process and establish project boundaries with external entities.",
                    "To display the database schema normalization.",
                    "To measure code execution speed."
                ],
                "correct": 1,
                "explanation": "A Context Diagram (Level 0) represents the entire system as one bubble, defining the scope and data interactions with external entities."
            },
            {
                "question": "In a DFD, what is a 'Black Hole' error?",
                "options": [
                    "A process with inputs but no outputs.",
                    "A process with outputs but no inputs.",
                    "A database crash.",
                    "A missing foreign key."
                ],
                "correct": 0,
                "explanation": "A Black Hole is an illegal process that absorbs incoming data flows but produces no output data flows."
            },
            {
                "question": "Can an External Entity directly read from or write to a Data Store in a DFD?",
                "options": [
                    "Yes, if the entity has admin privileges.",
                    "No, all data moving between entities and stores must pass through an intermediate process.",
                    "Yes, during Level 2 DFDs only.",
                    "Only in agile development."
                ],
                "correct": 1,
                "explanation": "In standard DFD rules, data stores cannot connect directly to external entities; a process must mediate the read/write action."
            },
            {
                "question": "What is the 'Balancing Rule' between Level 0 and Level 1 DFDs?",
                "options": [
                    "Number of processes must equal number of entities.",
                    "All inputs and outputs across the system boundary in Level 0 must be conserved in Level 1.",
                    "Every process must have exactly two outputs.",
                    "Data stores must have equal storage capacity."
                ],
                "correct": 1,
                "explanation": "Balancing ensures that all data flows entering or leaving the system boundary at a parent level remain consistent at the child level."
            },
            {
                "question": "What is a Data Dictionary?",
                "options": [
                    "An English language dictionary for developers.",
                    "A centralized repository detailing metadata, data types, formats, and definitions of all DFD data flows and stores.",
                    "A Python dictionary object.",
                    "A list of database table passwords."
                ],
                "correct": 1,
                "explanation": "A Data Dictionary is a structured reference describing the meaning, relationships, origin, type, and size of every data item in the system."
            }
        ],
        "viva_questions": [
            {
                "q": "What are the four basic symbols used in a Data Flow Diagram?",
                "a": "1. External Entity (Rectangle), 2. Process (Rounded Rectangle/Circle), 3. Data Flow (Directed Arrow), 4. Data Store (Open-ended rectangle/parallel lines)."
            },
            {
                "q": "What is the difference between a DFD and a Flowchart?",
                "a": "A Flowchart shows sequential control flow, decision branches, and execution order. A DFD shows data flow and transformations without indicating timing, loops, or control sequence."
            },
            {
                "q": "What is a Miracle process in a DFD?",
                "a": "A process that generates output data flows spontaneously without any incoming data flows to produce them."
            },
            {
                "q": "What is meant by Level 1 DFD decomposition?",
                "a": "Decomposing the single central process of Level 0 into 3 to 7 primary functional sub-processes, identifying major data stores and internal data flows."
            },
            {
                "q": "What information does a Data Dictionary entry contain?",
                "a": "Data Name, Alias (if any), Data Type (e.g., String, Integer), Length/Format, Valid Values/Range, and Description of purpose."
            }
        ],
        "checklist": [
            "Studied DFD standard notations, rules, and common errors",
            "Created Level 0 Context Diagram for LabPilot AI",
            "Decomposed system into Level 1 DFD with 4 processes and 4 data stores",
            "Compiled a complete Data Dictionary table",
            "Verified diagram balancing and completed assessment quiz"
        ]
    },
    {
        "id": 4,
        "code": "RTU-SE-04",
        "title": "Develop Structured Design for the DFD Model Developed",
        "category": "Architectural Design",
        "duration": "2 Hours",
        "difficulty": "Intermediate",
        "short_desc": "Transform DFD processes into software modules via Structure Charts, evaluate Module Cohesion and Coupling, and apply Top-Down design principles.",
        "learning_objectives": [
            "Understand Structured Design and the transition from analysis (DFD) to architectural design.",
            "Learn how to construct Structure Charts showing module hierarchy, calling relationships, and data/control couples.",
            "Understand Module Cohesion types (from Coincidental to Functional Cohesion).",
            "Understand Module Coupling types (from Content to Data Coupling).",
            "Apply Transform Analysis and Transaction Analysis to map DFDs into software modules.",
            "Design, edit, and export an interactive Structure Chart for the LabPilot system."
        ],
        "theory_sections": [
            {
                "heading": "1. What is Structured Design & Structure Charts?",
                "content": """
**Structured Design** is a systematic approach to software architecture that converts a Data Flow Diagram (DFD) into a hierarchy of software modules represented as a **Structure Chart**.

### Structure Chart Elements:
1. **Module:** A contiguous block of code (function, procedure, class method) performing a specific task (represented as a Rectangle).
2. **Call Relationship:** An arrow from parent module to child module indicating invocation.
3. **Data Couple:** An arrow with an open circle representing data parameters passed between modules.
4. **Control Couple (Flag):** An arrow with a solid circle representing status flags or boolean control switches (e.g., `is_valid`, `eof`).
"""
            },
            {
                "heading": "2. Cohesion: Aim for HIGH Cohesion",
                "content": """
**Cohesion** measures how closely related and focused the responsibilities of a single module are. 
*Rule of Thumb: High Cohesion is Desirable.*

### Levels of Cohesion (Worst to Best):
1. **Coincidental (Worst):** Module tasks have no meaningful relationship (e.g., `do_random_things()`).
2. **Logical:** Module performs a set of logically categorized tasks selected by a flag (e.g., `print_all(report_type)`).
3. **Temporal:** Module tasks are grouped because they occur at the same time (e.g., `startup_initialization()`).
4. **Procedural:** Tasks must be executed in a specific sequential order.
5. **Communicational:** Tasks operate on the same input or output data structure.
6. **Sequential:** Output of one task is input to the next within the module.
7. **Functional (Best):** Module performs exactly ONE single, well-defined mathematical or logical task (e.g., `calculate_triangle_area()`, `hash_password()`).
"""
            },
            {
                "heading": "3. Coupling: Aim for LOW Coupling",
                "content": """
**Coupling** measures the degree of interdependence between two software modules.
*Rule of Thumb: Low (Loose) Coupling is Desirable.*

### Levels of Coupling (Worst to Best):
1. **Content (Worst):** One module directly modifies or accesses internal data of another module.
2. **Common:** Multiple modules share read/write access to global variables.
3. **Control:** One module passes a control flag to dictate the internal logical branching of another.
4. **Stamp:** Modules share a complex composite data structure (like an entire record) when only a single field is needed.
5. **Data (Best):** Modules communicate strictly by passing primitive, minimal data parameters (e.g., `add(a, b)`).
"""
            }
        ],
        "procedure": [
            "Take the 4 processes from Experiment 3's Level 1 DFD.",
            "Identify the Root (Executive) module: 'LabPilot Controller'.",
            "Decompose into intermediate managers: Auth Manager, Experiment Manager, Test Runner Manager, and Progress Evaluator.",
            "Decompose each manager into atomic leaf modules with functional cohesion (e.g., `validate_credentials`, `compile_c_code`, `compare_output`).",
            "Define data couples and control flags passed between parent and child modules.",
            "Construct and save the Structure Chart in the interactive workspace."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Analyze Level 1 DFD for Transform Centering",
                "instruction": "Review the DFD and identify input branch (afferent), central transform, and output branch (efferent).",
                "example": "Afferent: Read input code; Transform: Compile and evaluate; Efferent: Display results matrix.",
                "expected_output": "Central transformation identified."
            },
            {
                "step_num": 2,
                "title": "Define Top-Level Controller Module",
                "instruction": "Create the root module 'LabPilot Main Controller' responsible for orchestrating sub-modules.",
                "example": "Root module dispatches actions based on student navigation.",
                "expected_output": "Root module created on canvas."
            },
            {
                "step_num": 3,
                "title": "Add Second-Level Subsystem Modules",
                "instruction": "Attach child modules for Authentication, SRS Builder, Code Execution, and Gradebook.",
                "example": "Four main subsystems linked to Root Controller.",
                "expected_output": "Four branch nodes connected."
            },
            {
                "step_num": 4,
                "title": "Decompose into Atomic Worker Modules",
                "instruction": "Create leaf worker functions having Functional Cohesion.",
                "example": "`hash_password()`, `check_ambiguity()`, `invoke_gcc()`, `diff_output()`.",
                "expected_output": "Hierarchical tree with functional leaf nodes."
            },
            {
                "step_num": 5,
                "title": "Annotate Data & Control Couples",
                "instruction": "Identify parameters passed down and status flags returned back.",
                "example": "Pass `source_code` (data); return `compilation_status` (control flag).",
                "expected_output": "Data and control couples documented."
            },
            {
                "step_num": 6,
                "title": "Evaluate Cohesion & Coupling Metrics",
                "instruction": "Verify that all leaf modules exhibit Functional Cohesion and Data Coupling.",
                "example": "Check that no global variables are modified across module boundaries.",
                "expected_output": "Clean low-coupling architectural assessment."
            },
            {
                "step_num": 7,
                "title": "Save Structure Chart Diagram",
                "instruction": "Save the diagram to SQLite and export image format.",
                "example": "Persist structure chart record.",
                "expected_output": "Diagram saved in `saved_diagrams`."
            },
            {
                "step_num": 8,
                "title": "Take Structured Design Quiz",
                "instruction": "Complete assessment quiz testing cohesion, coupling, and structure charts.",
                "example": "Submit quiz responses.",
                "expected_output": "Experiment 4 marked COMPLETED."
            }
        ],
        "worked_example": {
            "title": "Structure Chart Hierarchy for LabPilot AI",
            "content": """
### Structure Chart Representation (Mermaid Tree):
```mermaid
graph TD
    Root["0.0 LabPilot Main Controller"]

    Root --> M1["1.0 Auth Controller"]
    Root --> M2["2.0 SRS Controller"]
    Root --> M3["3.0 Test Execution Controller"]
    Root --> M4["4.0 Progress Controller"]

    M1 --> M11["1.1 read_credentials()"]
    M1 --> M12["1.2 verify_password_hash()"]
    M1 --> M13["1.3 issue_session_cookie()"]

    M2 --> M21["2.1 parse_requirements()"]
    M2 --> M22["2.2 check_ieee_ambiguities()"]
    M2 --> M23["2.3 save_srs_to_db()"]

    M3 --> M31["3.1 write_temp_c_file()"]
    M3 --> M32["3.2 invoke_gcc_compiler()"]
    M3 --> M33["3.3 execute_with_stdin()"]
    M3 --> M34["3.4 compare_actual_vs_expected()"]

    M4 --> M41["4.1 calculate_module_score()"]
    M4 --> M42["4.2 update_progress_record()"]
```
"""
        },
        "quiz": [
            {
                "question": "Which of the following represents the most desirable level of Module Cohesion?",
                "options": ["Coincidental Cohesion", "Temporal Cohesion", "Functional Cohesion", "Logical Cohesion"],
                "correct": 2,
                "explanation": "Functional Cohesion is the highest and best level, where every element in the module contributes to executing a single, well-defined task."
            },
            {
                "question": "Which form of Module Coupling is considered the worst and most dangerous in software design?",
                "options": ["Data Coupling", "Stamp Coupling", "Content Coupling", "Control Coupling"],
                "correct": 2,
                "explanation": "Content Coupling occurs when one module directly accesses or alters the internal data or instructions of another, completely breaking encapsulation."
            },
            {
                "question": "What is the primary visual difference between a Data Couple and a Control Couple in a Structure Chart?",
                "options": [
                    "Data couple has an open circle; control couple has a filled (solid) circle.",
                    "Data couple is a dashed line; control couple is solid.",
                    "Data couple is red; control couple is blue.",
                    "They are identical."
                ],
                "correct": 0,
                "explanation": "Standard structured design notation uses an arrow with an open circle for data and a filled circle for a control flag."
            },
            {
                "question": "In software architecture, what is the golden rule regarding Cohesion and Coupling?",
                "options": [
                    "High Cohesion and High Coupling",
                    "Low Cohesion and Low Coupling",
                    "High Cohesion and Low Coupling",
                    "Low Cohesion and High Coupling"
                ],
                "correct": 2,
                "explanation": "High Cohesion (focused modules) and Low Coupling (minimal interdependence) create maintainable, testable, and reusable software."
            },
            {
                "question": "Transform Analysis in Structured Design is used to:",
                "options": [
                    "Convert DFD data flow networks into balanced Structure Charts.",
                    "Translate Python code to C.",
                    "Normalize relational databases.",
                    "Draw wireframe mockups."
                ],
                "correct": 0,
                "explanation": "Transform Analysis identifies the central processing stream of a DFD and maps it into a top-down module invocation hierarchy."
            }
        ],
        "viva_questions": [
            {
                "q": "What is a Structure Chart?",
                "a": "A graphic design tool that represents the hierarchical organization, calling sequences, and parameter data/control interfaces of software modules."
            },
            {
                "q": "Define Cohesion and give an example of Functional Cohesion.",
                "a": "Cohesion is the internal strength of a module. Functional Cohesion occurs when a module performs a single task, like `math.sqrt(x)` or `compute_checksum()`."
            },
            {
                "q": "Define Coupling and give an example of Data Coupling.",
                "a": "Coupling measures the degree of dependency between two modules. Data Coupling occurs when modules share only primitive parameters, such as passing two integers to `int add(int a, int b)`."
            },
            {
                "q": "What is the difference between a DFD and a Structure Chart?",
                "a": "A DFD models how data flows through system transformations (Analysis). A Structure Chart models how software routines invoke one another and pass parameters (Design)."
            },
            {
                "q": "Why is Stamp Coupling inferior to Data Coupling?",
                "a": "In Stamp Coupling, an entire data structure (e.g., student record with 20 fields) is passed to a function that only needs 1 field (e.g., `roll_no`), introducing unnecessary coupling."
            }
        ],
        "checklist": [
            "Studied Structured Design principles and Structure Chart notations",
            "Understood the 7 levels of Cohesion and 5 levels of Coupling",
            "Converted Level 1 DFD into hierarchical software modules",
            "Designed and saved the Structure Chart for LabPilot AI",
            "Completed the assessment quiz with score recorded"
        ]
    },
    {
        "id": 5,
        "code": "RTU-SE-05",
        "title": "Develop Structural UML Diagrams of the Given Project",
        "category": "Structural OOAD",
        "duration": "3 Hours",
        "difficulty": "Intermediate",
        "short_desc": "Design and render static architectural models: Class, Object, Component, Deployment, and Package diagrams using Mermaid.js vector studio.",
        "learning_objectives": [
            "Understand Unified Modeling Language (UML) structural (static) modeling.",
            "Design Class Diagrams with attributes, methods, visibility, and relationships (Inheritance, Association, Aggregation, Composition).",
            "Model Object Diagrams depicting runtime object states and values.",
            "Construct Component Diagrams showing high-level software modularity and interfaces.",
            "Create Deployment Diagrams illustrating physical runtime nodes (Client, Server, Database).",
            "Group related classes into Package Diagrams.",
            "Use the multi-tab interactive UML Studio to edit, render, and save diagrams."
        ],
        "theory_sections": [
            {
                "heading": "1. What are Structural UML Diagrams?",
                "content": """
**Structural UML Diagrams** depict the static architecture of a software system—representing elements that exist independently of time, such as classes, objects, interfaces, physical components, and hardware deployment nodes.

### The 5 Core Structural Diagrams in RTU Syllabus:
1. **Class Diagram:** Backbone of OOAD. Shows classes, attributes, operations, and relationships.
2. **Object Diagram:** Snapshot of the system at a specific runtime instant showing actual instance values.
3. **Component Diagram:** Illustrates software components (libraries, executables, database files) and their wiring.
4. **Deployment Diagram:** Models physical hardware nodes (laptops, cloud servers, databases) and network connections.
5. **Package Diagram:** Groups related classes or use cases into logical namespaces/folders for maintainability.
"""
            },
            {
                "heading": "2. Class Relationships Defined",
                "content": """
* **Association (Plain line):** Relationship between two classes where neither owns the other (e.g., `Student` *enrolls in* `Course`).
* **Inheritance / Generalization (Solid line with hollow triangle):** Is-a relationship (e.g., `Student` *is-a* `User`).
* **Aggregation (Solid line with hollow diamond):** Has-a relationship where child can exist independently of parent (e.g., `Department` *has* `Professors`).
* **Composition (Solid line with filled diamond):** Strong has-a relationship where child cannot exist without parent (e.g., `Experiment` *owns* `Step` objects).
* **Dependency (Dashed arrow):** One class depends on another's interface (e.g., `TestRunner` *uses* `GCCCompiler`).
"""
            }
        ],
        "procedure": [
            "Open the Structural UML Studio workspace.",
            "Select the Class Diagram tab and model core entities: User, Student, Teacher, Experiment, TestCase, Submission.",
            "Switch to the Object Diagram tab and instantiate objects with concrete student data.",
            "Switch to Component Diagram and model Frontend, Flask Server, SQLite, and GCC Worker.",
            "Switch to Deployment Diagram and model Student Browser, Localhost PC, and Storage.",
            "Switch to Package Diagram and organize classes into Auth, CoreLab, and Engine packages.",
            "Save all 5 structural diagrams to the database."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Model Core Class Diagram",
                "instruction": "Define class attributes (with `+` public, `-` private, `#` protected) and methods in Mermaid syntax.",
                "example": "`class Student { +string roll_no; +submit_lab() }`",
                "expected_output": "Rendered Class Diagram with inheritance and associations."
            },
            {
                "step_num": 2,
                "title": "Model Instance Object Diagram",
                "instruction": "Create an object snapshot showing `rahul : Student` with `roll_no = '22EBKCS042'`.",
                "example": "Instantiate `exp1 : Experiment` linked to `rahul`.",
                "expected_output": "Object Diagram showing runtime attribute values."
            },
            {
                "step_num": 3,
                "title": "Construct Component Diagram",
                "instruction": "Model software modules: Web UI, Flask API, GCC Wrapper, SQLite File.",
                "example": "Show `[Flask Backend]` dependent on `[SQLite Database]` and `[MinGW GCC]`.",
                "expected_output": "Component wiring diagram rendered."
            },
            {
                "step_num": 4,
                "title": "Construct Deployment Diagram",
                "instruction": "Model physical hardware deployment: Client Workstation running Browser connecting via HTTP to Localhost.",
                "example": "Node `<<Device>> Student PC` containing `<<Execution Environment>> Python 3.14`.",
                "expected_output": "Physical deployment topology rendered."
            },
            {
                "step_num": 5,
                "title": "Organize into Package Diagram",
                "instruction": "Group classes into logical packages: `Authentication`, `VirtualLabCore`, and `ExecutionEngine`.",
                "example": "Package `VirtualLabCore` imports `Authentication`.",
                "expected_output": "Package hierarchy rendered."
            },
            {
                "step_num": 6,
                "title": "Verify Multiplicity & Relationship Correctness",
                "instruction": "Check that multiplicities (e.g., `1` to `*`) and diamond arrowheads match OO design rules.",
                "example": "One `Student` can have `0..*` `Submissions`.",
                "expected_output": "Syntactically valid UML models."
            },
            {
                "step_num": 7,
                "title": "Save All Structural Diagrams",
                "instruction": "Click 'Save Structural UML' to persist diagram definitions in SQLite.",
                "example": "Saved records for all 5 diagrams.",
                "expected_output": "Diagram data stored in database."
            },
            {
                "step_num": 8,
                "title": "Take Structural UML Quiz",
                "instruction": "Attempt the quiz and mark Experiment 5 complete.",
                "example": "Complete questions on UML relationships.",
                "expected_output": "Experiment 5 marked COMPLETED."
            }
        ],
        "worked_example": {
            "title": "Complete Class Diagram Model for LabPilot AI",
            "content": """
```mermaid
classDiagram
    class User {
        +int id
        +string username
        +string name
        +string role
        +login()
        +logout()
    }

    class Student {
        +string roll_no
        +string semester
        +start_experiment(exp_id)
        +submit_quiz()
    }

    class Teacher {
        +string employee_id
        +grade_submission()
        +view_analytics()
    }

    class Experiment {
        +int id
        +string code
        +string title
        +list steps
        +load_workspace()
    }

    class Submission {
        +int id
        +datetime submitted_at
        +int score
        +save_result()
    }

    User <|-- Student : Inheritance
    User <|-- Teacher : Inheritance
    Student "1" --> "*" Submission : creates
    Experiment "1" --> "*" Submission : evaluated_in
```
"""
        },
        "quiz": [
            {
                "question": "Which relationship represents strong ownership where child objects are destroyed if the parent is destroyed?",
                "options": ["Aggregation", "Composition", "Generalization", "Association"],
                "correct": 1,
                "explanation": "Composition (represented by a filled black diamond) indicates strong lifecycle ownership where parts cannot exist without the whole."
            },
            {
                "question": "In a UML Class diagram, what visibility is indicated by the '-' symbol?",
                "options": ["Public", "Protected", "Private", "Package"],
                "correct": 2,
                "explanation": "UML visibility notations: `+` is Public, `-` is Private, `#` is Protected, and `~` is Package."
            },
            {
                "question": "What is the key difference between a Class Diagram and an Object Diagram?",
                "options": [
                    "Class diagram shows static templates; Object diagram shows a concrete snapshot of instances with runtime values.",
                    "Class diagram is behavioral; Object diagram is structural.",
                    "Object diagram has no attributes.",
                    "Class diagrams are only used for Java."
                ],
                "correct": 0,
                "explanation": "A Class diagram models the abstract blueprints, while an Object diagram captures specific objects and their state at a single moment in time."
            },
            {
                "question": "Which structural diagram models physical hardware nodes, network topologies, and execution environments?",
                "options": ["Component Diagram", "Deployment Diagram", "Package Diagram", "State Diagram"],
                "correct": 1,
                "explanation": "Deployment diagrams visualize the physical execution nodes (servers, devices, cloud instances) and artifact deployments."
            },
            {
                "question": "An open diamond at the end of a relationship line in UML denotes:",
                "options": ["Composition", "Aggregation", "Inheritance", "Realization"],
                "correct": 1,
                "explanation": "An open (hollow) diamond denotes Aggregation—a weak 'has-a' relationship where child parts can exist independently of the container."
            }
        ],
        "viva_questions": [
            {
                "q": "What is UML and who developed it?",
                "a": "Unified Modeling Language (UML) is a standardized visual modeling language in software engineering developed by Grady Booch, Ivar Jacobson, and James Rumbaugh (the 'Three Amigos')."
            },
            {
                "q": "What is the difference between Aggregation and Composition?",
                "a": "Aggregation is weak ownership (hollow diamond; e.g., Car and Driver—driver exists without car). Composition is strong ownership (filled diamond; e.g., Car and Engine—engine's lifecycle is bound to car)."
            },
            {
                "q": "What does a Component Diagram show?",
                "a": "It shows how software is split into replaceable components (e.g., DLLs, packages, services) and how they communicate via provided and required interfaces."
            },
            {
                "q": "What is a Deployment Diagram used for?",
                "a": "To visualize the physical hardware topology (servers, laptops, network connections) on which software artifacts run."
            },
            {
                "q": "What are Multiplicities in a Class Diagram?",
                "a": "They define the number of instances of one class that can relate to a single instance of another class (e.g., `1`, `0..1`, `1..*`, `*`)."
            }
        ],
        "checklist": [
            "Studied UML structural diagram types and notation standards",
            "Designed Class Diagram with inheritance and associations",
            "Modeled Object, Component, Deployment, and Package diagrams",
            "Persisted all structural models into the SQLite database",
            "Attempted the assessment quiz and verified viva answers"
        ]
    },
    {
        "id": 6,
        "code": "RTU-SE-06",
        "title": "Develop Behavioural UML Diagrams of the Given Project",
        "category": "Behavioural OOAD",
        "duration": "3 Hours",
        "difficulty": "Intermediate",
        "short_desc": "Model dynamic software behavior and message sequences: Use Case, Activity, Sequence, and State Machine diagrams with interactive vector visualization.",
        "learning_objectives": [
            "Understand dynamic modeling in UML representing system behavior over time.",
            "Design Use Case Diagrams with Actors, Use Cases, `<<include>>`, and `<<extend>>` relationships.",
            "Model workflow and business logic with Activity Diagrams (Forks, Joins, Decisions).",
            "Construct Sequence Diagrams depicting chronological message exchanges between participants.",
            "Design State Machine Diagrams tracking object lifecycle transitions and events.",
            "Use the multi-tab interactive editor to create, validate, and save all behavioural diagrams."
        ],
        "theory_sections": [
            {
                "heading": "1. What are Behavioural UML Diagrams?",
                "content": """
**Behavioural UML Diagrams** capture the dynamic behavior of a software system—how objects interact, exchange messages, transition between operational states, and respond to user events over time.

### The 4 Essential Behavioural Diagrams in RTU Syllabus:
1. **Use Case Diagram:** Defines system functional boundaries from an external user's perspective.
2. **Activity Diagram:** Models step-by-step procedural workflow, concurrency (fork/join), and decision paths (similar to an advanced flowchart).
3. **Sequence Diagram:** Shows objects interacting across chronological lifelines via message arrows.
4. **State Machine Diagram:** Models the discrete states an object passes through during its lifecycle in response to events.
"""
            },
            {
                "heading": "2. Use Case Relationships: <<include>> vs <<extend>>",
                "content": """
* **Actor:** Person, role, or external system interacting with the application (e.g., `Student`, `Teacher`).
* **Use Case:** A specific goal or service provided by the system (e.g., `Perform Experiment`).
* **`<<include>>` Relationship:** Mandatory sub-routine. The base use case *cannot* complete without executing the included use case (e.g., `Submit Experiment` *includes* `Verify Authentication`).
* **`<<extend>>` Relationship:** Optional or conditional behavior triggered under specific conditions (e.g., `Take Quiz` *extends* `Request Hint`).
"""
            },
            {
                "heading": "3. Sequence Diagram Components",
                "content": """
* **Lifeline (Vertical dashed line):** Represents the lifetime of an object/participant during the scenario.
* **Activation Box (Thin rectangle):** Indicates the period during which an object is actively executing a task.
* **Synchronous Message (Solid arrow with filled head):** Sender waits for receiver to finish before proceeding.
* **Asynchronous Message (Solid arrow with open head):** Sender continues without waiting.
* **Return Message (Dashed line with open arrow):** Returning control and data to the caller.
"""
            }
        ],
        "procedure": [
            "Open the Behavioural UML Studio workspace.",
            "Model the Use Case Diagram showing Student and Teacher actors with core lab features.",
            "Switch to the Activity Diagram tab and model the Student Login and Experiment Submission workflow.",
            "Switch to Sequence Diagram and trace the message flow: Student -> Browser -> Flask Server -> GCC -> Database.",
            "Switch to State Machine Diagram and model an Experiment lifecycle: Not Started -> In Progress -> Submitted -> Evaluated.",
            "Save all 4 behavioural diagrams to SQLite."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Model Use Case Diagram",
                "instruction": "Add actors `Student` and `Teacher` and connect them to use cases with system boundaries.",
                "example": "Student connects to `Register`, `Build SRS`, `Execute Test`, `View Score`.",
                "expected_output": "Use Case Diagram with system boundary rendered."
            },
            {
                "step_num": 2,
                "title": "Define <<include>> and <<extend>> Relations",
                "instruction": "Connect `Submit Practical` to `Verify Login` via `<<include>>`.",
                "example": "Show conditional `<<extend>>` for `Trigger Mistake DNA`.",
                "expected_output": "Properly stereotype-annotated use case relations."
            },
            {
                "step_num": 3,
                "title": "Model Activity Diagram Workflow",
                "instruction": "Create an activity diagram with Initial Node, Action states, Decision diamond, and Final Node.",
                "example": "Enter Code -> Compile -> Valid? Yes -> Run Tests; No -> Display Error.",
                "expected_output": "Complete workflow with decision logic."
            },
            {
                "step_num": 4,
                "title": "Construct Chronological Sequence Diagram",
                "instruction": "Model numbered messages between `Student`, `WebUI`, `FlaskServer`, `GCC`, and `Database`.",
                "example": "`Student->>WebUI: Click Run`, `WebUI->>Flask: POST /api/tests/run`.",
                "expected_output": "Sequence diagram with activation bars and return messages."
            },
            {
                "step_num": 5,
                "title": "Construct State Machine Diagram",
                "instruction": "Model states: `NOT_STARTED`, `IN_PROGRESS`, `QUIZ_ATTEMPTED`, `COMPLETED` with transition triggers.",
                "example": "`[*] -> NOT_STARTED -> (start_exp) -> IN_PROGRESS -> (submit) -> COMPLETED -> [*]`.",
                "expected_output": "State machine transition model rendered."
            },
            {
                "step_num": 6,
                "title": "Verify Synchronization & Concurrency",
                "instruction": "Check that Sequence Diagram message order is strictly top-to-bottom chronological.",
                "example": "Verify no time-travel inconsistencies exist in lifeline exchanges.",
                "expected_output": "Logically sound sequence model."
            },
            {
                "step_num": 7,
                "title": "Save All Behavioural Diagrams",
                "instruction": "Persist the 4 behavioural models into SQLite.",
                "example": "Click 'Save Behavioural UML' to save.",
                "expected_output": "Records persisted in `saved_diagrams`."
            },
            {
                "step_num": 8,
                "title": "Attempt Behavioural Quiz & Submit",
                "instruction": "Complete the assessment quiz and mark Experiment 6 complete.",
                "example": "Submit quiz responses.",
                "expected_output": "Experiment 6 marked COMPLETED."
            }
        ],
        "worked_example": {
            "title": "Complete Sequence Diagram Model for LabPilot AI",
            "content": """
```mermaid
sequenceDiagram
    autonumber
    actor Student
    participant WebUI as Virtual Lab Frontend
    participant Server as Flask Server
    participant GCC as MinGW GCC Compiler
    participant DB as SQLite Database

    Student->>WebUI: Click "Run Test Suite"
    WebUI->>Server: POST /api/tests/run (C code, test inputs)
    Server->>GCC: Compile solution.c
    alt Compilation Error
        GCC-->>Server: Error Output (Exit code != 0)
        Server-->>WebUI: Return Compilation Error
        WebUI-->>Student: Display Error in Red
    else Compilation Success
        GCC-->>Server: solution.exe generated
        Server->>Server: Pipe test inputs into stdin
        Server->>DB: Save test results & coverage
        DB-->>Server: Acknowledged
        Server-->>WebUI: JSON (PASS/FAIL, execution time ms)
        WebUI-->>Student: Display Results Matrix & Mistake DNA
    end
```
"""
        },
        "quiz": [
            {
                "question": "What is the difference between an <<include>> and an <<extend>> relationship in a Use Case Diagram?",
                "options": [
                    "<<include>> is mandatory; <<extend>> is optional and conditional.",
                    "<<include>> is optional; <<extend>> is mandatory.",
                    "<<include>> is for teachers; <<extend>> is for students.",
                    "They are identical terms in UML 2.5."
                ],
                "correct": 0,
                "explanation": "An `<<include>>` use case must always be executed as part of the base use case, whereas an `<<extend>>` use case is executed only under specific conditional circumstances."
            },
            {
                "question": "In a Sequence Diagram, what does the vertical dashed line descending from an object represent?",
                "options": ["Inheritance link", "Object Lifeline", "Database relationship", "Execution error"],
                "correct": 1,
                "explanation": "A Lifeline represents the duration of existence of a participant/object during the interaction."
            },
            {
                "question": "Which node in a UML Activity diagram is used to split a single control flow into two or more concurrent, parallel flows?",
                "options": ["Decision Node", "Fork Node", "Join Node", "Merge Node"],
                "correct": 1,
                "explanation": "A Fork node (thick horizontal/vertical bar) splits one incoming flow into multiple concurrent parallel flows."
            },
            {
                "question": "In a State Machine Diagram, what triggers a transition between two states?",
                "options": ["An Event (or signal) meeting an optional Guard Condition", "A CPU clock cycle", "A database query", "A UML class definition"],
                "correct": 0,
                "explanation": "State transitions are triggered by events (e.g., button click, timeout) evaluated against boolean guard conditions `[condition]`."
            },
            {
                "question": "Which behavioural diagram is best suited for modeling concurrent business workflows and decision branching?",
                "options": ["Sequence Diagram", "Activity Diagram", "Class Diagram", "Package Diagram"],
                "correct": 1,
                "explanation": "Activity diagrams are ideal for workflows, business processes, and algorithmic steps with decision nodes and parallel threads."
            }
        ],
        "viva_questions": [
            {
                "q": "What is the purpose of a Use Case Diagram?",
                "a": "To provide a high-level visual summary of system functions and show how external actors interact with those functions across the system boundary."
            },
            {
                "q": "What is an Activation Bar in a Sequence Diagram?",
                "a": "A thin vertical rectangle on a lifeline indicating that the object is currently executing a procedure or holding CPU control."
            },
            {
                "q": "What is the difference between a Decision node and a Fork node in an Activity diagram?",
                "a": "A Decision node chooses ONE alternate path based on a condition (diamond symbol). A Fork node splits execution into MULTIPLE parallel concurrent paths (solid bar)."
            },
            {
                "q": "What is a Guard Condition in a State Machine diagram?",
                "a": "A boolean expression written in square brackets `[x > 0]` that must evaluate to True for the state transition to occur."
            },
            {
                "q": "Explain the difference between Synchronous and Asynchronous messages.",
                "a": "A Synchronous message halts the sender until the receiver finishes and responds (filled arrowhead). An Asynchronous message lets the sender continue working immediately without waiting (open arrowhead)."
            }
        ],
        "checklist": [
            "Studied UML behavioural modeling concepts and notations",
            "Designed Use Case diagram with <<include>> and <<extend>>",
            "Constructed Activity diagram with decision and workflow nodes",
            "Modeled Chronological Sequence diagram for test runner",
            "Constructed State Machine diagram and completed quiz"
        ]
    },
    {
        "id": 7,
        "code": "RTU-SE-07",
        "title": "Manage Project Using ProjectLibre Project Management Software Tool",
        "category": "Project Management",
        "duration": "2 Hours",
        "difficulty": "Intermediate",
        "short_desc": "Plan, schedule, and track software engineering projects using Work Breakdown Structures (WBS), Gantt Charts, dependencies, and ProjectLibre.",
        "learning_objectives": [
            "Understand project planning, estimation, Work Breakdown Structure (WBS), and scheduling.",
            "Master Gantt Charts, milestones, task durations, and critical path concepts.",
            "Understand task dependencies (Finish-to-Start, Start-to-Start, Finish-to-Finish).",
            "Learn how to use ProjectLibre—an open-source project management alternative to Microsoft Project.",
            "Use the interactive Project Planning & Gantt Scheduler to create, link, and track project milestones."
        ],
        "theory_sections": [
            {
                "heading": "1. What is Software Project Management?",
                "content": """
**Software Project Management (SPM)** is the discipline of planning, organizing, staffing, monitoring, and controlling software development to deliver the product on schedule, within budget, and meeting quality standards.

### The Project Management Iron Triangle:
* **Scope:** Features and deliverables required.
* **Time:** Schedule and deadlines.
* **Cost:** Budget, personnel, and infrastructure resources.
* *Quality:* Bounded by the equilibrium of Scope, Time, and Cost.
"""
            },
            {
                "heading": "2. Work Breakdown Structure (WBS) & Gantt Charts",
                "content": """
* **Work Breakdown Structure (WBS):** A hierarchical decomposition of the total project scope into manageable deliverables and individual work packages.
* **Gantt Chart:** A horizontal bar chart introduced by Henry Gantt that illustrates a project schedule.
  * **X-axis:** Calendar timeline (days, weeks, months).
  * **Y-axis:** List of project tasks.
  * **Bars:** Represent duration, start date, end date, and % completion.
* **Milestone:** A zero-duration marker representing a critical event (e.g., *'SRS Approved by Guide'*, *'Beta Release'*).
"""
            },
            {
                "heading": "3. Task Dependencies & Relationships",
                "content": """
Tasks rarely happen in isolation; their execution order is determined by dependency constraints:
1. **Finish-to-Start (FS - Most Common):** Task B cannot start until Task A finishes (e.g., *Testing cannot start until Implementation finishes*).
2. **Start-to-Start (SS):** Task B can start once Task A starts (concurrent tasks).
3. **Finish-to-Finish (FF):** Task B cannot finish until Task A finishes.
4. **Start-to-Finish (SF):** Task B cannot finish until Task A starts (rare).

### Critical Path Method (CPM):
The sequence of dependent tasks that forms the **longest path** through the project. Any delay in a critical path task directly delays the entire project completion date.
"""
            },
            {
                "heading": "4. ProjectLibre Overview & Installation",
                "content": """
**ProjectLibre** is a leading free and open-source desktop alternative to Microsoft Project, widely used in academia and industry.

### Standard Workflow in ProjectLibre:
1. Download & Install ProjectLibre (Java-based open source).
2. Create New Project: Enter Project Name, Manager Name, and Start Date.
3. Define the Calendar (Standard 8-hour workday, weekend holidays).
4. Enter Task Names and estimated Durations (e.g., `2d`, `5d`, `1w`).
5. Indent Subtasks under summary parent tasks to generate the WBS.
6. Link Predecessors (e.g., set Task 3's predecessor to Task 2).
7. Inspect the auto-generated Gantt Chart and Critical Path (red bars).
8. Track progress by updating % Complete as work proceeds.
"""
            }
        ],
        "procedure": [
            "Open the Interactive Gantt Scheduler workspace inside LabPilot.",
            "Review the standard 8-task schedule for the LabPilot Virtual Lab project.",
            "Add/Edit tasks, specify duration in days, and configure Finish-to-Start predecessor dependencies.",
            "Review the auto-calculated project timeline, start/end dates, and milestones.",
            "View instructions on how to replicate the identical task list in the standalone ProjectLibre tool.",
            "Save the task schedule and export the Gantt summary report."
        ],
        "steps": [
            {
                "step_num": 1,
                "title": "Define Project Scope & Start Date",
                "instruction": "Set project baseline start date and name (e.g., LabPilot Virtual Lab Project).",
                "example": "Project Start: Day 1; Target Duration: 24 working days.",
                "expected_output": "Project calendar baseline established."
            },
            {
                "step_num": 2,
                "title": "Build Work Breakdown Structure (WBS)",
                "instruction": "Break project into 8 core phases: Requirements, SRS, DFD, Structure Design, UML, Coding, Testing, Documentation.",
                "example": "Tasks entered in order of execution.",
                "expected_output": "8-task WBS table populated."
            },
            {
                "step_num": 3,
                "title": "Assign Realistic Durations (Days)",
                "instruction": "Estimate effort for each task (e.g., Requirements: 2d, SRS: 3d, Implementation: 7d).",
                "example": "Sum of individual efforts = 24 total person-days.",
                "expected_output": "Durations assigned to every work package."
            },
            {
                "step_num": 4,
                "title": "Configure Predecessors (Dependencies)",
                "instruction": "Link tasks sequentially using Finish-to-Start (FS) constraints.",
                "example": "SRS (Task 2) depends on Requirements (Task 1); Testing (Task 7) depends on Coding (Task 6).",
                "expected_output": "Dependencies mapped with zero circular logic."
            },
            {
                "step_num": 5,
                "title": "Generate Visual Gantt Chart",
                "instruction": "Observe the visual timeline rendering bars, dependencies, and milestones.",
                "example": "Visual bar graph displaying overlapping and sequential activities.",
                "expected_output": "Interactive Gantt timeline rendered on screen."
            },
            {
                "step_num": 6,
                "title": "Identify Critical Path & Milestones",
                "instruction": "Identify tasks with zero slack/float where any delay delays final delivery.",
                "example": "Implementation and Testing are on the Critical Path.",
                "expected_output": "Critical tasks identified."
            },
            {
                "step_num": 7,
                "title": "Save Project Schedule",
                "instruction": "Save the task list and schedule into the SQLite database.",
                "example": "Click 'Save Schedule' to persist project data.",
                "expected_output": "Project plan saved in `practical_documents`."
            },
            {
                "step_num": 8,
                "title": "Attempt SPM Quiz & Complete Practical",
                "instruction": "Answer the assessment quiz and mark Experiment 7 complete.",
                "example": "Submit quiz responses.",
                "expected_output": "All 7 RTU experiments completed!"
            }
        ],
        "worked_example": {
            "title": "Standard LabPilot AI Project Schedule Table",
            "content": """
| Task ID | Task Description | Duration | Predecessors | Milestone Marker |
| :--- | :--- | :--- | :--- | :--- |
| **T-01** | Feasibility Study & Requirement Analysis | 2 Days | - | Project Kickoff |
| **T-02** | IEEE 830 SRS Document Drafting | 3 Days | T-01 | Baseline SRS Approved |
| **T-03** | Data Flow Diagram (Level 0 & 1) | 2 Days | T-02 | Analysis Sign-off |
| **T-04** | Structured Design (Structure Chart) | 2 Days | T-03 | Architectural Model |
| **T-05** | Object-Oriented UML Modeling (Static & Dynamic) | 3 Days | T-04 | Design Frozen |
| **T-06** | Implementation (Flask Server, GCC Engine, Web UI) | 7 Days | T-05 | Code Complete |
| **T-07** | Boundary Testing & Traceability Verification | 3 Days | T-06 | Alpha Verified |
| **T-08** | Final Documentation, Viva Prep & Deployment | 2 Days | T-07 | Final Lab Delivery |
"""
        },
        "quiz": [
            {
                "question": "What does the horizontal length of a bar on a Gantt Chart represent?",
                "options": ["Budget cost", "Task Duration (time)", "Number of developers assigned", "Code complexity"],
                "correct": 1,
                "explanation": "On a Gantt chart, the horizontal length of the bar directly represents the calendar duration of the task."
            },
            {
                "question": "In project management, what is a Milestone?",
                "options": [
                    "A task requiring at least one month of work.",
                    "A critical event or checkpoint having zero duration.",
                    "A bug in the source code.",
                    "A server upgrade."
                ],
                "correct": 1,
                "explanation": "A Milestone is a key progress checkpoint marking completion of a major deliverable, carrying 0 days duration."
            },
            {
                "question": "What is the Critical Path in a project network?",
                "options": [
                    "The path with the highest financial budget.",
                    "The longest sequence of dependent tasks that determines the earliest project completion date.",
                    "The easiest tasks assigned to juniors.",
                    "The network path with the most bugs."
                ],
                "correct": 1,
                "explanation": "The Critical Path is the longest continuous chain of dependent tasks; any delay on this path directly delays the overall project delivery."
            },
            {
                "question": "What is the most common dependency relationship between software tasks?",
                "options": ["Finish-to-Start (FS)", "Start-to-Start (SS)", "Finish-to-Finish (FF)", "Start-to-Finish (SF)"],
                "correct": 0,
                "explanation": "Finish-to-Start (FS) is the most standard dependency: Task B cannot begin until Task A has completed."
            },
            {
                "question": "ProjectLibre is a free, open-source desktop replacement for which commercial tool?",
                "options": ["Microsoft Word", "Microsoft Project", "Adobe Photoshop", "Docker Desktop"],
                "correct": 1,
                "explanation": "ProjectLibre was developed as a premier open-source desktop replacement for Microsoft Project."
            }
        ],
        "viva_questions": [
            {
                "q": "What is a Work Breakdown Structure (WBS)?",
                "a": "A hierarchical, deliverable-oriented decomposition of a project into smaller, manageable work packages that can be easily estimated, scheduled, and monitored."
            },
            {
                "q": "What is the Critical Path Method (CPM)?",
                "a": "A project modeling technique that calculates the longest path of planned activities to determine the minimum total time required to complete the project."
            },
            {
                "q": "What is Slack or Float in project scheduling?",
                "a": "The amount of time a task can be delayed without causing a delay to subsequent dependent tasks (Free Float) or the overall project completion date (Total Float)."
            },
            {
                "q": "What is the difference between a Task and a Milestone?",
                "a": "A Task consumes time, effort, and resources (e.g., 'Develop Flask Backend - 5 days'). A Milestone represents an instantaneous achievement checkpoint with zero duration (e.g., 'Code Frozen - 0 days')."
            },
            {
                "q": "Why is project scheduling essential in Software Engineering?",
                "a": "Without a schedule, teams cannot coordinate dependencies, manage resource bottlenecks, track delays, or commit to reliable delivery deadlines."
            }
        ],
        "checklist": [
            "Studied project planning, WBS, and Gantt chart scheduling concepts",
            "Configured 8 project tasks with durations and predecessors",
            "Inspected the visual Gantt timeline and critical path",
            "Learned ProjectLibre desktop workflow and procedures",
            "Completed the assessment quiz and verified all viva questions"
        ]
    }
]

def get_rtu_experiment_by_id(exp_id):
    for exp in RTU_EXPERIMENTS:
        if exp["id"] == int(exp_id):
            return exp
    return None

def get_all_rtu_experiments_summary():
    summary = []
    for exp in RTU_EXPERIMENTS:
        summary.append({
            "id": exp["id"],
            "code": exp["code"],
            "title": exp["title"],
            "category": exp["category"],
            "duration": exp["duration"],
            "difficulty": exp["difficulty"],
            "short_desc": exp["short_desc"],
            "learning_objectives": exp["learning_objectives"],
            "checklist": exp["checklist"]
        })
    return summary
