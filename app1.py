import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (cm):", min_value=1.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.info("You have a normal weight.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
