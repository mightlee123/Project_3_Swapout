 import os 
import json
import streamlit as st
from eth_account import account
from eth_typing.evm import Address
from tensorflow.python.framework.dtypes import as_dtype
from tensorflow.python.ops.gen_math_ops import bucketize
from tensorflow.python.ops.gen_string_ops import string_format
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from web3 import Web3
import streamlit as st
from bip44 import Wallet
from web3 import Account
from mnemonic import Mnemonic
    
    
    if st.button('Finalize Registration'):
        if mnemonic is None:
            mnemo = Mnemonic("english")  
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



    # trasaction of deal not sing up 
      # contract address for now   
    def sol_function_cal():
        accounts = w3.eth.accounts
        account = accounts[2]
        proprietor = st.text_input('Enter your digital address')
        collectable_details = st.text_input("Deed Details", value="Deed To Collectable")
        token_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1) 
        
        if st.button('New Deed'):
            itm_hash = contract.functions.deedForItem(proprietor, collectable_details).transact({'from' : account, 'to' : proprietor,  'gas': 2812493})
            print(itm_hash)
            print("hello")
            
            token_owner = contract.functions.ownerOf(token_id).transact({'from' : account, 'to' : proprietor})
            st.write(f"The Swap Deed Owner {token_owner}")
        
            token_uri = contract.functions.tokenURI(token_id).transact({'from' :account, "to" : proprietor})
            st.write(f"The Deed's tokenURI metadata is {token_uri}")
            print("champ shit")

            balanceOf = contract.functions.balanceOf(proprietor).transact({'from' :account, "to" : proprietor})

            st.write(f"Balance {balanceOf}")
            print(balanceOf)
            print("champ shit")


sol_function_cal()


    #receiver = st.text_input('Input item information')

    message_seller = st.text_input('Write a message to the lister of the item, Dont share sensetive info')

contact_seller()
