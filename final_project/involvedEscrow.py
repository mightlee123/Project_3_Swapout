import time
from six import b
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
from bip44 import Wallet
from web3 import Account
from mnemonic import Mnemonic
from web3.contract import transact_with_contract_function


load_dotenv()
mnemonic = os.getenv("MNEMONIC")

st.cache(allow_output_mutation=True)

st.title("Welcome to Swapout. Smart Contracts!")

st.markdown("## Your blockchain powered virtual market place")

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


def involvedEscrow():
    ganache_url = "HTTP://127.0.0.1:7545"

    web3 = Web3(Web3.HTTPProvider(ganache_url))

    web3.eth.defaultAccount  = web3.eth.accounts[0]

    contract_location = web3.eth.defaultAccount

    accounts = web3.eth.accounts


    bytecode = ("608060405234801561001057600080fd5b50604051610a6f380380610a6f8339818101604052606081101561003357600080fd5b8101908080519060200190929190805190602001909291908051906020019092919050505082600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550670de0b6b3a7640000810260018190555060016000806101000a81548160ff0219169083600381111561010957fe5b021790555050505061094f806101206000396000f3fe6080604052600436106100915760003560e01c80639b3bcb33116100595780639b3bcb33146101a7578063a035b1fe146101d4578063afe01043146101ff578063c4bce18014610235578063d0e30db01461026257610091565b806308551a53146100965780633ccfd60b146100d757806342842e0e146100e15780635e10177b1461015c5780637150d8ae14610166575b600080fd5b3480156100a257600080fd5b506100ab61026c565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6100df610292565b005b3480156100ed57600080fd5b5061015a6004803603606081101561010457600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061043f565b005b61016461044f565b005b34801561017257600080fd5b5061017b61061e565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101b357600080fd5b506101bc610644565b60405180821515815260200191505060405180910390f35b3480156101e057600080fd5b506101e9610657565b6040518082815260200191505060405180910390f35b34801561020b57600080fd5b5061021461065d565b6040518082600381111561022457fe5b815260200191505060405180910390f35b34801561024157600080fd5b5061024a61066e565b60405180821515815260200191505060405180910390f35b61026a610681565b005b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610338576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260258152602001806108f56025913960400191505060405180910390fd5b6002600381111561034557fe5b60008054906101000a900460ff16600381111561035e57fe5b146103d1576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601d8152602001807f43616e6e6f74207769746864726177206174207468697320737461676500000081525060200191505060405180910390fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc6001549081150290604051600060405180830381858888f19350505050158015610419573d6000803e3d6000fd5b5060036000806101000a81548160ff0219169083600381111561043857fe5b0217905550565b61044a83838361043f565b505050565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146104f5576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260258152602001806108f56025913960400191505060405180910390fd5b6002600381111561050257fe5b60008054906101000a900460ff16600381111561051b57fe5b1461058e576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260178152602001807f43616e6e6f7420636f6e6669726d2064656c697665727900000000000000000081525060200191505060405180910390fd5b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc6001549081150290604051600060405180830381858888f193505050501580156105f8573d6000803e3d6000fd5b5060036000806101000a81548160ff0219169083600381111561061757fe5b0217905550565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600060029054906101000a900460ff1681565b60015481565b60008054906101000a900460ff1681565b600060019054906101000a900460ff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610727576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260258152602001806108f56025913960400191505060405180910390fd5b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415610799576001600060016101000a81548160ff0219169083151502179055505b600160038111156107a657fe5b60008054906101000a900460ff1660038111156107bf57fe5b14610832576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600c8152602001807f416c72656164792070616964000000000000000000000000000000000000000081525060200191505060405180910390fd5b60015434146108a9576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260148152602001807f57726f6e67206465706f73697420616d6f756e7400000000000000000000000081525060200191505060405180910390fd5b6001543414156108cf576001600060026101000a81548160ff0219169083151502179055505b60026000806101000a81548160ff021916908360038111156108ed57fe5b021790555056fe4f6e6c79207468652062757965722063616e2063616c6c20746869732066756e6374696f6ea2646970667358221220bec0430f206de38be6c09cc95c0d8d85daf3bbd22f1359777e2048e132e2296f64736f6c63430007060033")


    abi = ('[{"inputs":[{"internalType":"address","name":"_buyer","type":"address"},{"internalType":"address payable","name":"_seller","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"buyer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmDelivery","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"currState","outputs":[{"internalType":"enum Escrow.State","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"isBuyerIn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isSellerIn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"seller","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"payable","type":"function"}]')



    involvedEscrow = web3.eth.contract(abi = abi, bytecode = bytecode)

    buyer_ = st.selectbox("Select Buyer Account", options=accounts)
    st.write(f"{buyer_} This is buyer")

    seller_ = st.selectbox("Select Seller Account", options=accounts)
    st.write(f"{seller_} This is the seller")

    amm = st.number_input("Enter a Certificate Token ID to display", value=0, step=1) 

    price =  st.write(f"This is the agreed ammount set per swap deal {amm}")
    if st.button('Construct Deed of Sale'):
        construc_hash = involvedEscrow.constructor(buyer_, seller_, amm).transact({'gas': 2812493})
        receipt = web3.eth.waitForTransactionReceipt(construc_hash)
       
        print(construc_hash, buyer_,receipt)
        st.write(f'This is your transactionHash {construc_hash},Here is your TransactionReceipt {receipt}')

    if st.button('Buyer Deposit funds'):
        view = buyer_
        if view == buyer_:
            deposit_hash = involvedEscrow.functions.deposit().transact({'from' : buyer_, 'to' : contract_location, 'value': amm})
            deposit_receipt = web3.eth.waitForTransactionReceipt(deposit_hash)
            
            print(deposit_hash, deposit_receipt)
            st.write(f'This is your deposit_hash {deposit_hash},Here is your TransactionReceipt {deposit_receipt}')

    if st.button('Transfer SWAP DeeD'):
        safeTransfer_hash = involvedEscrow.functions.safeTransferFrom(contract_location, buyer_, 14).transact({'from' : buyer_, 'to' : contract_location})
        safeTransfer_receipt = web3.eth.waitForTransactionReceipt(safeTransfer_hash)
        print(safeTransfer_hash, safeTransfer_receipt)
        st.write(f'This is your deposit_hash {safeTransfer_hash},Here is your TransactionReceipt {safeTransfer_receipt}')


    if st.button('Buyer Confirm Delivery and Release Deposited Amount'):
        confirmDelivery_hash = involvedEscrow.functions.confirmDelivery().transact({'from' : buyer_, 'to' : contract_location})
        confirmation_receipt = web3.eth.waitForTransactionReceipt(confirmDelivery_hash)

        print(confirmDelivery_hash, confirmation_receipt)
        st.write(f'This is your confirmDelivery_hash {confirmDelivery_hash},Here is your confirmation_receipt {confirmation_receipt}')


    
involvedEscrow()



    ## find a way to extract ammount of have them allow us to handle transaction 


    

    # way to accept and verify dosit to and from smart contract 
