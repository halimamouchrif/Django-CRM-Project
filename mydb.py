import mysql.connector


dataBase = mysql.connector.connect(
    host= '127.0.0.1',
    user ='root',
    passwd ='password123',
    auth_plugin = 'mysql_native_password',
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dcrmdb")

print("db successfully created")