#!/usr/bin/python3

import mysql.connector as mysql

# RDS info
u='harsh'    # RDS username
p=''  # RDS password
db='harshdbs'   # RDS database name 
h='harsh.******************.rds.amazonaws.com'  # RDS database host name


# Now connecting to the RDS database

conn = mysql.connect(user=u,password=p,database=db,host=h)

# Now generating a SQL language cursor 
cur=conn.cursor()

# Now we can write the SQL query
cur.execute("show tables;")

# Now printing the result
print(cur.fetchall())

# Closing the connection to the database
conn.close()


