import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pydantic import BaseModel, SecretStr
import streamlit_pydantic as sp

class Register():

    def __init__():
        st.set_page_config(
            page_title="Register",
            page_icon=":blossom:",
            # layout="wide",
            initial_sidebar_state="expanded"
        )


    def validate(pwd, pwd1):
        if pwd != pwd1:
            st.error('Enter a password and ReEnter password as Same')
        else:
            pass

    def Register():
        datas = st.container()
        datas.title('Register')
        name = datas.text_input('Name','')
        password = datas.text_input('Password','',type='password')
        password2 = datas.text_input('ReEnter a Password','',type='password')
        if password and password2:
            validate(password,password2)
        else:
            if password or password2:
                st.error('Please Enter a Password Field dont missout Password or ReEnter a Password')
        datas.radio('Gender',['Male','Female'])
        number = datas.text_input('Phone Number :telephone:','',max_chars=10)
        if number:
            if not number.isdigit():
                datas.warning('Enter a Valid number')
        Submit = datas.button('Submit')
        Home = datas.button('Home')
        if Submit:
            switch_page('Login')
        if Home:
            switch_page('stream_sample')

if __name__=='__main__':
    st.markdown("""
        <style>
            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }
        </style>
        """, unsafe_allow_html=True)
    Register.Register()
