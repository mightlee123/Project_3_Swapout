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
from web3.datastructures import T

load_dotenv()
mnemonic = os.getenv("MNEMONIC")


w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./contracts/compiled/involvedEscrow_abi.json')) as f:
        generalReg_abi = json.load(f)

    contract_address = os.getenv('SMART_CONTRACT_ADDRESS_')
    

    contract = w3.eth.contract(
        address=contract_address,
        abi=generalReg_abi
)
    return contract

contract = load_contract()






st.title("Welcome to Swapout. Smart Contracts!")

st.markdown("## Your blockchain powered virtual market place")

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

fedback = st.button('Create a Contract with us')
if fedback == True:
    _buyer = st.text_input("Enter the buyers eth address")
    _seller = st.text_input("Enter the sellers eth address")
    _price = st.text_input("Enter the amount in eth")

    #escrow_constructor = contract.constructor(_buyer, _seller, _price).call() # in ETH 

    
    initContract = st.button('Buyer Initiate Contract')
    #buyer
    initContract_sell = st.button('Seller Initiate Contract') #seller
    if initContract & initContract_sell == True:
        contract_confirm = contract.functions.initContract().call()

    ammount_eth = st.number_input("Comfirm your ETH deposit aomunt")
    if ammount_eth == True:
        contract.functions.deposit().transact()

    buyerCofimation = st.button('Confirm delivery of collectable')
    if buyerCofimation == True:
        contract.functions.confirmDelivery().transact()

    swapWithdraw = st.button('Withdraw funds and void transaction')
    if swapWithdraw == True:
        contract.functions.withdraw().transact()

    





    ## find a way to extract ammount of have them allow us to handle transaction 


    

    # way to accept and verify dosit to and from smart contract 










# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'Select car make',
#     ('Chevrolet', 'Porsche', 'BMW')
# )

# add_selectbox = st.sidebar.selectbox(
#     'Select the year',
#     ('1960','1970','1980')
# )   
