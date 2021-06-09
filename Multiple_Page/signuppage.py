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
import pandas as pd
from path import Path
<<<<<<< Updated upstream
#from data_to_csv import general_info, private_info
=======
from PIL import Image
from Image_Storage import save_image
>>>>>>> Stashed changes

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

# Creating 3 Subsections for the Sign Up Page
header = st.beta_container()
personal_info = st.beta_container()
vehicle_info = st.beta_container()
wallet_info = st.beta_container()

# Creating the 2 Buttons: Cancel and Finalize Registration
prev, _ ,next = st.beta_columns([1, 2, 1])

# next.button("Finalize Registration")

if prev.button("Cancel") == True:
    webbrowser.open_new_tab('http://localhost:8086/')

# Placing a title in the Header Subsection
with header:
    st.write("## Let's create your SWAPOUT Account!")

# Collecting the User's Personal Information on the Sign Up Page
with personal_info:
    st.write("Personal Information")

    first, last = st.beta_columns(2)

    first_name = first.text_input("First Name")
    last_name = last.text_input("Last Name")

    email_address = st.text_input("Email Address")

    mailing_address = st.text_input('Mailing Address')

    password, confirmpassword = st.beta_columns(2)

    password = password.text_input("Password", type="password")
    confirm_password = confirmpassword.text_input("Confirm Password", type="password")

# Collecting the User's Vehicle Information on the Sign Up Page
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

# The user will create their wallet address, and account address.
with wallet_info:

    
    if st.button("Create Digital Address") == True:

        while mnemonic is None:
            mnemonic = mnemonic.generate(strength=128)
        mnemonic_seed_phrase = st.write(f"<link of/OR info about seed fphrases {mnemonic}")
        wallet = Wallet(mnemonic)
        wallet_obj = st.write(f"<link of/OR info about seed fphrases {wallet}")
        private, public = wallet.derive_account('eth')
        st.write(private)
        account = Account.privateKeyToAccount(private)
<<<<<<< Updated upstream
        st.write(account.address)
=======
        st.write(
            f"""{account.address} <----- This is the address associated with your new Ethereum account.
            We are using this address to store all your tokenized collectables and swaped for collectables on the Ethereum blockchain.""")

    def sol_function_cal():
        proprietor =  account_address
        contract_sender = st.text_input('Enter the contract sender')
        tokenURI =  st.text_input('enter tokenURI')
        #c_add  = st.write(eval("enter add"))
        # if proprietor == True:
        receipt = False
        if st.button('New Deed'):
            print("I'm HERE")
            itm_hash = contract.functions.deedForItem(
                proprietor,
                tokenURI
            ).transact({'to' : proprietor, 'from' : contract_sender, 'gas': 1000000})
            receipt = w3.eth.waitForTransactionReceipt(itm_hash)
        print(f'{contract_sender, receipt}')


if next.button("Finalize Registration") == True:
    # pulls the general info of the users and saves it to a dataframe(csv)
    general_info_list = []
    general_info_list.append({"First Name": first_name, "Last Name": last_name, "Email": email_address, "Year": year, "Make": make, "Model": model, "Miles": miles, "Certification": certification})
    Path="../Project3_practice/general_info_df.csv"
    general_info_df=pd.DataFrame(general_info_list)
    general_info_df.to_csv(Path)


    # pulls the private info of the users and saves it to a dataframe(csv)
    private_info_list = []
    private_info_list.append({"Password": confirm_password, "Physical Address": mailing_address, "Digital Address": account_address})
    Path="../Project3_practice/private_info_df.csv"
    private_info_df=pd.DataFrame(private_info_list)
    private_info_df.to_csv(Path)

    save_image(account_address)


    # Clicking Finalize Registration will take them to the Dashboard page
    webbrowser.open_new_tab("http://localhost:8502/")
>>>>>>> Stashed changes
    
        val = ("ether") # token RUI
        def sol_function_cal():
            receiver =  st.text_input('enter receiver address')
            return receiver, #sell_side
            if receiver == True:
                    itm_hash = contract.functions.deedForItem(
                    receiver
                ).transact({'to' : receiver , 'gas': 1000000})
                    receipt = w3.eth.waitForTransactionReceipt(itm_hash)
                    print(itm_hash)
        sol_function_cal()



    if next.button("Finalize Registration") == True:
        # this fuction pulls the general info of the users and saves it to a dataframe(csv)
        def general_info():
            general_info_list = []
            general_info_list.append({"First Name": first_name, "Last Name": last_name, "Email": email_address, "Year": year, "Make": make, "Model": model, "Miles": miles, "Certification": certification})
            Path="../Project3_practice/general_info_df.csv"
            general_info_df=pd.DataFrame(general_info_list)
            general_info_df.to_csv(Path)


        # this fuction pulls the private info of the users and saves it to a dataframe(csv)
        def private_info():
            private_info_list = []
            private_info_list.append({"Email": email_address, "Password": confirm_password, "Physical Address": mailing_address, "Account Address": receiver})
            Path="../Project3_practice/private_info_df.csv"
            private_info_df=pd.DataFrame(private_info_list)
            private_info_df.to_csv(Path)

        

        # Clicking Finalize Registration will take them to the Dashboard page
        webbrowser.open_new_tab("http://localhost:8502/")