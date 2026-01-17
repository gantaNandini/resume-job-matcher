def analyze_sections(resume_text):
    resume_text = resume_text.lower()

    sections = {
        "Skills": ["skills", "technical skills", "key skills"],
        "Experience": ["experience", "work experience", "employment"],
        "Projects": ["projects", "academic projects", "personal projects"],
        "Education": ["education", "qualification", "academic"],
        "Certifications": ["certification", "certifications", "courses"]
    }

    analysis = {}

    for section, keywords in sections.items():
        found = any(keyword in resume_text for keyword in keywords)

        if found:
            analysis[section] = "Present"
        else:
            analysis[section] = "Missing"

    return analysis
