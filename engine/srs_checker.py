"""
SRS Quality & Ambiguity Checker Module
LabPilot AI — Software Engineering Virtual Lab

Analyzes Software Requirement Specifications (SRS) for:
- Ambiguous / vague terms (e.g., 'fast', 'user-friendly', 'secure')
- Measurable metrics (e.g., seconds, %, numbers)
- Proper formatting and classification
"""

import re

# Vague terms and explanations according to IEEE 830 standards
AMBIGUITY_DICTIONARY = {
    "fast": "Subjective term. Specify an exact response time threshold (e.g., 'response time < 200ms').",
    "quick": "Subjective term. Specify a quantitative duration (e.g., 'within 2 seconds').",
    "user-friendly": "Vague. Specify usability criteria (e.g., 'requires <= 3 clicks' or 'usable without prior training').",
    "user friendly": "Vague. Specify usability criteria (e.g., 'requires <= 3 clicks').",
    "robust": "Non-testable. Specify exact error handling behavior under failure.",
    "secure": "Vague. Specify standard protocols (e.g., 'using AES-256 encryption and HTTPS').",
    "efficient": "Subjective. Define memory, CPU usage, or execution time limits.",
    "easy": "Subjective. Define training duration or error rate for users.",
    "approximate": "Uncertain boundary. Give exact allowable tolerance (e.g., '+/- 5%').",
    "optimal": "Unmeasurable. Define the exact optimization objective.",
    "flexible": "Vague. Specify what parameters or configurations can be changed.",
    "adequate": "Indefinite. Specify minimum acceptable standard.",
    "real-time": "Ambiguous. Define maximum permissible latency in milliseconds."
}

def analyze_requirement(req_text, req_id="REQ", req_type="Functional", priority="Must-Have"):
    """
    Analyzes a single requirement statement and returns quality metrics and warnings.
    """
    text_lower = req_text.lower()
    issues = []
    suggestions = []

    # 1. Ambiguity word check
    detected_words = []
    for word, advice in AMBIGUITY_DICTIONARY.items():
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text_lower):
            detected_words.append(word)
            issues.append(f"Ambiguous term '{word}' found.")
            suggestions.append(advice)

    # 2. Measurability check (numbers, percentages, units)
    has_metrics = bool(re.search(r'\b\d+(\.\d+)?(%|ms|s|sec|seconds|px|mb|gb|users|req/s)?\b', text_lower))

    # 3. Action verb check (shall, must, will, should)
    has_modal_verb = bool(re.search(r'\b(shall|must|should|will|can)\b', text_lower))
    if not has_modal_verb:
        issues.append("Missing standard requirement modal verb (e.g., 'The system SHALL...').")
        suggestions.append("Follow standard IEEE format: 'The system SHALL <perform specific action> when <condition>.'")

    # 4. Length check
    words_count = len(req_text.split())
    if words_count < 5:
        issues.append("Requirement is too short and lacks operational context.")
        suggestions.append("Include input, action, and expected system response.")
    elif words_count > 45:
        issues.append("Requirement is too compound; consider breaking it into atomic sub-requirements.")
        suggestions.append("Split compound sentences connected with multiple 'and/also' into individual requirements.")

    # Calculate quality score (0 to 100)
    score = 100
    score -= (len(detected_words) * 20)
    if not has_modal_verb:
        score -= 20
    if not has_metrics and req_type == "Non-Functional":
        score -= 25
        issues.append("Non-Functional Requirement lacks measurable verification criteria.")
        suggestions.append("Add measurable thresholds (e.g., 'within 500ms', 'uptime 99.9%').")
    if words_count < 5:
        score -= 20

    score = max(10, min(100, score))

    status = "EXCELLENT" if score >= 85 else ("ACCEPTABLE" if score >= 60 else "NEEDS_REVISION")

    return {
        "req_id": req_id,
        "text": req_text,
        "type": req_type,
        "priority": priority,
        "score": score,
        "status": status,
        "detected_ambiguities": detected_words,
        "issues": issues,
        "suggestions": suggestions,
        "has_metrics": has_metrics
    }

def analyze_srs_document(requirements_list):
    """
    Analyzes an entire list of requirement dicts.
    """
    analyzed_items = []
    total_score = 0
    ambiguity_count = 0

    for req in requirements_list:
        res = analyze_requirement(
            req_text=req.get("text", ""),
            req_id=req.get("id", "REQ-01"),
            req_type=req.get("type", "Functional"),
            priority=req.get("priority", "Must-Have")
        )
        analyzed_items.append(res)
        total_score += res["score"]
        ambiguity_count += len(res["detected_ambiguities"])

    count = len(requirements_list)
    average_score = round(total_score / count) if count > 0 else 0

    return {
        "requirements": analyzed_items,
        "average_score": average_score,
        "total_requirements": count,
        "total_ambiguities_detected": ambiguity_count,
        "overall_grade": "A" if average_score >= 85 else ("B" if average_score >= 70 else ("C" if average_score >= 50 else "D"))
    }
