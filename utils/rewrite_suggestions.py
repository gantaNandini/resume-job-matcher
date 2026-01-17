def rewrite_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills[:6]:
        suggestions.append(
            f"Add a bullet point demonstrating hands-on experience with {skill} (project, internship, or certification)."
        )
    return suggestions
