from ast import main
import openai
import pandas as pd
import streamlit as st
from openai import OpenAI
import os
import seaborn as sns
import matplotlib as plt

from dotenv import load_dotenv
load_dotenv()
openai_api_key = st.secrets["OPENAI_API_KEY"]

            
def handle_data_upload_and_visual():
    # Create a file uploader widget for data upload
    uploaded_file = st.file_uploader("Upload a dataset file", type=["csv"])

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
            # Display pair plot with kernel density estimate (KDE) plots
            sns.pairplot(df[columns], kind="kde")

            # Display pair plot with regression plots
            sns.pairplot(df[columns], kind="reg")

            # Display pair plot with histograms
            sns.pairplot(df[columns], kind="hist")
            st.pyplot()
        else:
            st.warning("Please select columns for visualization.")


def main():
    st.image('logo2.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()

if __name__=="__main__":
    main()