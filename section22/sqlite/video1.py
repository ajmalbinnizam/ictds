import sqlite3

#conn = sqlite3.connect(':memory:')
#createa a database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#createa a table
c.execute("""CREATE TABLE customers(
first_name DATATYPE,
last_name DATATYPE,
email DATATYPE    
)""")

c.execute("""CREATE TABLE customers(
first_name TEXT,
last_nameTEXT,
email TEXT
)""")
#NULL, INTEGER(NUMBER), REAL(DECIMAL), TEXT ,BLOB(ANOTHER FILE MP3)

#commit our command
conn.commit()

#close our connection
conn.close








