SECTION_MARKET_KEYWORDS = {
    "Skills": ["python", "java", "sql", "aws", "docker", "react"],
    "Experience": ["experience", "years", "worked", "industry"],
    "Projects": ["project", "built", "implemented"],
    "Education": ["degree", "btech", "university"],
    "Certifications": ["certification", "certified"]
}

def market_section_scores(market_text):
    market_text = market_text.lower()
    scores = {}

    for section, keywords in SECTION_MARKET_KEYWORDS.items():
        hits = sum(1 for k in keywords if k in market_text)
        total = len(keywords)

        # scale to 1–10 (same as resume scoring)
        score = round((hits / total) * 10, 1)

        # prevent zero-width bars
        scores[section] = max(score, 1)

    return scores
