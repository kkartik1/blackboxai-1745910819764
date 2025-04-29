import streamlit as st
import plotly.express as px
import pandas as pd

def suggest_visualizations(variable_info):
    suggestions = []
    for var, var_type in variable_info.items():
        if var_type in ["Discrete Numeric", "Categorical String"]:
            suggestions.append(f"Bar Chart of {var}")
        elif var_type == "Continuous Numeric":
            suggestions.append(f"Histogram of {var}")
        elif var_type == "Date":
            suggestions.append(f"Time Series of {var}")
    return suggestions

def generate_visualizations(df, variable_info, selected_viz):
    for viz in selected_viz:
        if viz.startswith("Bar Chart of "):
            var = viz.replace("Bar Chart of ", "")
            fig = px.bar(df[var].value_counts().reset_index(), x='index', y=var, labels={'index': var, var: 'Count'})
            st.plotly_chart(fig)
        elif viz.startswith("Histogram of "):
            var = viz.replace("Histogram of ", "")
            fig = px.histogram(df, x=var)
            st.plotly_chart(fig)
        elif viz.startswith("Time Series of "):
            var = viz.replace("Time Series of ", "")
            if var in df.columns and pd.api.types.is_datetime64_any_dtype(df[var]):
                df_sorted = df.sort_values(var)
                fig = px.line(df_sorted, x=var, y=df_sorted.columns[0])  # Just an example, y axis needs better logic
                st.plotly_chart(fig)
            else:
                st.warning(f"Column {var} is not a datetime type.")
