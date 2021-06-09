import streamlit as st
import os, sys
import pandas as pd 
from PIL import Image


@st.cache
def load_image (image_file):
    img = Image.open(image_file)
    return img  

def save_image(logged_in_user):
    image_file = st.file_uploader("Upload An Image",type=['jpg'])
    if image_file is not None:
        file_details = {"FileName":image_file.name, "FileType":image_file.type}
        #st.write(type(image_file))
        img = load_image(image_file)
        st.image(img)
        
        save_path = '/Users/ayechan/Desktop/Project_3_Swapout/jpg'
        file_name = "{logged_in_user}.jpg"
        #new_file_name = user_name
        completeName = os.path.join(save_path, file_name)
        with open(completeName, "wb") as f:
            f.write(image_file.getbuffer())
            ##renaming image file
            # os.rename(file_name, user_name)
        st.success("File Saved")

<<<<<<< Updated upstream
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
            file_name = image_file.name
            #new_file_name = user_name
            completeName = os.path.join(save_path, file_name)
            with open(completeName, "wb") as f:
                f.write(image_file.getbuffer())
                ##renaming image file
                # os.rename(file_name, user_name)
            st.success("File Saved")
           
if __name__ == '__main__':
	main()
=======
>>>>>>> Stashed changes


