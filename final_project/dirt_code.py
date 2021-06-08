
import os
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

from crypto_wallet import generate_account
from crypto_wallet import get_balance
from crypto_wallet import send_transaction 

st.button('Create a listing with us') 
True = 'Yes'
False = 'No'
if st.buttton ('Create a listing with us') == True:    

    def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
        mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
        wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
        private, public = wallet.derive_account("eth")

        account = Account.privateKeyToAccount(private)

        return account

    # we would have to append the acount to our database 



 
        prev_block = pychain.chain[-1]
        prev_block_hash = prev_block.hash_block()

def listing_database


listing_database = {
    "Transformer": ["Transformer", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/0b228b2c-3a14-472e-a3fa-0ed6c0feab95.a8be9b92a81864dcda0af0b90a033ae1"],
    "Toys": ["Toys", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/1140-collectibles-old-toys.web.jpeg"],
    "Pokemon": ["Pokemon", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/colect_pokemon.jpeg"],
    "Hero": ["Hero", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/hero-D23A7W.jpeg"]
}

# A list of the FinTech Finder candidates first names
item_list = ["Transformer", "Toys", "Pokemon", "Hero"]


# Delete the `input_data` variable from the Streamlit interface.
#input_data = st.text_input("Block Data")
   # Convert private key into an Ethereum account

newaccount = get_balance(account.address)

st.sidebar.write(f'This is your new accout adrres {newaccount} with us')  


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

selection = st.sidebar.selectbox('Select an Item', item_list)

offer = st.sidebar.number_input("Offer for item")

st.sidebar.markdown("## Item Name, Item Rate, and Ethereum Address")

# @TODO:
# Add an input area where you can get a value for `sender` from the user.
# YOUR CODE HERE
sender = st.text_input('Input sender information')

# @TODO:
# Add an input area where you can get a value for `receiver` from the user.
# YOUR CODE HERE
receiver = st.text_input('Input receiver information')

# @TODO:
# Add an input area where you can get a value for `amount` from the user.
# YOUR CODE HERE
amount = st.text_input('Enter amount')

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # @TODO
    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`,
    # and `amount` values
    new_block = Block(
        record=Record(sender, receiver, amount),
        #data=input_data,
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()


