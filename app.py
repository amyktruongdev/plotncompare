import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt  # Correct import

st.set_page_config(page_title="Plot and Compare", layout="centered")
st.title("Plot and compare xlsx")

xlsx_file = st.file_uploader("Upload the Excel (.xlsx) file", type=["xlsx"])

if xlsx_file:
    # Read the Excel file
    excel_df = pd.read_excel(xlsx_file)

    # Set up bar plot
    st.subheader("Bar Plot Comparison Across CLs")
    fig, ax = plt.subplots()

    # Create bar positions
    labels = ['CL 1', 'CL 2', 'CL 3']
    x = range(len(labels))  # [0, 1, 2]
    width = 0.2  # Width of each bar

    # Plot each value type (minimum, typical, maximum)
    ax.bar([i - width for i in x], excel_df['minimum'], width, label='Minimum')
    ax.bar(x, excel_df['typical'], width, label='Typical')
    ax.bar([i + width for i in x], excel_df['maximum'], width, label='Maximum')

    # Customize the plot
    ax.set_ylabel("Value")
    ax.set_title("Comparison of Values Across CLs")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    st.pyplot(fig)
