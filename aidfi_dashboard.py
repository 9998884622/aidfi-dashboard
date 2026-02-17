import streamlit as st

st.set_page_config(page_title="AIDFI Cyber", layout="wide")

st.title("🛡 AIDFI – AI Digital Forensics Investigator")

st.sidebar.title("Control Panel")

file = st.sidebar.file_uploader("Upload Log File")

if file:

    data = file.read().decode()

    st.subheader("Investigation Dashboard")

    if "failed" in data.lower():

        st.error("🔴 Threat Level: HIGH")

        st.write("Attack Type: Brute Force Attack")

        st.write("AI Investigator: Multiple login failures detected")

    elif "unauthorized" in data.lower():

        st.warning("🟠 Threat Level: MEDIUM")

    else:

        st.success("🟢 Threat Level: SAFE")

    report = "AIDFI Cyber Forensic Report Generated"

    st.download_button("Download Report", report)
