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

load_dotenv()
mnemonic = os.getenv("MNEMONIC")


w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./contracts/compiled/generalReg_abi.json')) as f:
        generalReg_abi = json.load(f)

    contract_address = os.getenv('SMART_CONTRACT_ADDRESS')

    contract = w3.eth.contract(
        address=contract_address,
        abi=generalReg_abi
)
    return contract

contract = load_contract()



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

#adding navigator to sidebar(testing)
import pickle as pkle
import os.path

# # create a button in the side bar that will move to the next page/radio button choice
# next = st.sidebar.button('Next on list')

new_choice = ['Home','Gallery','About']
if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(new_choice):
        next_clicked = 0 
else:
    next_clicked = 0 #the start

if next:
    next_clicked = next_clicked +1
    if next_clicked == len(new_choice):
        next_clicked = 0 # go back to the beginning i.e. homepage

choice = st.sidebar.radio("go to",('Home', 'Gallery', 'About'), index=next_clicked)
pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

if choice == 'Home':
    st.write('this is home')
elif choice == 'Gallery':
    st.write('A Gallery of some sort')
elif choice == 'About':
    st.write('About page')

left_column, right_column = st.beta_columns(2)
left_column.button('New User')
    # input_data = st.text_input("Create User ID")    
    # input_data = st.text_input("Enter personal number")
    # input_data = st.text_input("Confirm personal number")     
    # left_column.button("Sign Up!")
header = st.beta_container()
personal_info = st.beta_container()
vehicle_info = st.beta_container()

prev, _ ,next = st.beta_columns([1, 8, 1])

next.button("Next")

prev.button("Previous")

with header:
    st.write("## Let's create your SWAPOUT Account!")
    
with personal_info:
    st.write("Personal Information")

    first, last = st.beta_columns(2)
    
    first.text_input("First Name")
    last.text_input("Last Name")

    st.text_input("Email Address")

    password, confirmpassword = st.beta_columns(2)

    password.text_input("Password", type="password")
    confirmpassword.text_input("Confirm Password", type="password")

    
    st.write("Vehicle Information")

    year = st.selectbox("What year is your car?", options = range(2021, 1949, -1))
         
    make = st.selectbox("What make is your vehicle?", options = ["Acura", "Alfa Romeo", "AMC", "Aston Marton", "Audi", "Bentley", "BMW", "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Citroen", "Datsun", "Daewoo", "Delorean", "Dodge", "Eagle", "Ferarri", "FIAT", "Fisker", "Ford", "Freightliner", "Genesis", "Geo", "GMC", "Honda", "HUMMER", "Hyundai", "INFINITI", "Isuzu", "Jaguar", "Jeep", "Karma", "Kia", "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Lotus", "LUCID", "Maserati", "Maybach", "MAZDA", "McLaren", "Mercedes-Benz", "Mercury", "MINI", "Mitsubishi", "NIO", "Nissan", "Oldsmobile", "Opel", "Peugot", "Plymouth", "Pontiac", "Porsche", "RAM", "Renault", "Rolls-Royce", "Saab", "Saturn", "Scion", "Skoda", "smart", "SRT", "Studebaker", "Subaru", "Suzuki", "Tesla", "Toyota", "Vauzhall", "Volkswagen", "Volvo", "Yugo"])

    model = st.text_input("What model is your car?")

    miles = st.text_input("How many miles does your car have?")

    certification = st.radio("Does your car have any aftermarket parts?", ("Yes", "No"))
        
    price =  st.text_input("In USD name your price?")

    #date = datetime.date.today()

    tokenURI = (f"{year,model,certification,make,miles}")

    content = (year, make , model, miles)

           # # adding value of the vehicle
        # value = st.slider(
        # 'Select a range of values',
        # 0.0, 100.0, (25.0, 75.0)

        # adding file upoader
    uploaded_files = st.file_uploader("Upload Images Here", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)

            st.button('Finalize Registration')
            
            while mnemonic is None:
                mnemo = mnemonic('english')
            mnemonic = mnemo.generate(strength=128)        

            st.write(mnemonic)

            wallet = Wallet(mnemonic)
            st.write(wallet) 

            private, public = wallet.derive_account('eth')

            st.write(private, public)

            account = Account.privateKeyToAccount(private)

            owner = st.write(account.address)


            itm_hash = contract.functions.registerItem(owner, content, price, tokenURI)



if right_column.button('Existing User'):
    input_data = st.text_input("Enter User ID")
    input_data = st.text_input("Enter personal number")

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'Select car make',
#     ('Chevrolet', 'Porsche', 'BMW')
# )

# add_selectbox = st.sidebar.selectbox(
#     'Select the year',
#     ('1960','1970','1980')
# )
