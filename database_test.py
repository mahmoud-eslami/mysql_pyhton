# first you need to a plugin for connect to mysql 
# for example we have two plugin 1- pyconnect and 2- python|connector
# we use python connector in this example


import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    database='userdata'
)

customCursor = mydb.cursor()

# customCursor.execute('show databases')
# customCursor.execute('show tables')
# customCursor.execute('desc user')
customCursor.execute('select * from user')

for x in customCursor:
    print(x)
    
