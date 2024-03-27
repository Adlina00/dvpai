import openai
import pandas as pd
import streamlit as st
from openai import OpenAI
import os
import seaborn as sns


from dotenv import load_dotenv
load_dotenv()
openai_api_key = st.secrets["OPENAI_API_KEY"]

            
def handle_data_upload_and_visual():
    # Create a file uploader widget for data upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        #Read the uploaded csv file into a dataframe
        df = pd.read_csv(uploaded_file)

        #display the uploaded data
        st.write("Uploaded Data: ")
        st.write(df)

        columns = st.multiselect("Select columns for visualization", df.columns)

        if columns:
            #Generate a pairplot based on the selected columns
            st.write("Pairplot based on selected columns: ")
            sns.pairplot(df[columns], kind="scatter")
            st.pyplot()
            st.write("Right click and save your image for further")

            # Calculate descriptive statistics for the selected columns
            summary_stats = df[columns].describe()

            # Display the summary statistics
            st.write("**Chart Summary:**")
            st.write(summary_stats)

    def generate_chart_summary(data):
        """
        This function analyzes the chart data (`data`) and generates a summary. 
        Calculates descriptive statistics for the provided data.

        Replace the placeholder logic with calculations relevant to your chart type
        (e.g., trends, correlations, outliers).

        Args:
            data (pd.DataFrame): The DataFrame containing the selected columns.

        Returns:
            str: A string summarizing the key insights from the chart.
            str: A string summarizing the descriptive statistics.
        """

        summary_text = ""

        # Calculate summary statistics
        summary_stats = generate_chart_summary(data)
        summary_text += f"**Descriptive Statistics:**\n{summary_stats}\n"

        # Example analysis for pairplots (replace with specific logic)

        # Identify correlations
        correlations = data.corrcoef().unstack().dropna().sort_values(ascending=False)
        strong_correlations = correlations[abs(correlations) > 0.7]

        if not strong_correlations.empty:
            corr_list = strong_correlations.index.tolist()
            corr_values = strong_correlations.values.tolist()
            corr_text = ", ".join([f"{corr[0]} ({corr[1]:.2f})" for corr in zip(corr_list, corr_values)])
            summary_text += f"**Strong Correlations:** {corr_text}\n"

        return summary_text
    

def main():
    st.image('logo2.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()

if __name__=="__main__":
    main()