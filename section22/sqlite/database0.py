import sqlite3

#conn = sqlite3.connect(':memory:')
#createa a database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

# createa a table
# NULL, INTEGER(NUMBER), REAL(DECIMAL), TEXT ,BLOB(ANOTHER FILE MP3)
c.execute("""CREATE TABLE customers(
first_name TEXT,
last_name TEXT,
email TEXT    
)""")

c.execute("INSERT INTO customers VALUES ('um', 'guitar','ajmalnizam246@gmail.com')")

#inserting many customers
many_customers = [
    ('ummj','muk', 'ummj@gmal'),
    ('jech', 'john', 'jech@gail.com'),
      ('hazr', 'shaji', 'jh@gmail.com'),   
  ]
c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customers)

# --------------------------------
c.execute("SELECT * FROM customers")

# print(c.fetchall())
# print(c.fetchone()[1])
#print(c.fetchmany(3))

items = c.fetchall()
# print(items)
print("NAME" + '\t\t'  + ' mailid')
print("-----------------------")
for item in items:
    # print(item[0])
    print(item[0], item[1] + "\t\t" + item[2])

# ---------------------------
# primary key
c.execute("SELECT  rowid, * FROM customers")
c.execute("SELECT *FROM customers WHERE first_name = 'aju' ")
c.execute("SELECT * FROM customers WHERE first_name LIKE  'aj%' ")
c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com' ")

# ----------------------------
# updatee records
c.execute("""UPDATE customers SET first_name = 'ajmal'
          WHERE rowid = '1'
""")

# ------------------
# delete record
c.execute("DELETE FROM customers where rowid = 8")

# ---------------
# order by rowid ASC DESC and column name
c.execute("SELECT rowid, * FROM customers ORDER BY first_name")
##and or

c.execute("""SELECT rowid, * FROM customers 
          WHERE last_name LIKE 'niz%' OR first_name = 'jec' 
          
          """)

c.execute("""SELECT rowid, * FROM customers 
          WHERE first_name LIKE 'aj%' and rowid = 2
          
          """)


# -----------------
# limiting result
c.execute("SELECT rowid, * FROM customers ORDER BY first_name LIMIT 2 ")


# -----------------
# dropping table

c.execute("DROP TABLE customers")
conn.commit


c.execute("SELECT * FROM customers")

items = c.fetchall()
for item in items:
    print(item)


#commit our command
conn.commit()

#close our connection
conn.close