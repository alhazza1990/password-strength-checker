import re
import getpass

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Add symbols (!@#$).")

    return score, feedback


def strength_level(score):
    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    return levels.get(score, "Unknown")


def main():
    print("=== Password Strength Checker ===")
    password = getpass.getpass("Enter password: ")

    score, feedback = check_password_strength(password)
    level = strength_level(score)

    print(f"\nStrength: {level} ({score}/5)")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print("- " + item)
    else:
        print("Excellent password ✅")


if __name__ == "__main__":
    main()
