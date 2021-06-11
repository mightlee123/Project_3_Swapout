# SwapOutExchange

-----

* Classified Advertisements Blockchain-Powered Backed by Smart Contracts.

### Our mission with SwapOut
We are looking for SwapOut to add trust and boost privacy into the market of used collectibles. For us to achieve our goal we looked to integrate blockchain into this market. With the help smart contracts, we can preset any terms and specific conditions and requirements, also require integrity of buyer and seller using signatures.

![image](https://user-images.githubusercontent.com/73854785/121705516-8f64a480-ca89-11eb-88f1-41fe32e6776a.png)

-----

### The App 
Building a quick path from sign up to blockchain verifiability by direct access to a custom Ethereum Wallet and address during sign up.

![image](https://user-images.githubusercontent.com/73854785/121713328-955e8380-ca91-11eb-8784-49baa54c1865.png)

-----

![image](https://user-images.githubusercontent.com/73854785/121713520-d060b700-ca91-11eb-9bee-8b50b5eef6e9.png)

-----
### Digital Equivalent Entitling Deliverance
Innovating with DEED’s Digital Equivalent Entitling Deliverance using from the ERC-721 token standard embed with conditionally customizable smart contracts. as a representation of the physical item in your digital wallet
-----

https://user-images.githubusercontent.com/73854785/121716162-904f0380-ca94-11eb-9598-2843b788e6a3.mp4

-----

![image](https://user-images.githubusercontent.com/73854785/121728670-6f8daa80-caa2-11eb-9352-65610c737fb7.png)

-----

### SwapMeet
With innovation comes simplicity. We aim to impeccably fortify our DEED’s and present the intricate concept and to our users with just the benefits of this innovative method. Notifications and negotiations at the tips of your fingers via well familiar methods. Once your DEED is created and on the Swap Meet other early adopters of blockchain can reach out with offers. 

![image](https://user-images.githubusercontent.com/73854785/121728768-8b914c00-caa2-11eb-8832-6b3ad3ddbc50.png)

-----

![image](https://user-images.githubusercontent.com/73854785/121728795-95b34a80-caa2-11eb-865e-0bf0354b5fdd.png)

-----

### Transactions phase
In the transactions phase we once again deliver a customizable solution powered by smart contracts. With the DEED of Sale contract an involved escrow takes place between the parties involved. The buyers address must also be the one depositing the funds into the contract. The seller controls the transfer of the SWAP DEED. After being notified of buyer’s deposit and physical transfer being made the seller will then send over the SWAP DEED as proof of ownership via owing the original tokenized DEED and the new DEED of Sale. All this power come from the embracing of embodiment in blockchain. Verify and solidify with SwapOut.

https://user-images.githubusercontent.com/73854785/121729601-854f9f80-caa3-11eb-8179-2812bbba4f7c.mp4

-----

### Foundational Design Team:

*  Mike Husary 
*  Might Lee
*  Aye Oo
*  Javier Barrios
 
------

### Swapping Ahead 
* Continue to put user experience first.
* Create a verified network for our memebers to communicate.
* Shopping assicatnce with Oracle data.
* Lightning auctions using our DEED's and smart contracts.

-----

### Sample Code

Custom background


```
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
```
----

Home page 

```
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import webbrowser



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

left_column, right_column = st.beta_columns(2)

# left_column.button('Sign Up')

if left_column.button('Sign Up') == True:
    webbrowser.open_new_tab('http://localhost:8087/')


if right_column.button('Log In') == True:
    webbrowser.open_new_tab('http://localhost:8085/')
```

----

Allowing for image uploads

```
@st.cache
def load_image (image_file):
    img = Image.open(image_file)
    return img
def save_image():
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
            save_path = '../Project_3_Swapout/jpg'
            file_name = "{account_address}.jpg"
            #new_file_name = user_name 
            #completeName = os.path.join(save_path, file_name)
            #with open(completeName, "wb") as f:
                #f.write(image_file.getbuffer())
                ##renaming image file
                # os.rename(file_name, user_name)
            st.success("File Saved")
```
------

Directing data flow

```
if next.button("Finalize Registration") == True:
    import pathlib as Path
    # pulls the general info of the users and saves it to a dataframe(csv)
    general_info_list = []
    general_info_list.append({"First Name": first_name, "Last Name": last_name, "Email": email_address, "Year": year, "Make": make, "Model": model, "Miles": miles, "Certification": certification})
    general_path = Path("../Project_3_Swapout/csv_data/general_info.csv")
    general_info_df=pd.read_csv(general_path)
    general_info_df.append(general_info_list)


    # pulls the private info of the users and saves it to a dataframe(csv)
    private_info_list = []
    private_info_list.append({"Digital Address": account_address, "Password": confirm_password, "Physical Address": mailing_address, })
    private_path = Path("../Project_3_Swapout/csv_data/private_info.csv")
    private_info_df=pd.read_csv(private_path)
    private_info_df.append(private_info_list)
```
----

Involed escrow 

```
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
        ```


           
