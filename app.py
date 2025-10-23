import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021')
st.subheader('Was the tutorial helpful?')

### --- LOAD DATAFRAME
excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)