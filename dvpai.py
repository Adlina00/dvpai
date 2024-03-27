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

        # Example calculations (replace with specific logic)
        average_values = data.mean().to_string(index=False)
        summary_text += f"Average values:\n{average_values}\n"

        # Add more calculations and formatting based on your chart and desired insights

        return summary_text
    

def main():
    st.image('logo2.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()

if __name__=="__main__":
    main()