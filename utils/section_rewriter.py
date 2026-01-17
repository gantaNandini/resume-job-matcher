def section_rewrite_tips(section_scores):
    tips = {}

    for section, score in section_scores.items():
        if score < 40:
            tips[section] = (
                f"Add more concrete examples, metrics, and relevant keywords in {section}."
            )
        elif score < 70:
            tips[section] = (
                f"Strengthen {section} by aligning it more closely with job requirements."
            )

    return tips
