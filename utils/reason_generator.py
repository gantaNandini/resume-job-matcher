def generate_reasons(score, skill_gap):
    reasons = []

    if score < 40:
        reasons.append(
            "The overall content of the resume does not align well with the job description."
        )

    if len(skill_gap["missing"]) > 0:
        reasons.append(
            "Several important technical skills required for this role are missing from the resume."
        )

    if score < 20:
        reasons.append(
            "The resume appears to be focused on a different role or technology stack."
        )

    return reasons
