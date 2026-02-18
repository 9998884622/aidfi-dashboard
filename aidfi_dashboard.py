import streamlit as st
import json
import os


USER_FILE = "users.json"


# Load users
def load_users():

    if os.path.exists(USER_FILE):

        with open(USER_FILE, "r") as f:

            return json.load(f)

    return {}



# Save users
def save_users(users):

    with open(USER_FILE, "w") as f:

        json.dump(users, f)




# Page Config
st.set_page_config(page_title="AIDFI Login", layout="centered")



# CSS for same UI as image
st.markdown("""

<style>

body{

background-color:#0f7c8f;

}

.box{

background-color:#e6e6e6;

padding:40px;

border-radius:10px;

}

.red{

color:red;

font-size:14px;

}

</style>

""", unsafe_allow_html=True)




# Session page control
if "page" not in st.session_state:

    st.session_state.page = "login"



users = load_users()



# ---------------- REGISTER PAGE ----------------

if st.session_state.page == "register":


    st.markdown("<div class='box'>", unsafe_allow_html=True)


    st.title("Register")


    email = st.text_input("Email")

    password = st.text_input("Password", type="password")



    if st.button("Register"):


        if email == "" or password == "":

            st.markdown("<p class='red'>* Fill all fields</p>", unsafe_allow_html=True)


        elif email in users:

            st.markdown("<p class='red'>* Email already exists</p>", unsafe_allow_html=True)


        else:

            users[email] = password

            save_users(users)


            st.success("Register Successfully")


            st.session_state.page = "login"

            st.rerun()



    if st.button("Go to Login"):

        st.session_state.page = "login"

        st.rerun()



    st.markdown("</div>", unsafe_allow_html=True)




# ---------------- LOGIN PAGE ----------------

if st.session_state.page == "login":


    st.markdown("<div class='box'>", unsafe_allow_html=True)


    st.title("Login")


    email = st.text_input("Email")

    password = st.text_input("Password", type="password")


    error = ""


    if st.button("Sign In"):


        if email == "" or password == "":

            error = "* Enter Email and Password"


        elif email not in users:

            error = "* Email not registered"


        elif users[email] != password:

            error = "* Incorrect Password"


        else:

            st.success("Login Successful")

            st.stop()



    if error:

        st.markdown(f"<p class='red'>{error}</p>", unsafe_allow_html=True)




    st.write("Don't have account?")


    if st.button("Sign up"):

        st.session_state.page = "register"

        st.rerun()



    st.markdown("</div>", unsafe_allow_html=True)
