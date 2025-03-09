import re  # Used for regular expressions to check password conditions.
import random # Used for generating random strong passwords.
import string # Used for generating random strong passwords.
import streamlit as st # Python library for creating web apps.

# for password strength meter
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(10))

# Streamlit UI
st.title("🔒 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"): # Creates a button in the Streamlit app.
    if password:
        result, feedback = check_password_strength(password)
        st.write(result)
        for tip in feedback:
            st.write(tip)
    else:
        st.write("❌ Please enter a password to check.")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.write(f"🔑 Suggested Strong Password: `{strong_password}`")
