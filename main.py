import streamlit as st

from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
flow = InstalledAppFlow.from_client_secrets_file('secrets.toml', SCOPES)
credentials = flow.run_local_server(port=0)

st.write("Test 123")
