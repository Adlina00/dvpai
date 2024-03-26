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

        # If the "Get Data Summary button is clicked:
        if st.button("Get Data Summary"):
            """Generates a data visualization summary using OpenAI (if available)."""

            # Define the prompt content for the OpenAI model (clarified)
            prompt_content = f"**Provide a summary of the data visualization based on the uploaded data.**"

            # Define the messages for the OpenAI model (focused on summary)
            messages = [
                {
                "role": "system",
                "content": "You can help me by summarizing the data visualization."
                },
                {
                "role": "user",
                "content": prompt_content
                }
            ]

            try:
                # Call OpenAI and display the response (error handling)
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                st.write("Data Visualization Summary:", response.choices[0].text.strip())

            except Exception as e:  # Handle potential errors with OpenAI or network issues
                st.error("Failed to generate data visualization summary. Error:", e)

def main():
    st.image('logo2.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()

if __name__=="__main__":
    main()