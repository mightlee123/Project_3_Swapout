import streamlit as st
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any



st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.blackenterprise.com/wp-content/blogs.dir/1/files/2020/04/iStock-1125604286.jpg")
    }
.sidebar-content {
        background: url("https://www.pngkit.com/png/detail/336-3367267_reset-icon-transparent-refresh-icon-blue.png")
    }
    <\style>
    """,
    unsafe_allow_html=True
)

st.write("## Please enter your SWAPOUT Account Information")


input_data = st.text_input("User ID")
input_data = st.text_input("Password")

st.button('Log In') #== True:
   # webbrowser.open_new_tab('http://localhost:8085/')