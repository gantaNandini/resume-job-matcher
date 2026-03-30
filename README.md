AI Resume–Job Match Analytics Platform

A web-based ATS-style intelligent system that analyzes how well a resume matches a job description and presents results through an interactive analytics dashboard.

🌟 Features
📄 PDF resume parsing
🎯 Resume vs job description matching
📊 ATS-style match score (0–10)
🧠 Skill gap analysis (matched vs missing skills)
🧩 Section-wise resume evaluation
📈 Market vs resume comparison
📉 Interactive dashboard (Chart.js)
🌙 Dark mode support
📥 Downloadable PDF report
🛠 Technologies Used
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Visualization: Chart.js
Templating: Jinja2
PDF Processing: Text extraction libraries
▶️ How to Run (Without Docker)
git clone https://github.com/gantaNandini/resume-job-matcher.git
cd resume-job-matcher

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app.py

👉 Open in browser:

http://localhost:5000
🐳 How to Run (Using Docker)
1. Build Docker image
docker build -t resume-matcher .
2. Run Docker container
docker run -p 5000:5000 resume-matcher

👉 Open in browser:

http://localhost:5000
