import streamlit as st
import pandas as pd

import src.myFunction as myFunction

st.header("This is page1")

uploaded_csv = st.file_uploader("Upload file",type=['csv'])

if uploaded_csv is not None:
    data = pd.read_csv(uploaded_csv)

button1 = st.button("show sample records")
if button1 == True:
    #st.dataframe(data.head(4))
    myFunction.show_sample_records(data)

button2 = st.button("show columns")
if button2 == True:
    #st.write("columns : ",data.columns)
    myFunction.show_columns(data)

button3 = st.button("show missing data")
if button3 == True:
    #st.write("missing data : ",data.isnull())
    myFunction.show_missing_data(data)

button4 = st.button("show data stats")
if button4 == True:
    #st.write("data stats : ",data.describe())
    myFunction.show_data_stats(data)

# if uploaded_csv is not None:
#     data = pd.read_csv(uploaded_csv)
#     #st.dataframe(data.head(4))