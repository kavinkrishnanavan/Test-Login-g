import streamlit as st
import tempfile
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/userinfo.profile']

# Read Google client secrets JSON string from Streamlit secrets
json_str = st.secrets["o"]

# Write JSON string to a temp file
with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
    f.write(json_str)
    f.flush()
    temp_file_path = f.name

# OAuth flow
flow = InstalledAppFlow.from_client_secrets_file(temp_file_path, SCOPES)
credentials = flow.run_local_server(port=0)

# Use Google People API to get user profile info
people_service = build('people', 'v1', credentials=credentials)
profile = people_service.people().get(resourceName='people/me', personFields='names').execute()

# Extract display name
names = profile.get('names', [])
display_name = names[0].get('displayName') if names else "Unknown"

st.write(f"Welcome, {display_name}!")
