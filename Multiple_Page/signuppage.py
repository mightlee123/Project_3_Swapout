import os 
import json
from eth_account import account
from eth_typing.evm import Address
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from datetime import datetime
from typing import Any
#Import the Web3 library
from web3 import Web3
import streamlit as st
from bip44 import Wallet
from web3 import Account
import webbrowser

load_dotenv()
mnemonic = os.getenv("MNEMONIC")



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

header = st.beta_container()
personal_info = st.beta_container()
vehicle_info = st.beta_container()

prev, _ ,next = st.beta_columns([1, 2, 1])

next.button("Finalize Registration")

if prev.button("Cancel") == True:
    webbrowser.open_new_tab('http://localhost:8086/')

with header:
    st.write("## Let's create your SWAPOUT Account!")

with personal_info:
    st.write("Personal Information")

    first, last = st.beta_columns(2)

    first.text_input("First Name")
    last.text_input("Last Name")

    st.text_input("Email Address")

    st.text_input('Mailing Address')

    password, confirmpassword = st.beta_columns(2)

    password.text_input("Password", type="password")
    confirmpassword.text_input("Confirm Password", type="password")


with vehicle_info:
    st.write("Vehicle Information")

    year = st.selectbox("What year is your car?", options = range(2021, 1949, -1))

    make = st.selectbox("What make is your vehicle?", options = ["Acura", "Alfa Romeo", "AMC", "Aston Marton", "Audi", "Bentley", "BMW", "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Citroen", "Datsun", "Daewoo", "Delorean", "Dodge", "Eagle", "Ferarri", "FIAT", "Fisker", "Ford", "Freightliner", "Genesis", "Geo", "GMC", "Honda", "HUMMER", "Hyundai", "INFINITI", "Isuzu", "Jaguar", "Jeep", "Karma", "Kia", "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Lotus", "LUCID", "Maserati", "Maybach", "MAZDA", "McLaren", "Mercedes-Benz", "Mercury", "MINI", "Mitsubishi", "NIO", "Nissan", "Oldsmobile", "Opel", "Peugot", "Plymouth", "Pontiac", "Porsche", "RAM", "Renault", "Rolls-Royce", "Saab", "Saturn", "Scion", "Skoda", "smart", "SRT", "Studebaker", "Subaru", "Suzuki", "Tesla", "Toyota", "Vauzhall", "Volkswagen", "Volvo", "Yugo"])

    model = st.text_input("What model is your car?")

    miles = st.text_input("How many miles does your car have?")

    certification = st.radio("Does your car have any aftermarket parts?", ("Yes", "No"))


    # adding file upoader
    uploaded_files = st.file_uploader("Upload Images Here", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

# if st.button == 'Finalize Registration':
#     while mnemonic is None:
#         mnemo = mnemonic('english')
#     mnemonic = mnemo.generate(strength=128)        
#     st.write(mnemonic)
#     wallet = Wallet(mnemonic)
#     st.write(wallet) 
#     private, public = wallet.derive_account('eth')
#     st.write(private, public)
#     account = Account.privateKeyToAccount(private)
#     owner = st.write(account.address)
#     itm_hash = contract.functions.registerItem(owner, content, price, date, tokenURI)

# if 'Finalize Registration' == True:
    
#     # DataFrame for Personal Information
#     d1 = {'First Name': ['First Name'], 
#         'Last Name': ['Last Name'],
#         'Email Address': ['Email Address'],
#         'Mailing Address' : ['Mailing Address'],
#         'Password': ['Password'],
#         'Wallet ID': ['?']}

#     df1 = df.append(d1, ignore_index = True)
#     open('df1.csv', 'w').write(df.to_csv())

#     # Dataframe for Vehicle Inofmation
#     d2 = {'Email Address': ['Email Address'],
#         'Last 8 of Wallet ID': [],
#         'Year': 'year',
#         'Make': 'make',
#         'Model': 'model',
#         'Miles': 'miles',            
#         'Certification': 'certification'}

#     st.markdown('<h3>Thank you for creating your account!</h3>', unsafe_allow_html=True)
    
#     df2 = df.append(d2, ignore_index = True)
#     open('df2.csv', 'w').write(df.to_csv())
