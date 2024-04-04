import streamlit as st
import datetime
def text_input_widget():
    user_input = st.text_input("Enter your name")
    if user_input:
        st.write("Hello", user_input)

def slider_widget():
    age = st.slider("Select your age", 0, 100)
    if age:
        st.write("Your age is:", age)

def checkbox_widget():
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.write("Great! Let's proceed.")

def dropdown_widget():
    option = st.selectbox("Select a city", ["New York", "London", "Tokyo"])
    st.write("You selected:", option)

def button_widget():
    if st.button("Click me"):
        st.write("Button clicked!")

def file_uploader_widget():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file:
        st.write("File uploaded:", uploaded_file.name)

def date_input_widget():
    selected_date = st.date_input("Select a date", datetime.date.today())
    st.write("Selected date:", selected_date)
    
def number_input_widget():
    number = st.number_input("Enter a number", value = 0.3, step = 0.02, min_value= -0.0, max_value = 1.02)
    st.write("Number entered:", number)
    
def radio_button_widget():
    option = st.radio("Choose an option", ("Option 1", "Option 2", "Option 3"))
    st.write("Selected option:", option)
    
def multiselect_widget():
    options = st.multiselect("Select multiple options", ["Option 1", "Option 2", "Option 3"])
    st.write("Selected options:", options)

def color_picker_widget():
    color = st.color_picker("Choose a color", "#ff6347")
    st.write("Selected color:", color)

def time_input_widget():
    time = st.time_input("Enter a time", datetime.datetime.now().time())
    st.write("Time entered:", time)
