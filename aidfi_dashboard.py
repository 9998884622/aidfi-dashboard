import streamlit as st
import json
import os

# ---------- SETTINGS ----------

st.set_page_config(page_title="AIDFI Dashboard", layout="centered")

USERS_FILE = "users.json"
REPORTS_FOLDER = "reports"


# ---------- CREATE FILES IF NOT EXIST ----------

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

if not os.path.exists(REPORTS_FOLDER):
    os.makedirs(REPORTS_FOLDER)


# ---------- BACKGROUND ----------

def set_bg():

    bg_url = "https://raw.githubusercontent.com/9998884622/aidfi-dashboard/main/images/bg.jpg"

    st.markdown(f"""
    <style>

    .stApp {{
    background-image: url("{bg_url}");
    background-size: cover;
    }}

    .box {{
    background: rgba(0,0,0,0.7);
    padding: 30px;
    border-radius: 15px;
    color: white;
    }}

    </style>
    """, unsafe_allow_html=True)

set_bg()


# ---------- LOAD USERS ----------

def load_users():

    with open(USERS_FILE) as f:
        return json.load(f)


def save_users(users):

    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


# ---------- SESSION ----------

if "page" not in st.session_state:
    st.session_state.page = "login"


# ---------- REGISTER PAGE ----------

def register():

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.title("Register")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        users = load_users()

        if email in users:

            st.error("Email already exists")

        else:

            users[email] = password
            save_users(users)

            st.success("Registered Successfully")

            st.session_state.page = "login"
            st.rerun()

    st.button("Go to Login", on_click=lambda:
              st.session_state.update(page="login"))

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- LOGIN PAGE ----------

def login():

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        users = load_users()

        if email not in users:

            st.markdown(
                "<span style='color:red'>* Email not registered</span>",
                unsafe_allow_html=True
            )

        elif users[email] != password:

            st.error("Wrong password")

        else:

            st.success("Login Successful")

            st.session_state.page = "admin"
            st.rerun()

    st.button("Go to Register", on_click=lambda:
              st.session_state.update(page="register"))

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- ADMIN PAGE ----------

def admin():

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.title("Admin Upload")

    file = st.file_uploader("Upload Report")

    if st.button("Upload"):

        if file:

            path = os.path.join(REPORTS_FOLDER, file.name)

            with open(path, "wb") as f:
                f.write(file.read())

            st.success("Uploaded Successfully")

            st.session_state.page = "output"
            st.rerun()

    st.button("Logout", on_click=lambda:
              st.session_state.update(page="login"))

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- OUTPUT PAGE ----------

def output():

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.title("Reports")

    files = os.listdir(REPORTS_FOLDER)

    if files:

        for file in files:

            st.write(file)

            with open(os.path.join(REPORTS_FOLDER, file), "rb") as f:

                st.download_button(
                    "Download",
                    f,
                    file_name=file
                )

    else:

        st.write("No reports found")

    st.button("Back", on_click=lambda:
              st.session_state.update(page="admin"))

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- PAGE CONTROL ----------

if st.session_state.page == "login":

    login()

elif st.session_state.page == "register":

    register()

elif st.session_state.page == "admin":

    admin()

elif st.session_state.page == "output":

    output()
