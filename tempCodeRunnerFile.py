import string

# Check if the password is in a list of common passwords
def check_common_password(password):
    try:
        with open('common-password.txt', 'r') as f:
            common = f.read().splitlines()
        return password in common
    except FileNotFoundError:
        print("⚠️ 'common-password.txt' not found! Skipping common password check.")
        return False

# Evaluate password strength based on length and character variety
def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digits]

    # Length-based scoring
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    # Variety scoring
    score += sum(characters) - 1  # -1 to adjust over-scoring

    # Strength classification
    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score

# Generate user-friendly feedback
def feedback(password):
    if check_common_password(password):
        return "⚠️ Password was found in a common password list. Score: 0/7"

    strength, score = password_strength(password)

    feedback_msg = f"✅ Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback_msg += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback_msg += "- Make your password longer (more than 8 characters).\n"
        if not any(c.isupper() for c in password):
            feedback_msg += "- Include uppercase letters.\n"
        if not any(c.islower() for c in password):
            feedback_msg += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            feedback_msg += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback_msg += "- Add numbers.\n"

    return feedback_msg

# Main function to run the checker
if __name__ == "__main__":
    password = input("🔐 Enter your password: ")
    print(feedback(password))
