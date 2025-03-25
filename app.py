import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt  # <-- Corrected import

st.set_page_config(page_title="Plot and Compare", layout="centered")
st.title("Plot and compare xlsx")

xlsx_file = st.file_uploader("Upload the Excel (.xlsx) file", type=["xlsx"])

if xlsx_file:
    # Read the Excel file assuming the first row is the header
    excel_df = pd.read_excel(xlsx_file)

    # Transpose the DataFrame so rows become columns for boxplot comparison
    transposed_df = excel_df.T
    transposed_df.columns = ['Row 1', 'Row 2', 'Row 3']

    # Plot the boxplot
    st.subheader("Box Plot Comparison Across Rows")
    fig, ax = plt.subplots()
    transposed_df.boxplot(ax=ax)
    ax.set_ylabel("Value")
    ax.set_title("Comparison of Minimum, Typical, and Maximum Values Across Rows")
    st.pyplot(fig)
