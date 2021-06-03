import streamlit as st
import os
import pandas as pd 
from PIL import Image
@st.cache
def load_image (image_file):
    img = Image.open(image_file)
    return img  

def main():
    st.title ("File Uploads & Saved File to Directory App")
    menu = ["Home", "Dataset", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Upload Image")
        image_file = st.file_uploader("Upload An Image",type=['jpg'])
        if image_file is not None:
            file_details = {"FileName":image_file.name, "FileType":image_file.type}
            #st.write(type(image_file))
            img = load_image(image_file)
            st.image(img)
            
            with open(image_file.name, "wb") as f:
                f.write(image_file.getbuffer())
            st.success("File Saved")

if __name__ == '__main__':
	main()