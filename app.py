import streamlit as st
from check_breach import check_password, check_multiple_passwords

st.set_page_config(page_title="Password Breach Checker", page_icon="🔐")

st.title("🔐 Password Breach Checker")
st.write("Check if your password has appeared in known data breaches.")

option = st.radio(
    "Choose an option:",
    ("Check single password", "Check multiple passwords")
)

# ---- Single password ----
if option == "Check single password":
    password = st.text_input("Enter password", type="password")

    if st.button("Check Password"):
        if password:
            result = check_password(password)
            st.success(result)
        else:
            st.warning("Please enter a password.")

# ---- Multiple passwords ----
else:
    passwords = st.text_area(
        "Enter multiple passwords (one per line)"
    )

    if st.button("Check Passwords"):
        if passwords.strip():
            password_list = [p.strip() for p in passwords.splitlines()]
            results = check_multiple_passwords(password_list)

            for res in results:
                st.write(res)
        else:
            st.warning("Please enter at least one password.")