
Delete everything.

Paste this ONLY:

```python
import streamlit as st
import firebase_admin
from firebase_admin import credentials, storage, db

if not firebase_admin._apps:

    cred = credentials.Certificate({
        "type": st.secrets["FIREBASE_TYPE"],
        "project_id": st.secrets["FIREBASE_PROJECT_ID"],
        "private_key_id": st.secrets["FIREBASE_PRIVATE_KEY_ID"],
        "private_key": st.secrets["FIREBASE_PRIVATE_KEY"],
        "client_email": st.secrets["FIREBASE_CLIENT_EMAIL"],
        "client_id": st.secrets["FIREBASE_CLIENT_ID"],
        "token_uri": st.secrets["FIREBASE_TOKEN_URI"]
    })

    firebase_admin.initialize_app(cred, {
        "storageBucket": "aidfi-492df.appspot.com",
        "databaseURL": "https://aidfi-492df-default-rtdb.firebaseio.com/"
    })
