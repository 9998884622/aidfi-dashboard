import streamlit as st
import firebase_config as fb

st.title("Threat Analysis")

# check login
if "user" not in st.session_state:

    st.warning("Please Login First")

else:

    file = st.file_uploader("Upload File")

    lat = st.text_input("Enter Latitude")

    lng = st.text_input("Enter Longitude")

    if st.button("Scan"):

        if file:

            # save file
            fb.upload_file(file.name, file.name)

            # save location
            if lat and lng:

                fb.save_location(st.session_state.user, lat, lng)

            st.error("Threat Detected")

            st.success("Saved Successfully")
