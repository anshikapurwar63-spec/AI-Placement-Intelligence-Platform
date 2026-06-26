import streamlit as st
import pickle
import pandas as pd
from datetime import datetime
import os
import PyPDF2

model = pickle.load(
    open("models/company_predictor.pkl", "rb")
)

encoder = pickle.load(
    open("models/company_encoder.pkl", "rb")
)

df = pd.read_csv(
    "data/student_data.csv"
)

st.set_page_config(
    page_title="AI Placement Intelligence Platform",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Placement Intelligence Platform")

st.write(
    "Predict placement opportunities using Machine Learning"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average CGPA",
        round(df["cgpa"].mean(), 2)
    )

with col2:
    placement_rate = round(
        (df["placement_status"] == "Placed").mean() * 100,
        1
    )

    st.metric(
        "Placement Rate",
        f"{placement_rate}%"
    )

with col3:
    st.metric(
        "Top Hiring Company",
        df["company"].mode()[0]
    )

st.markdown("---")

st.subheader("📝 Student Details")

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=8.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=85
)

internships = st.number_input(
    "Internships",
    min_value=0,
    max_value=10,
    value=2
)

projects = st.number_input(
    "Projects",
    min_value=0,
    max_value=10,
    value=3
)

communication = st.slider(
    "Communication Skills",
    1,
    10,
    7
)

aptitude_score = st.slider(
    "Aptitude Score",
    0,
    100,
    75
)

mock_interview_score = st.slider(
    "Mock Interview Score",
    0,
    100,
    70
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=20,
    value=2
)

hackathons = st.number_input(
    "Hackathons",
    min_value=0,
    max_value=20,
    value=1
)

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)
predict = st.button("🚀 Predict Company")

if predict:

    student = pd.DataFrame(
        [[
            cgpa,
            attendance,
            internships,
            projects,
            communication,
            aptitude_score,
            mock_interview_score,
            certifications,
            hackathons
        ]],
        columns=[
            "cgpa",
            "attendance",
            "internships",
            "projects",
            "communication",
            "aptitude_score",
            "mock_interview_score",
            "certifications",
            "hackathons"
        ]
    )

    if cgpa >= 8.5:
        company = ["Microsoft"]

    elif cgpa >= 8:
        company = ["Capgemini"]

    elif cgpa >= 7:
        company = ["Infosys"]

    else:
        company = ["Tech Mahindra"]

    probability = min(
        95,
        round(
            (cgpa * 10)
            + (internships * 5)
            + (projects * 3)
        )
    )

    score = round(
        (cgpa * 10)
        + (internships * 5)
        + (projects * 3)
    )

    confidence = max(
        60,
        probability - 3
    )
probability = min(
    95,
    round(
        (cgpa * 10)
        + (internships * 5)
        + (projects * 3)
    )
)
student = pd.DataFrame(
    [[
        cgpa,
        attendance,
        internships,
        projects,
        communication,
        aptitude_score,
        mock_interview_score,
        certifications,
        hackathons
    ]],
    columns=[
        "cgpa",
        "attendance",
        "internships",
        "projects",
        "communication",
        "aptitude_score",
        "mock_interview_score",
        "certifications",
        "hackathons"
    ]
)
prediction = model.predict(student)

company = encoder.inverse_transform(
    prediction
)
st.success(
        f"🎯 Predicted Company: {company[0]}"
    )
if cgpa >= 8.5:
    company = ["Microsoft"]

elif cgpa >= 8:
    company = ["Capgemini"]

elif cgpa >= 7:
    company = ["Infosys"]

else:
    company = ["Tech Mahindra"]
    
    # Resume Analysis

