import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import webbrowser



st.title("Welcome to Swapout!")

st.markdown("## Your customized virtual market place")

#background picture
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

left_column, right_column = st.beta_columns(2)

# left_column.button('Sign Up')

if left_column.button('Sign Up') == True:
    webbrowser.open_new_tab('http://localhost:8087/')


if right_column.button('Log In') == True:
    webbrowser.open_new_tab('http://localhost:8085/')
