import streamlit as st
import requests
import zipfile
import io
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# 🔹 Google Drive authentication
@st.cache_resource
def connect_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # First time opens browser for auth
    return GoogleDrive(gauth)

drive = connect_drive()

# Replace with your shared folder ID
FOLDER_ID = "1W7ecBMXSIHGVEEKZIkYqFZmHGx3miHk5"

# 🔹 Fetch all files from the folder
@st.cache_data(ttl=60)
def list_files(folder_id):
    query = f"'{folder_id}' in parents and trashed=false"
    return drive.ListFile({'q': query}).GetList()

files = list_files(FOLDER_ID)

st.title("📸 Friends Group Photo Dashboard (Google Drive)")

if not files:
    st.warning("No photos found in Google Drive folder.")
else:
    persons = sorted(set([f['title'].split("_")[0] for f in files]))
    person = st.selectbox("Choose a Person", persons)

    st.subheader(f"📂 Showing Photos for: {person}")

    selected_files = [f for f in files if f['title'].startswith(person + "_")]

    if selected_files:
        for f in selected_files:
            download_url = f['alternateLink']
            st.image(f['thumbnailLink'], caption=f['title'], use_column_width=True)
            st.markdown(f"[🔽 Download {f['title']}]({download_url})", unsafe_allow_html=True)

        # 🔹 Option to download all as ZIP
        if st.button("Download All My Photos (ZIP)"):
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zipf:
                for f in selected_files:
                    content = requests.get(f['downloadUrl']).content
                    zipf.writestr(f['title'], content)
            st.download_button(
                label="💾 Download ZIP",
                data=zip_buffer.getvalue(),
                file_name=f"{person}_photos.zip",
                mime="application/zip"
            )
    else:
        st.warning("No photos found for this person.")
