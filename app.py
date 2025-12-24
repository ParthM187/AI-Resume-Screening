import streamlit as st
import plotly.express as px

from resume_skill_extractor import extract_resume_skills
from jd_skill_extractor import extract_jd_skills_from_text
from skill_matcher import match_skills
from google_recommender import get_google_recommendations

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Skill Matching System")
st.write("Upload your resume and paste the Job Description to see how well you match.")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📎 Upload Resume (PDF only)",
        type=["pdf"]
    )

with col2:
    jd_text = st.text_area(
        "📝 Paste Job Description",
        height=300
    )

analyze_btn = st.button("🔍 Analyze Resume")

# ---------------- PROCESSING ----------------
if analyze_btn:
    if resume_file is None or jd_text.strip() == "":
        st.warning("⚠️ Please upload resume and paste job description.")
    else:
        with st.spinner("Analyzing resume..."):
            # Extract skills
            resume_skills = extract_resume_skills(resume_file)
            jd_skills = extract_jd_skills_from_text(jd_text)

            matched_skills, missing_skills = match_skills(resume_skills, jd_skills)

            # Match %
            if len(jd_skills) > 0:
                match_percentage = round((len(matched_skills) / len(jd_skills)) * 100, 2)
            else:
                match_percentage = 0.0

        # ---------------- RESULTS ----------------
        st.subheader("📊 Match Results")

        st.metric("Match Percentage", f"{match_percentage} %")

        # --------- GRAPH ---------
        chart_data = {
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [len(matched_skills), len(missing_skills)]
        }

        fig = px.pie(
            chart_data,
            names="Category",
            values="Count",
            hole=0.5,
            title="Skill Match Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        # --------- SKILLS LIST ---------
        col3, col4 = st.columns(2)

        with col3:
            st.success("✅ Matched Skills")
            if matched_skills:
                for skill in matched_skills:
                    st.write(f"✔️ {skill}")
            else:
                st.write("No matched skills found.")

        with col4:
            st.error("❌ Missing Skills")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"❌ {skill}")
            else:
                st.write("No missing skills 🎉")

        # --------- RECOMMENDATIONS ---------
        if missing_skills:
            
            st.subheader("💡 Recommended Courses / Learning Resources")
            recommendations = get_google_recommendations(missing_skills)

            if recommendations:
                for rec in recommendations:
                    st.markdown(f"- {rec}")
            else:
                st.success("🎉 No recommendations needed. Your skills match well!")