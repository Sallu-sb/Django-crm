#Install Mysl on computer
#pip install-mysql
#pip install-mysql-Connector 
#pip install-mysql-Connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123.'
    )

    #prepare a cursor object

cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL Done!")