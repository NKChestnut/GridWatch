import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load Merged Multi-Year Data 
df = pd.read_csv("data/merged.csv")

# Optional: Add Time Features 
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour
df["month"] = pd.to_datetime(df["datetime"]).dt.month

# Feature Columns 
features = ["GHI", "Temperature", "Relative Humidity", "hour", "month"]
X = df[features]
y = df["grid_risk"]

# Train/Test Split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Class-Balanced Model 
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Evaluate Performance 
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, "models/gridwatch_model.pkl")
print("Model saved to models/gridwatch_model.pkl")
