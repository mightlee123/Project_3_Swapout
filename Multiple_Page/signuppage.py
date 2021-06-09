import os, sys
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
from PIL import Image
from Image_Storage import save_image

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


    account_address = st.text_input("Enter your Account Address")


@st.cache
def load_image (image_file):
    img = Image.open(image_file)
    return img
def main():
    # st.title ("File Uploads & Saved File to Directory App")
    # menu = ["Home"]
    # choice = st.sidebar.selectbox("Menu", menu)
    # if choice == "Home":
        # st.subheader("Upload Image")
        # user_name =
        image_file = st.file_uploader("Upload An Image",type=['jpg'])
        if image_file is not None:
            file_details = {"FileName":image_file.name, "FileType":image_file.type}
            #st.write(type(image_file))
            img = load_image(image_file)
            st.image(img)
            save_path = '/Users/ayechan/Desktop/Project_3_Swapout/jpg'
            file_name = "{account_address}.jpg"
            #new_file_name = user_name 
            completeName = os.path.join(save_path, file_name)
            with open(completeName, "wb") as f:
                f.write(image_file.getbuffer())
                ##renaming image file
                # os.rename(file_name, user_name)
            st.success("File Saved")
if __name__ == '__main__':
    main()

# The user will create their wallet address, and account address.
with wallet_info:

    
    if st.button("Create Digital Address") == True:

        if mnemonic is None:
            mnemo = mnemonic("english")  
            mnemonic = mnemo.generate(strength=256)
        mnemonic_seed_phrase = st.write(
            f"""This is your Mnemonic seed phrase.
            Do not share with anyone.
            When used in sequence it will  allow access to the wallet we've just created for you.
            ---> {mnemonic}""")
        wallet = Wallet(mnemonic)
        wallet_obj = st.write(
            f""" With the help of the bip44 package and your Mnemonic seed phrase
            we created this universal wallet instance.
            {wallet}""")
        private, public = wallet.derive_account('eth')
        st.write(
            f"""{private} <-----
            This is an encoded represantiation of your private key and the only way you should store in your device""")
        account = Account.privateKeyToAccount(private)
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


