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
    """, unsafe_allow_h
