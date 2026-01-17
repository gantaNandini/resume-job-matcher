# utils/market_vs_you.py
def market_vs_you(market_skills, resume_text, top_n=5):
    resume_text = resume_text.lower()
    report = []

    for skill, freq in market_skills.most_common(top_n):
        if skill in resume_text:
            report.append((skill, "Present in your resume"))
        else:
            report.append((skill, "Missing (common in market)"))

    return report
