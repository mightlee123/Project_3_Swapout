import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import webbrowser
import pandas as pd
from path import Path
from PIL import Image

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

st.title("Welcome to your SWAPOUT Account!")
    

navigation = st.sidebar.selectbox("Dashboard", ("The Swap Meet", "Account Information", "Transactions"))

df_general_info = pd.read_csv("./general_info_df.csv")
df_private_info = pd.read_csv("./private_info_df.csv")


# Swap Meet Page within the Dashboard
if navigation == "The Swap Meet":
    st.header("Available Cars")

    image = Image.open('./Images/540i.JPG')
    image2 = Image.open('./Images/MR2.jpg')

    st.image(image, caption = "2003 BMW 540i")
    st.button("Make Offer")

    st.image(image2, caption = "1986 Toyota MR2")
    #st.button("Make Offer")

# Account Information Page within the Dashboard
if navigation == "Account Information":

    # Display Personal Information
    st.header("Personal Information")

    
    #first, last = st.beta_columns(2)

    first = st.write('First Name:', df_general_info["First Name"])
    last = st.write('Last Name:', df_general_info["Last Name"])

    email_address = st.write(df_general_info["Email"])

    mailing_address = st.write(df_private_info["Physical Address"])


    # Display Vehicle Information
    st.header("Vehicle Information")

    first, last = st.beta_columns(2)

    make = first.text_input("Make")

    model = last.text_input("Model")

    first, last = st.beta_columns(2)

    year = first.text_input("Year")

    miles = last.text_input("How many miles does your car have?")

    certification = st.text_input("Certification")

    # Logout Button will return them to the Home Page
    if st.button("Logout") == True:
        webbrowser.open_new_tab('http://localhost:8501/')

if navigation == "Transactions":
    # Display Pending Transactions
    st.header("Pending Transactions")

    # Display Previous Transactions
    st.header("Previous Transactions")