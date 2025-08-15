import streamlit as st

if st.button("Authenticate"):

    st.login("google")

    st.write("😇🤮😵‍💫")

if st.user["name"] == "":

    st.write("Name not defined")

else:

    st.write(st.user["name"])


