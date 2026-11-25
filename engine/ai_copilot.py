"""
AI Practical Copilot & Mistake DNA Engine
LabPilot AI — Software Engineering Virtual Lab

Provides:
- Contextual hints for students during experiments
- "Mistake DNA" diagnosis (pattern recognition on common student errors)
- Teacher-level pedagogical feedback
"""

def generate_experiment_hints(experiment_type, step, student_data):
    """
    Returns contextual Socratic hints (not direct solutions, but guiding questions).
    """
    hints = []
    if experiment_type == "triangle":
        if step == "srs":
            hints.append("💡 Hint: What should happen if a user enters three zeros (0 0 0)? Did you specify this in your SRS?")
            hints.append("💡 Hint: Remember to state whether floating point inputs are permitted or only integer values.")
        elif step == "testing":
            hints.append("💡 Boundary Value Hint: The sum of two sides must be strictly greater than the third side. What test case verifies (1, 2, 3)?")
            hints.append("💡 Negative Testing Hint: Have you added at least one test case with negative lengths (e.g. -5, 5, 5)?")
        elif step == "uml":
            hints.append("💡 Design Hint: Does your TriangleClassifier class have clear responsibility separation from the InputValidator class?")
    elif experiment_type == "atm":
        if step == "testing":
            hints.append("💡 Security Hint: What happens if a user enters incorrect PIN 3 consecutive times?")
            hints.append("💡 Financial Boundary Hint: What happens if withdrawal amount equals the exact balance ($0 left)?")

    return hints

def diagnose_mistake_dna(srs_results, test_results):
    """
    Analyzes student submissions to identify recurring error patterns ('Mistake DNA').
    """
    patterns = []
    
    # Check SRS Ambiguity Pattern
    if srs_results:
        ambiguities = srs_results.get("total_ambiguities_detected", 0)
        if ambiguities >= 3:
            patterns.append({
                "code": "AMBIGUITY_TRAP",
                "title": "Subjective Requirement Bias",
                "severity": "MEDIUM",
                "description": f"You used {ambiguities} subjective terms (e.g., 'fast', 'user-friendly'). In SE, requirements must be testable with numbers.",
                "recommendation": "Replace adjectives with numeric thresholds (e.g., replace 'fast' with 'execution time < 50ms')."
            })

    # Check Boundary Value Testing Pattern
    if test_results and "results" in test_results:
        failed_tests = [t for t in test_results["results"] if not t["passed"]]
        total_tests = len(test_results["results"])
        
        # Check if tests include boundary cases (0 or negative)
        has_negative_input = any("-" in str(t.get("input", "")) for t in test_results["results"])
        has_zero_input = any("0" in str(t.get("input", "")).split() for t in test_results["results"])

        if not has_negative_input and not has_zero_input:
            patterns.append({
                "code": "BOUNDARY_BLINDNESS",
                "title": "Happy-Path / Positive Testing Bias",
                "severity": "HIGH",
                "description": "Your test suite only tests valid, positive inputs. It lacks boundary conditions (0, negative numbers).",
                "recommendation": "Apply Boundary Value Analysis (BVA): Test Minimum-1, Minimum, Maximum, and Maximum+1."
            })

        if failed_tests:
            patterns.append({
                "code": "INEQUALITY_FAILURE",
                "title": "Edge-Case Validation Mismatch",
                "severity": "HIGH",
                "description": f"{len(failed_tests)} out of {total_tests} test cases failed output verification.",
                "recommendation": "Review edge conditions where inputs are degenerate cases (e.g., side lengths 1, 2, 3 where 1+2=3)."
            })

    if not patterns:
        patterns.append({
            "code": "CLEAN_PASS",
            "title": "Strong Engineering Rigor",
            "severity": "LOW",
            "description": "No recurring critical patterns found. Requirements are verifiable and test coverage is comprehensive.",
            "recommendation": "Proceed to next advanced practical (e.g., State Machine / Concurrency testing)."
        })

    return patterns
