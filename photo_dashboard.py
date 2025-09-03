import streamlit as st

# -----------------------------
# CONFIGURATION
# -----------------------------
# Replace this with your actual Google Drive folder ID
# Example link: https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOpQrStUvWxYz?usp=sharing
FOLDER_ID = "1W7ecBMXSIHGVEEKZIkYqFZmHGx3miHk5"

# Function to build public embed link
def get_public_folder_link(folder_id):
    return f"https://drive.google.com/drive/folders/1W7ecBMXSIHGVEEKZIkYqFZmHGx3miHk5?usp=sharing"

# -----------------------------
# STREAMLIT APP
# -----------------------------
st.set_page_config(page_title="📸 Friends Photo Dashboard", layout="wide")

st.title("📸 Friends Photo Dashboard")

st.markdown("""
Welcome to your **Group Photo Dashboard**! 🎉  

**How it works:**  
1. Upload your photos into the shared Google Drive folder.  
2. This dashboard automatically shows all uploaded photos.  
3. Click any photo to open/download it in full size.  

⚡ *No need to re-upload or merge files. Just drop them in Drive and they appear here.*
""")

st.markdown("### 📂 Photo Gallery")
st.components.v1.iframe(get_public_folder_link(FOLDER_ID), width=1000, height=600)

st.info("✅ New photos added to Google Drive will appear here automatically.")



