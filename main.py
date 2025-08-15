import streamlit as st

if st.button("Authenticate"):

    st.login("google")

    st.write("😇🤮😵‍💫")

st.write(st.user["name"])
