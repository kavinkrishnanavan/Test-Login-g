import streamlit as st
import tempfile
from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
st.write(st.secrets["o"])
# Read the literal JSON string
json_str = st.secrets["o"]

# Write to a temp file
with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
    f.write(json_str)
    f.flush()
    temp_file_path = f.name

flow = InstalledAppFlow.from_client_secrets_file(temp_file_path, SCOPES)
credentials = flow.run_local_server(port=0, open_browser=False)

st.write("Logged in successfully!")

