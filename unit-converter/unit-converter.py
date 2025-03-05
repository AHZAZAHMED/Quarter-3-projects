import streamlit as st 

st.title("🌐Unit Converter")
st.markdown("#### This is a simple unit converter that converts units of length, weight, time and temperature.")
st.write("<h4 style='text-align: center;'>Made by Ahzaz Ahmed</h4>", unsafe_allow_html=True)
st.write("Select the category of unit you want to convert from the sidebar.")

category = st.selectbox("Select the category of unit you want to convert", ["Length", "Weight", "Time", "Temperature"])

def convert_unit(category, value,unit):
    if category == "Length":
        if unit == "Centimeter to Meter":
           return value / 100
        elif unit == "Meter to Centimeter":
            return value * 100
        elif unit == "Meter to Kilometer":
            return value / 1000
        elif unit == "Kilometer to Meter":
            return value * 1000
        elif unit == "Miles to  Kilometer":
            return value * 1.60934
        elif unit == "Kilometers to miles":
            return value / 1.60934
        elif unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value * 0.3048
        
    elif category == "Weight":
        if unit == "Grams to kilograms":
            return value / 1000
        elif unit == "Kilograms to grams":
            return value * 1000
        elif unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value * 0.453592
        elif unit == "Grams to ounces":
            return value * 0.035274
        elif unit == "Ounces to grams":
            return value * 28.3495

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15


if category == "Length":
    unit = st.selectbox("Select the unit you want to convert from", ["Centimeter to Meter", "Meter to Centimeter", "Meter to Kilometer", "Kilometer to Meter", "Miles to  Kilometer", "Kilometers to miles", "Meters to feet", "Feet to meters"])
elif category == "Weight":
    unit = st.selectbox("Select the unit you want to convert from", ["Grams to kilograms", "Kilograms to grams", "Kilograms to pounds", "Pounds to kilograms", "Grams to ounces", "Ounces to grams"])
elif category == "Time":
    unit = st.selectbox("Select the unit you want to convert from", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
elif category == "Temperature":
    unit = st.selectbox("Select the unit you want to convert from", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])



value = st.number_input("Enter the value that you want to convert")

def formula():
    if unit == "Centimeter  to Meter":
        st.write("Formula: value / 100")
    elif unit == "Meter to Centimeter":
        st.write("Formula: value * 100")
    elif unit == "Meter to Kilometer":
        st.write("Formula: value / 1000")
    elif unit == "Kilometer to Meter":
        st.write("Formula: value * 1000")
    elif unit == "Miles to  Kilometer":
        st.write("Formula: value * 1.60934")
    elif unit == "Kilometers to miles":
        st.write("Formula: value / 1.60934")
    elif unit == "Meters to feet":
        st.write("Formula: value * 3.28084")
    elif unit == "Feet to meters":
        st.write("Formula: value * 0.3048")
    elif unit == "Grams to kilograms":
        st.write("Formula: value / 1000")
    elif unit == "Kilograms to grams":
        st.write("Formula: value * 1000")   
    elif unit == "Kilograms to pounds":
        st.write("Formula: value * 2.20462")    
    elif unit == "Pounds to kilograms":
        st.write("Formula: value * 0.453592")
    elif unit == "Grams to ounces":
        st.write("Formula: value * 0.035274")
    elif unit == "Ounces to grams":
        st.write("Formula: value * 28.3495")
    elif unit == "Seconds to minutes":
        st.write("Formula: value / 60")
    elif unit == "Minutes to seconds":
        st.write("Formula: value * 60")
    elif unit == "Minutes to hours":
        st.write("Formula: value / 60")
    elif unit == "Hours to minutes":
        st.write("Formula: value * 60")
    elif unit == "Hours to days":
        st.write("Formula: value / 24")
    elif unit == "Days to hours":
        st.write("Formula: value * 24")
    elif unit == "Celsius to Fahrenheit":
        st.write("Formula: (value * 9/5) + 32")
    elif unit == "Fahrenheit to Celsius":
        st.write("Formula: (value - 32) * 5/9")
    elif unit == "Celsius to Kelvin":
        st.write("Formula: value + 273.15")
    elif unit == "Kelvin to Celsius":
        st.write("Formula: value - 273.15") 

if st.button("Convert"):
    if value == 0:
        st.error("Please enter a value to convert")
    else:
        result = convert_unit(category, value, unit)
        st.success(f"The result is {result:.2f}")
        formula()

