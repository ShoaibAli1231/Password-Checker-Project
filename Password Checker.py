import string


COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "letmein"
}


def evaluate_password(password: str) -> dict:
    """
    Evaluates the strength of a password and returns
    a dictionary containing the score, strength label,
    and improvement suggestions.
    """
    score = 0
    feedback = []

    # Rule checks
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    is_common = password.lower() in COMMON_PASSWORDS

    if length_ok:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if has_upper:
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if has_lower:
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if has_digit:
        score += 1
    else:
        feedback.append("Include at least one numeric digit.")

    if has_special:
        score += 1
    else:
        feedback.append("Include at least one special character.")

    if is_common:
        score = 0
        feedback.append("This password is too common. Choose a more unique password.")

    # Strength classification
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


def main():
    password = input("Enter a password to evaluate: ")
    result = evaluate_password(password)

    print("\nPassword Strength:", result["strength"])
    print("Score:", result["score"], "/ 5")

    if result["feedback"]:
        print("\nSuggestions for improvement:")
        for suggestion in result["feedback"]:
            print("-", suggestion)


if __name__ == "__main__":
    main()
