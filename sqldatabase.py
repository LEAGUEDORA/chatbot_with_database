import sqlite3
from database import database, ans
import random

conn = sqlite3.connect('User_Data.db')

print('ConnectedSuccesfully')

conn.execute('''DROP TABLE USERS''')

conn.execute(''' CREATE TABLE USERS
(ID INT PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL,
         KD INT NOT NULL,
         TIER CHAR(15),
         SERVER          CHAR(15),
         WIN INT NOT NULL,
         TOP10 INT NOT NULL);''')




for user_id in range(10000, 20000):
    conn.execute(''' INSERT INTO USERS ( ID, NAME, KD, TIER, SERVER, WIN, TOP10) VALUES (?,?,?,?,?,?,?) ''',(user_id, random.choice(database.Names), round(random.uniform(1,5), 2), random.choice(database.Tier), random.choice(database.Server), random.randrange(10,30), random.randrange(60, 90)))


conn.commit()



conn.close()