import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any

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
if left_column.button('New User'):
    input_data = st.text_input("Create User ID")    
    input_data = st.text_input("Enter personal number")
    input_data = st.text_input("Confirm personal number")     
    left_column.button("Sign Up!")

if right_column.button('Existing User'):
    input_data = st.text_input("Enter User ID")
    input_data = st.text_input("Enter personal number")

# call Streamlit functions inside a "with" block:
# with left_column:
#     chosen = st.radio(
#         'Categories',
#         ("Cars", "Watches"))
#     st.write(f"You are in {chosen} house!")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Select car make',
    ('Chevrolet', 'Porsche', 'BMW')
)

add_selectbox = st.sidebar.selectbox(
    'Select the year',
    ('1960','1970','1980')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)