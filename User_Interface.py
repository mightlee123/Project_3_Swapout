import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any


st.title("Welcome to Swapout!")
# # adding logo
# title_container = st.beta_container()
# col1, col2 = st.beta_columns([1, 20])
# image = Image.open('/Users/ayechan/Desktop/Project_3_Swapout/jpg/car.jpg')
# with title_container:
#     with col1:
#         st.image(image, width=64)
#     with col2:
#         st.markdown('<h1 style="color: purple;">Suzieq</h1>',
#                     unsafe_allow_html=True)
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
    # input_data = st.text_input("Create User ID")    
    # input_data = st.text_input("Enter personal number")
    # input_data = st.text_input("Confirm personal number")     
    # left_column.button("Sign Up!")
    header = st.beta_container()
    personal_info = st.beta_container()
    vehicle_info = st.beta_container()

    prev, _ ,next = st.beta_columns([1, 8, 1])

    next.button("Next")

    prev.button("Previous")

    with header:
        st.write("## Let's create your SWAPOUT Account!")
    
    with personal_info:
        st.write("Personal Information")

        first, last = st.beta_columns(2)
    
        first.text_input("First Name")
        last.text_input("Last Name")

        st.text_input("Email Address")

        password, confirmpassword = st.beta_columns(2)

        password.text_input("Password", type="password")
        confirmpassword.text_input("Confirm Password", type="password")

    with vehicle_info:
        st.write("Vehicle Information")

        year = st.selectbox("What year is your car?", options = range(2021, 1949, -1))

        make = st.selectbox("What make is your vehicle?", options = ["Acura", "Alfa Romeo", "AMC", "Aston Marton", "Audi", "Bentley", "BMW", "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Citroen", "Datsun", "Daewoo", "Delorean", "Dodge", "Eagle", "Ferarri", "FIAT", "Fisker", "Ford", "Freightliner", "Genesis", "Geo", "GMC", "Honda", "HUMMER", "Hyundai", "INFINITI", "Isuzu", "Jaguar", "Jeep", "Karma", "Kia", "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Lotus", "LUCID", "Maserati", "Maybach", "MAZDA", "McLaren", "Mercedes-Benz", "Mercury", "MINI", "Mitsubishi", "NIO", "Nissan", "Oldsmobile", "Opel", "Peugot", "Plymouth", "Pontiac", "Porsche", "RAM", "Renault", "Rolls-Royce", "Saab", "Saturn", "Scion", "Skoda", "smart", "SRT", "Studebaker", "Subaru", "Suzuki", "Tesla", "Toyota", "Vauzhall", "Volkswagen", "Volvo", "Yugo"])

        model = st.text_input("What model is your car?")

        miles = st.text_input("How many miles does your car have?")

        certification = st.radio("Does your car have any aftermarket parts?", ("Yes", "No"))

        # # adding value of the vehicle
        # value = st.slider(
        # 'Select a range of values',
        # 0.0, 100.0, (25.0, 75.0)

if right_column.button('Existing User'):
    input_data = st.text_input("Enter User ID")
    input_data = st.text_input("Enter personal number")

