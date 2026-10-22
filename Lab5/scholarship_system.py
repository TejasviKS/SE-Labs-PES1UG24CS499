"""Student scholarship eligibility screener."""
import json

# Global state
RESULTS = {}
WEIGHTS = {"gpa": 10, "credits": 2}
INCOME_LIMIT = 800000
CUTOFF = 85


def calculate_merit_score(gpa, credit_points):
    """Return merit score from GPA and extracurricular credits."""
    return gpa * WEIGHTS["gpa"] + credit_points * WEIGHTS["credits"]


def evaluate_applicant(student_id, test_scores, logs=None):
    """Score one applicant, store the result and return eligibility."""
    if logs is None:
        logs = []
    gpa = test_scores["gpa"]
    credit_point = test_scores.get("credits", 0)
    income = test_scores.get("income", 0)
    score = calculate_merit_score(gpa, credit_point)
    eligible = score >= CUTOFF and income < INCOME_LIMIT
    RESULTS[student_id] = {"score": score, "eligible": eligible}
    logs.append(f"{student_id} scored {score}")
    return eligible


def change_weights(gpa_weight, credit_weight):
    """Update the merit score weights."""
    WEIGHTS["gpa"] = gpa_weight
    WEIGHTS["credits"] = credit_weight


def persist_results(filename="scholarships.json"):
    """Save results to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(RESULTS, file)


def load_results(filename="scholarships.json"):
    """Load results from a JSON file, if it exists."""
    try:
        with open(filename, encoding="utf-8") as file:
            RESULTS.update(json.load(file))
    except (FileNotFoundError, json.JSONDecodeError):
        print("No saved results found, starting fresh.")


def print_shortlist():
    """Print all eligible applicants."""
    print("Shortlisted applicants:")
    for student_id, result in RESULTS.items():
        if result["eligible"]:
            print(" ", student_id, "score =", result["score"])


def main():
    """Evaluate sample applicants and show the shortlist."""
    evaluate_applicant("U001", {"gpa": 9.1, "credits": 4, "income": 450000})
    evaluate_applicant("U002", {"gpa": 7.2, "credits": 1, "income": 300000})
    evaluate_applicant("U003", {"gpa": 12.5, "credits": -3, "income": -1})
    evaluate_applicant("U004", {"gpa": 6.5})
    try:
        gpa_w = float(input("GPA weight (Enter = 10): ") or WEIGHTS["gpa"])
        credit_w = float(input("Credits weight (Enter = 2): ")
                         or WEIGHTS["credits"])
    except ValueError:
        print("Invalid number, keeping default weights")
    else:
        change_weights(gpa_w, credit_w)
    evaluate_applicant("U005", {"gpa": 8.4, "credits": 3, "income": 600000})
    persist_results()
    load_results()
    print_shortlist()


if __name__ == "__main__":
    main()
