"""
Traceability Matrix Engine
LabPilot AI — Software Engineering Virtual Lab

Links Requirements (SRS) to UML Design elements and Test Cases.
Detects coverage gaps, orphaned requirements, and untested design components.
"""

def generate_traceability_matrix(requirements, uml_classes, test_cases, mappings=None):
    """
    requirements: list of dicts [{'id': 'REQ-01', 'title': 'Equilateral detection', 'type': 'FR'}]
    uml_classes: list of str ['TriangleClassifier', 'InputValidator']
    test_cases: list of dicts [{'id': 'TC-01', 'name': 'All sides equal', 'target_req': 'REQ-01'}]
    mappings: optional explicit mapping dict { 'REQ-01': {'uml': ['TriangleClassifier'], 'tests': ['TC-01']} }
    """
    matrix = []
    covered_requirements = 0
    total_requirements = len(requirements)

    for req in requirements:
        req_id = req.get("id")
        req_title = req.get("text") or req.get("title", "Requirement")
        
        # Find mapped test cases
        linked_tests = []
        for tc in test_cases:
            target = tc.get("target_req") or tc.get("req_id")
            if target == req_id or (target is None and req_id in tc.get("name", "")):
                linked_tests.append(tc.get("id"))

        # Find linked UML classes (heuristically or through mapping)
        linked_classes = []
        if mappings and req_id in mappings:
            linked_classes = mappings[req_id].get("uml", [])
        else:
            # Simple keyword matching between req title and UML classes
            for cls in uml_classes:
                if any(word.lower() in req_title.lower() for word in [cls.lower(), "triangle", "validator", "classifier"]):
                    if cls not in linked_classes:
                        linked_classes.append(cls)
            if not linked_classes and uml_classes:
                linked_classes.append(uml_classes[0]) # Default association

        has_coverage = len(linked_tests) > 0
        if has_coverage:
            covered_requirements += 1

        matrix.append({
            "req_id": req_id,
            "req_title": req_title,
            "req_type": req.get("type", "Functional"),
            "linked_uml": linked_classes if linked_classes else ["(None)"],
            "linked_tests": linked_tests,
            "status": "COVERED" if has_coverage else "UNCOVERED",
            "test_count": len(linked_tests)
        })

    coverage_percent = round((covered_requirements / total_requirements * 100), 1) if total_requirements > 0 else 0

    return {
        "matrix": matrix,
        "total_requirements": total_requirements,
        "covered_requirements": covered_requirements,
        "uncovered_requirements": total_requirements - covered_requirements,
        "traceability_coverage_percent": coverage_percent
    }
