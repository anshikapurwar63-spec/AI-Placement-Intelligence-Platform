import pandas as pd
import random

data = []

for i in range(1, 501):

    cgpa = round(random.uniform(5.5, 9.8), 2)
    attendance = random.randint(60, 100)
    internships = random.randint(0, 4)
    projects = random.randint(1, 6)

    python_skill = random.randint(0, 1)
    sql_skill = random.randint(0, 1)
    powerbi_skill = random.randint(0, 1)
    java_skill = random.randint(0, 1)
    cpp_skill = random.randint(0, 1)
    dsa_skill = random.randint(0, 1)

    communication = random.randint(5, 10)
    aptitude = random.randint(50, 100)
    mock_interview = random.randint(50, 100)

    certifications = random.randint(0, 5)
    hackathons = random.randint(0, 3)

    # SMART COMPANY ASSIGNMENT

    if cgpa >= 8.5 and internships >= 2 and projects >= 3:
        placement_status = "Placed"
        company = random.choice([
            "Oracle",
            "SAP",
            "IBM",
            "Deloitte"
        ])

    elif cgpa >= 7.5:
        placement_status = "Placed"
        company = random.choice([
            "Infosys",
            "Accenture",
            "Cognizant",
            "Capgemini"
        ])

    elif cgpa >= 6.5:
        placement_status = "Placed"
        company = random.choice([
            "TCS",
            "Wipro",
            "HCL",
            "Tech Mahindra"
        ])

    else:
        placement_status = "NotPlaced"
        company = "None"

    data.append([
        i,
        cgpa,
        attendance,
        internships,
        projects,
        python_skill,
        sql_skill,
        powerbi_skill,
        java_skill,
        cpp_skill,
        dsa_skill,
        communication,
        aptitude,
        mock_interview,
        certifications,
        hackathons,
        placement_status,
        company
    ])

columns = [
    "student_id",
    "cgpa",
    "attendance",
    "internships",
    "projects",
    "python",
    "sql",
    "powerbi",
    "java",
    "cpp",
    "dsa",
    "communication",
    "aptitude_score",
    "mock_interview_score",
    "certifications",
    "hackathons",
    "placement_status",
    "company"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/student_data.csv", index=False)

print("500 student records generated successfully!")
print(df.head())