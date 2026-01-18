from flask import Flask, render_template, request, session

from utils.resume_parser import extract_resume_text
from utils.section_analyzer import analyze_sections
from utils.suggestions import generate_suggestions
from utils.skill_gap import analyze_skill_gap
from utils.market_analyzer import extract_market_skills
from utils.hybrid_explainer import generate_hybrid_explanation
from utils.market_vs_you import market_vs_you
from utils.rewrite_suggestions import rewrite_suggestions
from utils.section_scorer import score_sections
from utils.confidence import confidence_label
from utils.market_section_scores import market_section_scores
from utils.pdf_report import generate_pdf
from utils.section_rewriter import section_rewrite_tips


# ---------------- APP SETUP ----------------
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback-secret")


# ---------------- HELPER ----------------
def to_python(obj):
    """Convert numpy / non-JSON types to pure Python"""
    if isinstance(obj, dict):
        return {k: to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_python(v) for v in obj]
    elif hasattr(obj, "item"):
        return obj.item()
    else:
        return obj


# ---------------- MAIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    confidence = None
    error = None

    section_analysis = None
    suggestions = None
    skill_gap = None
    hybrid_reasons = None
    market_compare = None
    section_scores = None
    market_section_scores_data = None
    rewrite_tips = None
    rewrite_by_section = None
    pdf_path = None

    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_description = request.form.get("job_description")

        if not resume_file or not job_description:
            error = "Please upload a resume and enter a job description."
        else:
            resume_text = extract_resume_text(resume_file)

            if not resume_text:
                error = "Unable to read resume file."
            else:
                # 1️⃣ SECTION SCORES (1–10)
                section_scores = score_sections(resume_text)

                # 2️⃣ OVERALL SCORE (1–10)
                score = round(
                    sum(section_scores.values()) / len(section_scores),
                    1
                )
                score = max(score, 1)

                # 3️⃣ CONFIDENCE
                confidence = confidence_label(score)

                # 4️⃣ ANALYSIS
                section_analysis = analyze_sections(resume_text)
                skill_gap = analyze_skill_gap(resume_text, job_description)
                suggestions = generate_suggestions(section_analysis)

                rewrite_by_section = section_rewrite_tips(section_scores)

                # 5️⃣ MARKET INTELLIGENCE
                market_skills = extract_market_skills("data/jobs.csv", job_description)
                market_compare = market_vs_you(market_skills, resume_text)

                market_text = " ".join(market_skills.elements())
                market_section_scores_data = market_section_scores(market_text)

                # 6️⃣ AI EXPLANATION
                hybrid_reasons = generate_hybrid_explanation(
                    score,
                    skill_gap,
                    market_skills,
                    resume_text
                )

                # 7️⃣ REWRITE TIPS
                rewrite_tips = rewrite_suggestions(skill_gap["missing"]) if skill_gap else None

                # 8️⃣ PDF REPORT
                pdf_path = generate_pdf(
                    score,
                    confidence,
                    section_scores,
                    skill_gap,
                    hybrid_reasons
                )

                # 9️⃣ SAVE DASHBOARD DATA
                session["dashboard_data"] = to_python({
                    "score": score,
                    "confidence": confidence,
                    "section_scores": section_scores,
                    "skill_gap": skill_gap,
                    "market_compare": market_compare
                })

    return render_template(
        "index.html",
        score=score,
        confidence=confidence,
        section_scores=section_scores,
        section_analysis=section_analysis,
        skill_gap=skill_gap,
        reasons=hybrid_reasons,
        suggestions=suggestions,
        market_compare=market_compare,
        market_section_scores=market_section_scores_data,
        rewrite_tips=rewrite_tips,
        rewrite_by_section=rewrite_by_section,
        pdf_path=pdf_path,
        error=error
    )


# ---------------- DASHBOARD HELPERS ----------------
def ai_section_suggestions(section_scores):
    suggestions = {}
    for section, score in section_scores.items():
        if score < 5:
            suggestions[section] = (
                f"Your {section} section is weak. Add role-specific keywords, "
                f"quantify achievements, and align with the job description."
            )
        elif score < 7.5:
            suggestions[section] = (
                f"Your {section} section is decent. Improve clarity and include "
                f"impact metrics or tools used."
            )
        else:
            suggestions[section] = (
                f"Your {section} section is strong. Minor optimization recommended."
            )
    return suggestions


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    data = session.get("dashboard_data")

    if not data:
        return "No analysis data found. Please analyze a resume first."

    section_ai_tips = ai_section_suggestions(data["section_scores"])

    market_compare = data.get("market_compare", {
        "Skills": 7.5,
        "Projects": 7.0,
        "Experience": 8.0,
        "Education": 6.5,
        "Certifications": 6.0
    })

    ats_keywords = {
        "Python": True,
        "Machine Learning": True,
        "SQL": False,
        "Docker": False,
        "REST API": True
    }

    improvement_checklist = [
        "Add missing skills from the job description",
        "Quantify achievements using numbers",
        "Mirror job description keywords",
        "Improve project descriptions",
        "Add relevant certifications or tools"
    ]

    return render_template(
        "dashboard.html",
        score=data["score"],
        confidence=data["confidence"],
        section_scores=data["section_scores"],
        skill_gap=data["skill_gap"],
        market_compare=market_compare,
        section_ai_tips=section_ai_tips,
        ats_keywords=ats_keywords,
        improvement_checklist=improvement_checklist
    )


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
