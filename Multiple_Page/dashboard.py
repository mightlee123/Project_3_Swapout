import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import webbrowser
import pandas as pd
from path import Path

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

df = pd.read_csv("./user_enteries_df.csv")

# The Swap Meet Page within the Dashboard. Also the landing page after Registration & Log In.
if navigation == "The Swap Meet":
    st.header("Listings")


# Account Information Page within the Dashboard
if navigation == "Account Information":

    # Display Personal Information
    st.header("Personal Information")

    
    first, last = st.beta_columns(2)

    first_name = first.text_input("First Name")
    last_name = last.text_input("Last Name")

    email_address = st.text_input("Email Address")

    mailing_address = st.text_input('Mailing Address')


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


# Transactions Page within the Dashboard
if navigation == "Transactions":
    # Display Pending Transactions
    st.header("Pending Transactions")

    # Display Previous Transactions
    st.header("Previous Transactions")