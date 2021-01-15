import database2

# add a record to the database
# database2.add_one('ajmal', 'nizam', 'ajmalnizam369@gmail.com')


# delete record use rowid as string
# database2.delete_one('10')


# add many record 
# stuff = [('aju','new','@gmail.com'),
#          ('js','python', 'postgresql')]
# database2.add_many(stuff)

database2.email_lookup('ajmalnizam246@gmail.com')

# show all database
# database2.show_all()