
import os
from eth_utils.decorators import T
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.auto.infura.kovan import w3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

from eth_account import account
import streamlit as st
from dataclasses import dataclass
from typing import Any, List


from crypto_wallet import get_balance
#from crypto_wallet import send_transaction 
#from crypto_wallet import creation_button 
from crypto_wallet import contact_seller

##########################################

listing_database = {
    "Transformer": ["Transformer", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/0b228b2c-3a14-472e-a3fa-0ed6c0feab95.a8be9b92a81864dcda0af0b90a033ae1.jpeg"],
    "Toys": ["Toys", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/1140-collectibles-old-toys.web.jpg"],
    "Pokemon": ["Pokemon", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/colect_pokemon.jpg"],
    "Hero": ["Hero", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/hero-D23A7W.jpg"]
}

item_list = ["Transformer", "Toys", "Pokemon", "Hero"] 




def create_account(): 
    user_input = st.selectbox("Would you like to create an account",    
        ['Choose option' ,'Yes', 'Not at this moment'])

    if  user_input  == ('Yes'):
        mnemonic = os.getenv("MNEMONIC")
        wallet = Wallet(mnemonic)
        private, public = wallet.derive_account("eth")
        account = Account.privateKeyToAccount(private)
        st.write(f'This is your new Ether adrres {account.address} with us')  

    elif user_input == ('Not at this moment'):
        st.write("Dont delay too long.")
           
create_account()


def select_item(): 
     """Display the database of Fintech Finders candidate information."""
     db_list = list(listing_database.values())

     for number in range(len(item_list)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Swapout item Rating: ", db_list[number][2])
        st.write("Price per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

select_item()


def contact_seller():

    #sender = st.text_input('Input your account address')

    #receiver = st.text_input('Input item information')

    message_seller = st.text_input('Write a message to the lister of the item, Dont share sensetive info')

contact_seller()
