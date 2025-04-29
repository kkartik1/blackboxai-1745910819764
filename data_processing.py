import pandas as pd
import streamlit as st

def process_data(uploaded_file):
    # Read Excel file into DataFrame
    df = pd.read_excel(uploaded_file)
    return df

def categorize_variables(df):
    variable_info = {}
    for col in df.columns:
        dtype = df[col].dtype
        unique_vals = df[col].nunique(dropna=True)
        if pd.api.types.is_numeric_dtype(dtype):
            if unique_vals < 20:
                var_type = "Discrete Numeric"
            else:
                var_type = "Continuous Numeric"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            var_type = "Date"
        elif pd.api.types.is_string_dtype(dtype):
            if unique_vals < 20:
                var_type = "Categorical String"
            else:
                var_type = "Character String"
        else:
            var_type = "Other"
        variable_info[col] = var_type
    return variable_info

def correct_categorization(variable_info):
    st.subheader("Correct Variable Categorization")
    corrected_info = {}
    for var, var_type in variable_info.items():
        corrected_type = st.selectbox(f"Variable: {var}", 
                                      options=["Discrete Numeric", "Continuous Numeric", "Date", "Categorical String", "Character String", "Other"],
                                      index=["Discrete Numeric", "Continuous Numeric", "Date", "Categorical String", "Character String", "Other"].index(var_type))
        corrected_info[var] = corrected_type
    return corrected_info
