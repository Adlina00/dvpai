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
            #Define the prompt content for the OPENAI model
            prompt_content = f"""Generate caption for the chart."""

            # Define the messages for the OpenAI model
            messages=[
                {
                    "role":"system", 
                    "content":"Generate caption for the visualization created."
                },
                {
                    "role":"user",
                    "content":prompt_content
                }

            ]

            # call openai and display the response
            response= openai.ChatCompletion. create(model = "gpt-3.5-turbo", messages=messages)
            st.write("Generated Visualization Code: ")
            st.code(response.choices[0].text.strip())

def main():
    st.image('logo2.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()

if __name__=="__main__":
    main()