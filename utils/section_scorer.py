SECTION_KEYWORDS = {
    "Skills": ["python", "java", "sql", "aws", "docker", "react", "ml", "nlp"],
    "Experience": ["experience", "worked", "developed", "led", "intern"],
    "Projects": ["project", "built", "implemented", "designed"],
    "Education": ["btech", "degree", "university", "college"],
    "Certifications": ["certification", "certified", "course"]
}

def score_sections(resume_text):
    resume_text = resume_text.lower()
    scores = {}

    for section, keywords in SECTION_KEYWORDS.items():
        hits = sum(1 for k in keywords if k in resume_text)
        total = len(keywords)

        # scale to 1–10
        score = round((hits / total) * 10, 1)

        # prevent zero score
        scores[section] = max(score, 1)

    return scores
