import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DB_PORT

try:
    mydb = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASSWD,
        database = DB_NAME,
        port = DB_PORT
    )
except NameError:
    print(f"Could not connect to the {DB_NAME} database: " + NameError)
    exit()
else:
    print(f"Connected to the {DB_NAME} database.")

mycursor = mydb.cursor(buffered=True, dictionary=True)