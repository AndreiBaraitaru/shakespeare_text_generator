import pandas as pd
import os

def create_survey(generated_texts, filename="survey.csv"):
    data = {"Generated Text": generated_texts, "Rating (1-5)": [None] * len(generated_texts), "Comments": [None] * len(generated_texts)}
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Survey file '{filename}' created successfully.")

def analyze_feedback(filename="survey.csv"):
    if not os.path.exists(filename):
        print(f"Survey file '{filename}' not found.")
        return None, []

    df = pd.read_csv(filename)

    if "Rating (1-5)" not in df.columns or "Comments" not in df.columns:
        print("Invalid survey file format.")
        return None, []

    avg_rating = df["Rating (1-5)"].dropna().astype(float).mean() if not df["Rating (1-5)"].dropna().empty else None
    comments = df["Comments"].dropna().tolist()

    return avg_rating, comments

if __name__ == "__main__":
    sample_texts = ["to be or not to be", "shall I compare thee to a summer's day"]
    
    # Check if survey already exists
    if not os.path.exists("survey.csv"):
        create_survey(sample_texts)

    avg_rating, comments = analyze_feedback()

    if avg_rating is not None:
        print("Average Rating:", avg_rating)
    else:
        print("No ratings available yet.")

    if comments:
        print("Comments:", comments)
    else:
        print("No comments provided yet.")
