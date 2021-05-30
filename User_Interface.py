import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any


st.title("Welcome to Swapout!")
st.markdown("## Your customized virtual market place")

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

# will use this list and next button to increment page, MUST BE in the SAME order
# as the list passed to the radio button
new_choice = ['Home','Gallery','About']

# This is what makes this work, check directory for a pickled file that contains
# the index of the page you want displayed, if it exists, then you pick up where the
#previous run through of your Streamlit Script left off,
# if it's the first go it's just set to 0
if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    # check if you are at the end of the list of pages
    if next_clicked == len(new_choice):
        next_clicked = 0 # go back to the beginning i.e. homepage
else:
    next_clicked = 0 #the start

# this is the second tricky bit, check to see if the person has clicked the
# next button and increment our index tracker (next_clicked)
if next:
    #increment value to get to the next page
    next_clicked = next_clicked +1

    # check if you are at the end of the list of pages again
    if next_clicked == len(new_choice):
        next_clicked = 0 # go back to the beginning i.e. homepage

# create your radio button with the index that we loaded
choice = st.sidebar.radio("go to",('Home', 'Gallery', 'About'), index=next_clicked)

# pickle the index associated with the value, to keep track if the radio button has been used
pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

# finally get to whats on each page
if choice == 'Home':
    st.write('this is home')
elif choice == 'Gallery':
    st.write('A Gallery of some sort')
elif choice == 'About':
    st.write('About page')

left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
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