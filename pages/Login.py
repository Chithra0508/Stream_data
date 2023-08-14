import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pydantic import BaseModel, SecretStr
import streamlit_pydantic as sp

class Pages():

    st.set_page_config(
        page_title="Login",
        page_icon=":sparkles:",
        # layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown("""
        <style>
            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }
        </style>
        """, unsafe_allow_html=True)


    datas = st.container()

    class ExampleModel(BaseModel):
        User_Name: str
        User_Password: SecretStr
    data = sp.pydantic_form(key="my_form", model=ExampleModel)
    if data:
        datas.json(data.json())
    Register = st.button('Register')
    Home = st.button('Home')
    if Register:
        switch_page('Register')
    if Home:
        switch_page('stream_sample')
