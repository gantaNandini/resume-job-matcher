def generate_suggestions(section_analysis):
    suggestions = []

    if section_analysis["Skills"] == "Missing":
        suggestions.append("Add a clear Skills section with relevant technical skills.")

    if section_analysis["Experience"] == "Missing":
        suggestions.append("Include an Experience section describing your roles and responsibilities.")

    if section_analysis["Projects"] == "Missing":
        suggestions.append("Add 1–2 relevant projects aligned with the job description.")

    if section_analysis["Education"] == "Missing":
        suggestions.append("Mention your educational background clearly.")

    if section_analysis["Certifications"] == "Missing":
        suggestions.append("Add certifications or courses relevant to the job role.")

    return suggestions
