import streamlit as st
import random
import string

def generate_password(length , use_digit , use_special):
    character = string.ascii_letters

    if use_digit:
        character += string.digits

    if use_special:
        character += string.punctuation
    
    return ''.join(random.choice(character) for _ in range(length))

st.title("Password Generator")

length = st.slider("Length of password", 4, 30, 14)

use_digit = st.checkbox("Use Digits")

use_special = st.checkbox("Use Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digit , use_special)
    st.write(f"Generated passwrod:  {password}")

st.write("---------------------------------------------------")

st.write("Build with ❤️ by [Ahzaz Ahmed](https://github.com/AHZAZAHMED)")