if resume_file is not None:

    pdf_reader = PyPDF2.PdfReader(resume_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    text = text.lower()

    skills = [
        "python",
        "sql",
        "power bi",
        "machine learning",
        "java",
        "c++",
        "html",
        "css"
    ]

    found_skills = []

    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    st.subheader("📄 Resume Analysis")

    st.success("Resume Successfully Read!")

    st.write("### ✅ Skills Found")

    if len(found_skills) > 0:

        for skill in found_skills:
            st.success(skill)

skills = [
    "python",
    "sql",
    "power bi",
    "machine learning",
    "java",
    "c++",
    "html",
    "css"
]

st.warning("Resume missing skills feature disabled")


st.subheader(
        "📈 Placement Probability"
)

st.progress(
    probability / 100
)

st.metric(
    "Probability",
    f"{probability}%"
)

st.subheader(
        "📊 Student Score"
    )

score = round(
        (cgpa * 10)
        + (internships * 5)
        + (projects * 3)
    )

st.metric(
        "Score",
        score
    )

    # Placement Readiness Gauge

st.subheader("🎯 Placement Readiness")

readiness = min(
        100,
        round(
            (cgpa * 10)
            + (internships * 5)
            + (projects * 3)
        )
    )

st.progress(readiness / 100)

st.metric(
        "Readiness Score",
        f"{readiness}%"
    )


st.subheader(
        "🎯 Placement Readiness"
    )

readiness = min(
        100,
        round(
            (cgpa * 10)
            + (internships * 5)
            + (projects * 3)
        )
    )

st.progress(
        readiness / 100
    )

st.metric(
    "Readiness Score",
        f"{readiness}%"
    )

if readiness >= 90:
        st.success("🏆 Excellent Candidate")

elif readiness >= 75:
        st.info("⭐ Good Candidate")

elif readiness >= 60:
        st.warning("⚠ Average Candidate")

else:
        st.error("❌ Needs Improvement")

st.subheader(
        "🏅 Student Ranking"
    )

if score >= 100:
        st.success("🏆 Top 10%")

elif score >= 80:
        st.info("🥈 Top 25%")

elif score >= 60:
        st.warning("🥉 Top 50%")

else:
        st.error("📚 Needs Improvement")
            # Top 3 Company Recommendations

st.write("DEBUG CGPA =", cgpa)
st.subheader(
        "🏆 Top 3 Company Recommendations"
    )

if cgpa >= 8.5:

        st.write("🥇 Microsoft")
        st.write("🥈 Amazon")
        st.write("🥉 Google")

elif cgpa >= 8:

        st.write("🥇 Capgemini")
        st.write("🥈 Cognizant")
        st.write("🥉 Accenture")

elif cgpa >= 7:

        st.write("🥇 Infosys")
        st.write("🥈 TCS")
        st.write("🥉 Wipro")

else:

        st.write("🥇 Tech Mahindra")
        st.write("🥈 HCL")
        st.write("🥉 Infosys")

    # Skill Gap Analysis

st.subheader(
        "📚 Skill Gap Analysis"
    )

if communication < 8:
        st.write("❌ Improve Communication Skills")

if aptitude_score < 80:
        st.write("❌ Improve Aptitude Skills")

if projects < 4:
        st.write("❌ Build More Projects")

if certifications < 3:
        st.write("❌ Gain More Certifications")

if (
        communication >= 8
        and aptitude_score >= 80
        and projects >= 4
        and certifications >= 3
    ):
        st.success(
            "✅ No Major Skill Gaps Found"
        )

    # Eligible Companies

st.subheader(
        "🏢 Eligible Companies"
    )

if cgpa >= 8.5:

        st.write("✅ Microsoft")
        st.write("✅ Amazon")
        st.write("✅ Google")
        st.write("✅ Oracle")

elif cgpa >= 8:

        st.write("✅ Capgemini")
        st.write("✅ Cognizant")
        st.write("✅ Accenture")
        st.write("✅ Infosys")

elif cgpa >= 7:

        st.write("✅ Infosys")
        st.write("✅ TCS")
        st.write("✅ Wipro")

else:

        st.write("✅ Tech Mahindra")
        st.write("✅ HCL")
        st.write("✅ Infosys")


history = pd.DataFrame(
        {
            "Date": [
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )
            ],
            "CGPA": [cgpa],
            "Score": [score],
            "Company": [company[0]],
            "Probability": [probability]
        }
    )

if os.path.exists(
        "prediction_history.csv"
    ):

        history.to_csv(
            "prediction_history.csv",
            mode="a",
            header=False,
            index=False
        )

else:

        history.to_csv(
            "prediction_history.csv",
            index=False
        )


report = f"""
    AI Placement Intelligence Platform

    Predicted Company: {company[0]}
    Placement Probability: {probability}%
    Student Score: {score}
    Readiness Score: {readiness}%
    """

st.download_button(
        "📥 Download Report",
        data=report,
        file_name="placement_report.txt",
        mime="text/plain"
    )


if os.path.exists(
    "prediction_history.csv"
    ):

        st.markdown("---")

st.subheader(
        "📜 Prediction History"
    )

history_df = pd.read_csv(
        "prediction_history.csv"
    )

st.dataframe(
        history_df.tail(10),
        use_container_width=True
    )

    # Footer

st.markdown("---")

st.caption(
    "AI Placement Intelligence Platform | Developed by Anshika Purwar"
    )