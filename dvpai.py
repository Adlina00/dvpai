import openai
import pandas as pd
import streamlit as st
from openai import OpenAI
import os


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

        import seaborn as sns
        import matplotlib as plt

        columns = st.multiselect("Select columns for visualization", df.columns)

        # Disable the PyplotGlobalUseWarning
        st.set_option('deprecation.showPyplotGlobalUse', False)

        if columns:
            #Generate a pairplot based on the selected columns
            st.write("Pairplot based on selected columns: ")
            sns.pairplot(df[columns], kind="scatter")
            st.pyplot()

        #Create a text area for user input prompt
        query = st.text_area("Enter your prompt: ", placeholder="Enter your prompt here")

        # If the "Get Visualization button is clicked:
        if st.button("Get Visualization"):
            #Define the prompt content for the OPENAI model
            prompt_content = f"""The dataset is ALREADY loaded into a DataFrame named 'df'. DO NOT load the data again. The DataFrame has the following columns: 
            (df.columns.tolist()) Provide a prompt generate a data visualization based on the uploaded data. - USE SINGLE CODE BLOCK with a solution. Do not explain the code - Do not comment the code. -ALWAYS WRAP UP THE CODE IN A SINGLE CODE BLOCK. - Example code format '''code'''"""

            # Define the messages for the OpenAI model
            model = "gpt-3.5-turbo"
            messages=[{
                {
                    "role":"system", 
                    "content":"You are a helpful Data Visualization assistant who generate a data visualization based on the uploaded data."
                },
                {
                    "role":"user",
                    "content":prompt_content
                }

            }]

            # call openai and display the response
            response= openai.chatCompletion. create(model = "gpt-3.5-turbo", messages=messages)
            st.write("Generated Visualization Code: ")
            st.code(response.choices[0].text.strip())

def main():
    st.image('logo.png')
    st.title("DataVizPro: AI-Powered Data Visualization Tool")
    response= handle_data_upload_and_visual()

if __name__=="__main__":
    main()