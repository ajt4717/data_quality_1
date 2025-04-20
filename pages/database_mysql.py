import streamlit as st
import pandas as pd

st.header("Database QC")

import mysql.connector

# connecting to the database 
mydb = mysql.connector.connect(
  host="bhhdeiho5kfkljyqx1ae-mysql.services.clever-cloud.com",
  user="uqnhvavizgrbe5jl",
  password="uT5V89vG6K4BTHigg7vT",
  port="3306",
  database="bhhdeiho5kfkljyqx1ae",
  use_pure=True
)

#test connection
print("**********   **********")
print(mydb)

# preparing a cursor object 
cursor = mydb.cursor(dictionary=True)

print("********** single query **********")
#querying
query = """
show databases;
"""

cursor.execute(query)
for x in cursor:
    print(x)


print("********** multiple query **********")
multiple_query = """
show databases;
use bhhdeiho5kfkljyqx1ae;
show tables;
select * from table1
"""

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
mysql_data=[]
for query in multiple_query.split(';'):
    cursor.execute(query)
    #columns = [i[0] for i in cursor.description]
    mysql_data = cursor.fetchall()
    print("type(mysql_data) : ",type(mysql_data))
    #print(columns)
    print("---------")
    df = pd.DataFrame(mysql_data)
    print(df)
    print("**************")


# disconnecting from server
mydb.close() 

button1 = st.button("show sample mysql records")
if button1 == True and len(mysql_data)>0:
    st.write(mysql_data)
    st.dataframe(df)
