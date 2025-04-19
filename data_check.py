import streamlit as st

st.title("Title : Data Quality")
st.header("Header : Checks")
st.subheader("subheader : check 1")

table1 = st.text_input("Enter table1 name")
table2 = st.text_input("Enter table2 name")

button1 = st.button("show tablenames")
if button1 == True :
    st.write(f'Table1 : {table1}')
    st.write(f'Table2 : {table2}')