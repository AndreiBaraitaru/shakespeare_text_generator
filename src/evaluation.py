import pandas as pd

def create_survey(generated_texts, filename="survey.csv"):
    data = {"Generated Text": generated_texts, "Rating (1-5)": [""] * len(generated_texts), "Comments": [""] * len(generated_texts)}
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def analyze_feedback(filename="survey.csv"):
    df = pd.read_csv(filename)
    avg_rating = df["Rating (1-5)"].dropna().astype(float).mean()
    comments = df["Comments"].dropna().tolist()
    return avg_rating, comments

if __name__ == "__main__":
    sample_texts = ["to be or not to be", "shall I compare thee to a summer's day"]
    create_survey(sample_texts)
    avg_rating, comments = analyze_feedback()
    print("Average Rating:", avg_rating)
    print("Comments:", comments)
