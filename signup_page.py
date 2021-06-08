import streamlit as st

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
