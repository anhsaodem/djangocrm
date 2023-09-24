# INSTALL Mysql on computer
# https://dev.mysql.com/dowloads/installer
# pip install mysql
# pip install mysql-conector
# pip install mysql-conector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345',
    auth_plugin='mysql_native_password'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dcrmproject")
print('ALL DONE')