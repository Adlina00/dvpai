from ast import main
import openai
import pandas as pd
import streamlit as st
from openai import OpenAI
import os


from dotenv import load_dotenv
load_dotenv()
openai_api_key = st.secrets["OPENAI_API_KEY"]

# set global variables
KEYLIST = list(range(1, 30))
DATA_TYPES = ['String', 'Integer', 'Decimal', 'Time']
STAT_TYPES = ['None', 'Sum', 'Mean', 'Min', 'Max', 'Std']
NUMERIC_TYPES = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
FLOAT_NUMERICS = ['float16', 'float32', 'float64']
INT_NUMERICS = ['int16', 'int32', 'int64']
DATE_TYPES = ['datetime64[ns]']
CHART_TYPES = ['Bar', 'Box', 'Histogram', 'Line', 'Linear Regression', 'Map', 'Scatter']
MAP_TYPES = ['USA-states', 'USA-Counties']
CHART_ERR_MESS = '### Unable to create chart. Edit input data'
CHARTS_WITHOUT_COLOR = ['Map']
COLOR_SCALE_OPTIONS = ['agsunset', 'bluered', 'blues', 'cividis', 'darkmint', 'emrld', 'earth', 
                       'greens', 'ice', 'inferno', 'jet', 'magma', 'magenta', 'tropic', 'viridis']
PLOT_STYLES = ['ggplot2', 'seaborn', 'simple_white', 'plotly',
               'plotly_white', 'plotly_dark', 'presentation', 'none']
GRID_OPTIONS = ['xgridoff', 'ygridoff']


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
            

def app_theme():
    custom_theme = {
    "primaryColor": "#7792E3",  # Accent color for interactive elements
    "backgroundColor": "#C0C0C0",  # Background color for the main content area
    "secondaryBackgroundColor": "#B9F1C0",  # Background color for sidebar and most interactive widgets
    "textColor": "#FFFFFF",  # Color used for almost all text
    "font": "sans serif",  # Font family for all text in the app, except code blocks
    "fontSize": 16  # Font size for text
    }

    # Apply the custom theme
    st.set_page_config(page_title="Custom Theme Example", layout="wide", initial_sidebar_state="expanded", theme=custom_theme)


def main():
    st.image('logo2.png')
    st.subheader("Easy Data Visualized with DataVizPro")
    return handle_data_upload_and_visual()



    

if __name__=="__main__":
    main()