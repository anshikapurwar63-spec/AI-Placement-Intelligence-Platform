import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("data/student_data.csv")

# Remove NotPlaced students
df = df[df["placement_status"] == "Placed"]

# Features
X = df[
    [
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
]

# Target
y = df["company"]

# Encode companies
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# Save model
pickle.dump(
    model,
    open("models/company_predictor.pkl", "wb")
)

pickle.dump(
    encoder,
    open("models/company_encoder.pkl", "wb")
)

print("Model saved successfully!")