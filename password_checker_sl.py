# Save as app.py and run with: streamlit run app.py

import streamlit as st
import string

def check_common_password(password):
    try:
        with open('common-password.txt') as f:
            common = f.read().splitlines()
        return password in common
    except FileNotFoundError:
        return False

def password_strength(password):
    score = 0
    length = len(password)
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    if length > 8: score += 1
    if length > 12: score += 1
    if length > 17: score += 1
    if length > 20: score += 1
    score += sum([upper, lower, digit, special]) - 1
    if score < 4: return "Weak", score
    elif score == 4: return "Okay", score
    elif 4 < score < 6: return "Good", score
    else: return "Strong", score

def feedback(password):
    if check_common_password(password):
        return "⚠️ Common password. Score: 0/7"
    strength, score = password_strength(password)
    msg = f"**Strength:** {strength} (Score: {score}/7)\n\n"
    if score < 4:
        msg += "### Suggestions:\n"
        if len(password) <= 8: msg += "- Use more than 8 characters\n"
        if not any(c.isupper() for c in password): msg += "- Add uppercase letters\n"
        if not any(c.islower() for c in password): msg += "- Add lowercase letters\n"
        if not any(c.isdigit() for c in password): msg += "- Include numbers\n"
        if not any(c in string.punctuation for c in password): msg += "- Use special characters\n"
    return msg

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter password", type="password")

if st.button("Check"):
    st.markdown(feedback(password))
