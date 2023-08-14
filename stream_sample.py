import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="Main Page",
    page_icon=":house:",
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
conn = st.experimental_connection("sql")
df = conn.query("select * from pet_owners")
st.dataframe(df)
datas.title('Home Page')
Login = datas.button('Login')
Register = datas.button('Register')
if Login:
    switch_page('Login')
elif Register:
    switch_page('Register')
else:
    st.session_state.page=False
