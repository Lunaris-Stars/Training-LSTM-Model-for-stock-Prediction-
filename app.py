import streamlit as st
import pandas as pd
from Gettin_Data import GetData, Clean_data
from Model_Training import analyze

# Title of the app
st.title("Stock Analysis Tool")

# Sidebar for user inputs
st.sidebar.header("User  Inputs")
company_name = st.sidebar.text_input("Enter the company name:")
start_date = st.sidebar.date_input("Start date:")
end_date = st.sidebar.date_input("End date:")

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'cleaned_data' not in st.session_state:
    st.session_state.cleaned_data = None
if 'view' not in st.session_state:
    st.session_state.view = 'main'  # Default view

# Input fields for model parameters
st.sidebar.header("Model Parameters")
time_step = st.sidebar.number_input("Time Step:", min_value=1, value=30)  # Default value set to 30
epochs = st.sidebar.number_input("Number of Epochs:", min_value=1, value=100)  # Default value set to 100
learning_rate = st.sidebar.number_input("Learning Rate:", min_value=0.0001, max_value=0.1, value=0.001, format="%.4f")  # Default value set to 0.001

# Main panel for buttons
st.header("Actions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Get Data"):
        if company_name:
            data = GetData(company_name, start_date, end_date)
            st.session_state.data = data
            st.success("Data fetched successfully!")
        else:
            st.warning("Please enter a company name.")

with col2:
    if st.button("Clean Data"):
        if st.session_state.data is not None and not st.session_state.data.empty:
            cleaned_data = Clean_data(st.session_state.data)
            st.session_state.cleaned_data = cleaned_data
            st.success("Data cleaned successfully!")
        else:
            st.warning("No data available to clean. Please fetch data first.")

with col3:
    if st.button("Save Cleaned Data"):
        if st.session_state.cleaned_data is not None and not st.session_state.cleaned_data.empty:
            Clean_data.save_data(st.session_state.cleaned_data)
            st.success("Cleaned data saved successfully!")
        else:
            st.warning("No cleaned data available to save. Please clean data first.")

# Option to choose data for analysis
analyze_data_option = st.selectbox("Select data for analysis:", ["Original Data", "Cleaned Data"])

# Analyze button
if st.button("Analyze"):
    if analyze_data_option == "Original Data":
        if st.session_state.data is not None and not st.session_state.data.empty:
            analyze(st.session_state.data, company_name, time_step, epochs, learning_rate)
            st.success("Analysis completed successfully on original data!")
        else:
            st.warning("No original data available for analysis. Please fetch data first.")
    elif analyze_data_option == "Cleaned Data":
        if st.session_state.cleaned_data is not None and not st.session_state.cleaned_data.empty:
            analyze(st.session_state.cleaned_data, company_name, time_step, epochs, learning_rate)
            st.success("Analysis completed successfully on cleaned data!")
        else:
            st.warning("No cleaned data available for analysis. Please clean data first.")