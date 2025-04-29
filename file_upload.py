import streamlit as st

def upload_file():
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])
    return uploaded_file
