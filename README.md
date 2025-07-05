# 🔐 Password Strength Checker

Passwords are the first line of defense in protecting digital systems. Weak or common passwords are often exploited through brute-force attacks, credential stuffing, and dictionary-based attacks. Therefore, ensuring that a password meets minimum complexity standards is crucial in cybersecurity.

This project presents a **Password Strength Checker** built using Python, offering both a **GUI application (Tkinter)** and a **web interface (Streamlit)**. It also includes a **modular utility file** for reusing password evaluation logic.

---

## 🎯 Objectives

- ✅ Check password strength based on:
  - Length
  - Character variety (uppercase, lowercase, digits, symbols)
  - Absence from common password lists
- ✅ Provide clear feedback and improvement tips
- ✅ Offer multiple user-friendly interfaces
- ✅ Follow modular coding best practices

---

## 🧪 Password Evaluation Criteria

Password strength is calculated using a scoring system based on length and character diversity.

### ✅ Length-Based Scoring:

| Condition                   | Score |
|----------------------------|-------|
| More than 8 characters     | +1    |
| More than 12 characters    | +1    |
| More than 17 characters    | +1    |
| More than 20 characters    | +1    |

### ✅ Character Variety (add 1 point per type):

- Contains uppercase letters → ✅  
- Contains lowercase letters → ✅  
- Contains digits → ✅  
- Contains special characters (e.g., `@#$%!`) → ✅  

**🎯 Score = Length score + (number of character types - 1)**  
**🔝 Maximum score: 7**

> ❗ If the password is found in the `common-passwords.txt` list, it is automatically marked **Weak**, regardless of the score.

---

## 📊 Strength Classification

| Score | Classification |
|-------|----------------|
| < 4   | Weak           |
| 4     | Okay           |
| 5–6   | Good           |
| 7     | Strong         |

---

## 🖥️ GUI App – Tkinter

### Features:
- Lightweight Python-based GUI
- User enters password in a secure input field
- Strength result shown in a pop-up alert

### How it works:
- Uses `tkinter` for layout and buttons
- Calls shared logic from `password_utils.py`
- Provides real-time feedback

---

## 🌐 Web App – Streamlit

### Features:
- Accessible in the browser via `localhost`
- Clean interface with password input field
- Instant feedback and improvement tips

### How it works:
- Uses `streamlit` to build UI
- Loads the logic from `password_utils.py`
- Renders the result as Markdown

---

## 🧰 Tech Stack

- **Language**: Python
- **Libraries**: `tkinter`, `streamlit`, `re`
- **Storage**: `common-passwords.txt` for weak password lookup

---

## 🚀 To Run

### 📦 Install Required Packages:

```bash
pip install streamlit
