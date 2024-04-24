import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from function import insert_user
import re

def signup():
    # if 'show_signup' not in st.session_state:
    #     st.session_state.show_signup = False
    # if 'signup_completed' not in st.session_state:
    #     st.session_state.signup_completed = False

    # if st.session_state.show_signup:
    with st.form('signupform',clear_on_submit=False):
        st.write("<h2>Sign Up</h2>", unsafe_allow_html=True)
        first_name = st.text_input(' ', placeholder='First Name', max_chars=20 )
        last_name = st.text_input(' ', placeholder='Last Name', max_chars=20 )
        email = st.text_input(' ', placeholder='Email', max_chars=80)
        password = st.text_input(' ', placeholder='Password', type="password")
        signuped = st.form_submit_button('Submit')

    if signuped:
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if(len(email)==0 or len(password)==0 or len(first_name)==0 or len(last_name)==0):
            if len(email)==0:
                st.error('Username field is empty')
            if len(password)==0:
                st.error('Password field is empty')
        elif not re.fullmatch(regex, email):
            st.error('The provided email is incorrect. Example: example@domain.com')
        else:
            st.session_state.logged_in = True
            st.success("Signup successful, you can now login")
        

if __name__ == "__main__":
    signup()
    