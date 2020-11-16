import sqlite3

connect = sqlite3.connect('User_Data.db')

cursor = connect.execute(''' SELECT *  FROM USERS  WHERE ID = (?)''', (,))


for i in cursor:
    print(i)