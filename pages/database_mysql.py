import streamlit as st
import pandas as pd
import time
import mysql.connector

import src.myFunction as myFunction

st.header("Database QC")

# connecting to the database 
mydb = mysql.connector.connect(
  host="bhhdeiho5kfkljyqx1ae-mysql.services.clever-cloud.com",
  user="uqnhvavizgrbe5jl",
  password="uT5V89vG6K4BTHigg7vT",
  port="3306",
  database="bhhdeiho5kfkljyqx1ae",
  use_pure=True
)

# #test connection
# print("**********   **********")
# print(mydb)

# preparing a cursor object 
cursor = mydb.cursor(dictionary=True)

# print("********** single query **********")
# #querying
# query = """
# show databases;
# """

# cursor.execute(query)
# for x in cursor:
#     print(x)

database_mysql = "bhhdeiho5kfkljyqx1ae"
table_mysql = st.text_input("Enter mysql table name")

def prepare_query(table_mysql):
    print("********** multiple query **********")
    multiple_query = """
    use bhhdeiho5kfkljyqx1ae;
    select * from {}
    """.format(table_mysql)
    print(multiple_query)
    return multiple_query

def execute_query(table_mysql, sql="na"):
    if sql=="na":
        multiple_query = prepare_query(table_mysql)
    else:
        multiple_query=sql
    
    for query in multiple_query.split(';'):
        cursor.execute(query)
        # #columns = [i[0] for i in cursor.description]
        mysql_data = cursor.fetchall()
        # print("type(mysql_data) : ",type(mysql_data))
        # #print(columns)
        print("---------")
        df = pd.DataFrame(mysql_data)
        print(df)
        print("**************")
    return df


button_explore = st.button("explore")
if button_explore == True :
    data = execute_query(table_mysql)
    st.write("Record count : ", data.shape[0])

# if button_explore == False :
#     time.sleep(60)

# if button_explore == True :
#     print("********** multiple query **********")
#     multiple_query = """
#     use bhhdeiho5kfkljyqx1ae;
#     select * from {}
#     """.format(table_mysql)
#     print(multiple_query)

    #not in proper format
    # mysql_data=[]
    # for query in multiple_query.split(';'):
    #     cursor.execute(query)
    #     for x in cursor:
    #         print(type(x))
    #         print(x)
    #         mysql_data.append(x)
    #
    #print(type(mysql_data))
    #print(mysql_data)

#other format



# button0 = st.button("show sample mysql records")
# if button0 == True and len(mysql_data)>0:
#     st.subheader("Data in normal format")
#     st.write(mysql_data)
#     st.subheader("Data in dataframe format")
#     st.dataframe(df)

button1 = st.button("show sample records")
if button1 == True:
    #st.dataframe(data.head(4))
    data = execute_query(table_mysql)
    myFunction.show_sample_records(data)

button2 = st.button("show columns")
if button2 == True:
    #st.write("columns : ",data.columns)
    sql = """use {}; select * from {} limit 1""".format(database_mysql,table_mysql)
    data = execute_query(table_mysql,sql)
    myFunction.show_columns(data)

button3 = st.button("show missing data")
if button3 == True:
    #st.write("missing data : ",data.isnull())
    data = execute_query(table_mysql)
    myFunction.show_missing_data(data)

button4 = st.button("show data stats")
if button4 == True:
    #st.write("data stats : ",data.describe())
    data = execute_query(table_mysql)
    myFunction.show_data_stats(data)

# disconnecting from server
mydb.close() 