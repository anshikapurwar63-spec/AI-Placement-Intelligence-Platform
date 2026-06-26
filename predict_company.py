import pickle
import pandas as pd

model = pickle.load(
    open("models/company_predictor.pkl", "rb")
)

encoder = pickle.load(
    open("models/company_encoder.pkl", "rb")
)

student = pd.DataFrame(
    [[
        8.5,  # cgpa
        90,   # attendance
        2,    # internships
        4,    # projects
        8,    # communication
        85,   # aptitude
        80,   # mock interview
        3,    # certifications
        1     # hackathons
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

company = encoder.inverse_transform(prediction)

print("Predicted Company:", company[0])