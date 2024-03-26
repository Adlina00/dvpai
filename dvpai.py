from ast import main
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

        chart_type = st.selectbox("Select Chart Type", ["Line Plot", "Scatter Plot", "Bar Chart", "Histogram"])

        if chart_type == "Line Plot":
                st.subheader("Line Plot")
                # Create a line plot
                fig, ax = plt.subplots()
                ax.plot(df.sepal_length, df.sepal_width)
                st.pyplot(fig)

        elif chart_type == "Scatter Plot":
                st.subheader("Scatter Plot")
                # Create a scatter plot
                fig, ax = plt.subplots()
                ax.scatter(df.petal_length, df.petal_width)
                st.pyplot(fig)

        elif chart_type == "Bar Chart":
                st.subheader("Bar Chart")
                # Create a bar chart
                bar_df = df.columns.value_counts()
                fig, ax = plt.subplots()
                ax.bar(bar_df.index, bar_df.values)
                st.pyplot(fig)

        elif chart_type == "Histogram":
                st.subheader("Histogram")
                # Create a histogram
                fig, ax = plt.subplots()
                ax.hist(df.sepal_length, bins=20)
                st.pyplot(fig)
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


def main():
    st.image('logo.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()

if __name__=="__main__":
    main()