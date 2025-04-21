import streamlit as st

def show_sample_records(data):
    st.dataframe(data)

def show_columns(data):
    st.write("columns : ",data.columns)

def show_missing_data(data):
    st.write("missing data : ",data.isnull())

def show_data_stats(data):
    st.write("data stats : ",data.describe())
