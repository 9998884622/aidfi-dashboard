import streamlit as st
import json

st.title("Login")

email=st.text_input("Email")

password=st.text_input("Password",type="password")

if st.button("Login"):

    with open("users.json") as f:

        users=json.load(f)

    if email in users and users[email]==password:

        st.session_state.user=email

        st.success("Login Success")

    else:

        st.error("Invalid")
