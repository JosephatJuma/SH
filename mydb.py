import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
   
)
# Prapare a curser object
cursorObject=database.cursor()

#Create A database
cursorObject.execute("CREATE DATABASE staff_hierarchy")

print("Database Created!")

