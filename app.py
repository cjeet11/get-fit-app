import streamlit as st

# Setup
st.set_page_config(page_title="Get Fit", page_icon="💪")

# App Header
st.title("💪 Get Fit")
st.write("Welcome to your personal fitness journey!")

# User Inputs
name = st.text_input("Enter your name")
weight = st.number_input("Weight (kg)", value=70.0)
height = st.number_input("Height (cm)", value=170.0)

if st.button("Calculate BMI"):
    bmi = round(weight / ((height/100)**2), 2)
    st.success(f"Hi {name}, your BMI is {bmi}")
    
    if bmi < 18.5:
        st.info("Status: Underweight - Focus on nutrition and strength.")
    elif 18.5 <= bmi <= 24.9:
        st.success("Status: Healthy weight - Keep it up!")
    else:
        st.warning("Status: Overweight - Focus on cardio and calorie deficit.")

# Features Section
st.divider()
st.subheader("Daily Goals")
st.checkbox("Drank 3L of water")
st.checkbox("7 hours of sleep")
st.checkbox("10 mins Meditation")
