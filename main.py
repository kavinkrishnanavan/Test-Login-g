import streamlit as st
import tempfile
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
json_str = st.secrets["o"]

with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
    f.write(json_str)
    f.flush()
    temp_file_path = f.name

flow = InstalledAppFlow.from_client_secrets_file(temp_file_path, SCOPES)
auth_url, _ = flow.authorization_url(prompt='consent')

st.write("Please open this URL in your browser to authorize:")
st.write(auth_url)

# Now run_local_server without opening the browser to wait for redirect
credentials = flow.run_local_server(port=0, open_browser=False)

st.write("Login successful!")
st.write(f"Access token: {credentials.token}")
