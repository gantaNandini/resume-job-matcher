COMMON_SKILLS = [
    "python", "java", "c++", "sql",
    "machine learning", "deep learning", "data analysis",
    "flask", "django", "fastapi",
    "html", "css", "javascript", "react", "node",
    "nlp", "computer vision",
    "aws", "docker", "kubernetes",
    "git", "rest api", "microservices"
]

def analyze_skill_gap(resume_text, job_text):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    missing_skills = []
    matched_skills = []

    for skill in COMMON_SKILLS:
        if skill in job_text:
            if skill in resume_text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

    return {
        "matched": matched_skills,
        "missing": missing_skills
    }
