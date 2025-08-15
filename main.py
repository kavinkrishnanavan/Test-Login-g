import streamlit as st

st.button("Authenticate" , onclick=st.login("google"))


st.write(st.user["name"])
