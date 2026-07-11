import streamlit as st 
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    
    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()  
    
#teacher login screen       
def teacher_screen_login():
    col1,col2 = st.columns(2,gap="xxlarge")
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home",type="secondary",key="loginbackbtn",shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    st.header("Login using password",text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("enter username",placeholder="@anil")
    teacher_pass = st.text_input("Enter password",type="password",placeholder="enter your password")
    st.divider()
    btncol1,btncol2 = st.columns(2)
    with btncol1:
        if st.button("Login",icon=":material/passkey:",shortcut="control+enter",width="stretch"):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()
    with btncol2:
        if st.button("Register instead",icon=":material/passkey:",width="stretch",type="primary"):
            st.session_state['teacher_login_type'] = 'register'
            st.rerun() 
    footer_dashboard()



#teacher register screen
def teacher_screen_register():
    col1,col2 = st.columns(2,gap="xxlarge")
    with col1:
        header_dashboard()
    with col2:
         if st.button("Go back to Home",type="secondary",key="loginbackbtn",shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    st.header("Register your teacher profile",text_alignment="center")
    
    st.space()
    st.space()
    teacher_username = st.text_input("Enter your username",placeholder="@anil")
    teacher_name = st.text_input("Enter your fullname",placeholder="Anil Sethy")
    teacher_pss = st.text_input("Enter your password",type="password",placeholder="enter your password")
    teacher_pass_confirm = st.text_input("Confirm your password",type="password",placeholder="enter confirm password")
    st.divider()
    btncol1,btncol2 = st.columns(2)
    with btncol1:
        st.button("Register now",icon=":material/passkey:",shortcut="control+enter",width="stretch")
           
    with btncol2:
        if st.button("Login instead",icon=":material/passkey:",width="stretch",type="primary"):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()
           
    footer_dashboard()
   
   