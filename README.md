# AI Resume–Job Match Analytics Platform

A web-based ATS-style system that evaluates how well a resume matches a job description and presents the results using an interactive analytics dashboard.

## 🚀 Features
- PDF resume parsing
- Resume vs job description matching
- ATS-style match score (0–10)
- Skill gap analysis (matched vs missing skills)
- Section-wise resume evaluation
- Market vs resume comparison
- Interactive dashboard (Chart.js)
- Dark mode support
- Downloadable PDF report

## 🛠 Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript
- Chart.js
- PDF text extraction
- Jinja2 templates

## ▶️ How to Run
```bash
git clone https://github.com/your-username/resume-job-matcher.git
cd resume-job-matcher
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
