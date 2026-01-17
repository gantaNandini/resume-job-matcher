import pandas as pd
from collections import Counter

COMMON_SKILLS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "data analysis", "flask", "django", "react", "node",
    "aws", "docker", "kubernetes", "git", "rest api", "microservices"
]

def extract_market_skills(jobs_csv_path, job_text):
    df = pd.read_csv(jobs_csv_path)

    job_text = job_text.lower()
    skill_counter = Counter()

    for _, row in df.iterrows():
        jd = str(row.get("jobdescription", "")).lower()

        # only consider similar roles
        if any(word in jd for word in job_text.split()[:5]):
            for skill in COMMON_SKILLS:
                if skill in jd:
                    skill_counter[skill] += 1

    return skill_counter
