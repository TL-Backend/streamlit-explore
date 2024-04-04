import streamlit as st
from widgets import text_input_widget, slider_widget, checkbox_widget, dropdown_widget, button_widget, file_uploader_widget, date_input_widget, number_input_widget, radio_button_widget, multiselect_widget, color_picker_widget, time_input_widget
from dataframe import basic_table, numpy_random_table

def main():
    st.title("My App")
    text_input_widget()
    slider_widget()
    checkbox_widget()
    dropdown_widget()
    button_widget()
    file_uploader_widget()
    date_input_widget()
    number_input_widget()
    radio_button_widget()
    multiselect_widget()
    color_picker_widget()
    time_input_widget() 
    basic_table()
    numpy_random_table()
    
if __name__ == "__main__":
    main()
