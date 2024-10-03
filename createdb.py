import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DB_PORT

try:
    myconnection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASSWD,
        port = DB_PORT
    )
except NameError:
    print("Database connection failed: " + NameError)
    exit()
else:
    print("Database connection successful")

mycursor = myconnection.cursor(buffered=True)

create_db = f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"
mycursor.execute(create_db)

mycursor.execute("SHOW DATABASES")

for database in mycursor:
    print(database)