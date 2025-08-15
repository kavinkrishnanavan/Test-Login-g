import streamlit as st

st.write(st.secrets)

def main():
    if not st.user.is_logged_in:
        st.header("Login Required")
        st.button("Log in with Google", on_click=st.login)
        st.stop()  # Stop the rest of the app until logged in
    
    # Once logged in
    st.header(f"Welcome, {st.user.name}!")
    st.write(f"Your email is: {st.user.email}")

    if st.button("Log out"):
        st.logout()
        st.experimental_rerun()

if __name__ == "__main__":
    main()
