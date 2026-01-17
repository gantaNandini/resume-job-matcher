def generate_hybrid_explanation(score, skill_gap, market_skills, resume_text):
    explanations = []

    # 1️⃣ Semantic explanation
    if score < 40:
        explanations.append(
            "The resume content does not closely match the responsibilities and requirements described in the job description."
        )

    # 2️⃣ JD-level missing skills (EXPLICIT)
    if skill_gap and skill_gap.get("missing"):
        explanations.append(
            "Missing key skills from the job description: "
            + ", ".join(skill_gap["missing"][:6])
        )

    # 3️⃣ Market-level missing skills (EXPLICIT)
    resume_text = resume_text.lower()
    market_missing = []

    for skill, freq in market_skills.most_common(6):
        if skill not in resume_text:
            market_missing.append(skill)

    if market_missing:
        explanations.append(
            "Based on analysis of similar roles in the job market, the following commonly expected skills are missing: "
            + ", ".join(market_missing)
        )

    # 4️⃣ Final fallback (never empty)
    if not explanations:
        explanations.append(
            "The resume structure is complete, but the content depth and relevance to the target role can be improved."
        )

    return explanations
