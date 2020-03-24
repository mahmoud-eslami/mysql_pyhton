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

customCursor.execute('show databases')
customCursor.execute('show tables')
customCursor.execute('desc user')
customCursor.execute('select * from user')

    
print('Please Enter Id :')    
personId = input()    
intPersonId = int(personId)

print('Please Enter Email :')    

email = input()
print('Please Enter userName :')    

username = input()
print('Please Enter passWord :')    

password = input()


query = (f'INSERT INTO user VALUES({intPersonId},"{email}","{username}","{password}")')
show_column = 'SELECT * FROM user'

customCursor.execute(query)
customCursor.execute(show_column)

for x in customCursor:
    print(x)


