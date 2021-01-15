import sqlite3

#conn = sqlite3.connect(':memory:')
#createa a database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()
c.execute("""CREATE TABLE customers(
first_name TEXT,
last_name TEXT,
email TEXT    
)""")

c.execute("INSERT INTO customers VALUES ('aju', 'nizam','ajmalnizam246@gmail.com')")

#inserting many customers
many_customers = [
    ('ummj','muk', 'ummj@gmal'),
    ('jech', 'john', 'jech@gail.com'),
      ('hazr', 'shaji', 'jh@gmail.com'),   
  ]
c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customers)

c.execute("Select rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)





#commit our command
conn.commit()

#close our connection
conn.close








