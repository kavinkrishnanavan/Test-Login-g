
import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        # Streamlit uses your secrets.toml to do OAuth flow internally
        st.login()
    st.stop()

st.write(f"Welcome, {st.user.name}!")
if st.button("Log out"):
    st.logout()
    st.experimental_rerun()
