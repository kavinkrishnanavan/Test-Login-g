import streamlit as st
import tempfile
from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Read JSON secrets string from Streamlit secrets
json_str = st.secrets["o"]

# Write to a temporary JSON file
with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as temp_file:
    temp_file.write(json_str)
    temp_file.flush()
    temp_file_path = temp_file.name

# Use the temp file path for the OAuth flow
flow = InstalledAppFlow.from_client_secrets_file(temp_file_path, SCOPES)
credentials = flow.run_local_server(port=0)

st.write("Logged in with Google!")
