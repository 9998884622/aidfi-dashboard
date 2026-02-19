```python
import firebase_admin

from firebase_admin import credentials,storage,db

import streamlit as st


if not firebase_admin._apps:

    cred=credentials.Certificate(dict(st.secrets["FIREBASE"]))

    firebase_admin.initialize_app(

        cred,

        {

        "storageBucket":st.secrets["FIREBASE"]["project_id"]+".appspot.com",

        "databaseURL":"https://"+st.secrets["FIREBASE"]["project_id"]+"-default-rtdb.firebaseio.com/"

        }

    )


bucket=storage.bucket()

ref=db.reference("intruder")


def upload_image(path,name):

    blob=bucket.blob(name)

    blob.upload_from_filename(path)


def save_location(user,lat,lng):

    ref.child(user).set({

    "lat":lat,

    "lng":lng

    })


def get_images():

    blobs=bucket.list_blobs()

    urls=[]

    for blob in blobs:

        urls.append(blob.public_url)

    return urls


def get_locations():

    return ref.get()
```
