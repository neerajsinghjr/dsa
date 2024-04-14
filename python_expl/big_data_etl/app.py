# database connection over here;;
from mysql.connector import connect
import traceback


database = '13karat'
user = 'postgres'
password = 'LYTYLWyLDSepxpwLr5fd'
host = 'karat-qa.cwre8jjo7pp9.ap-south-1.rds.amazonaws.com'
port = '5432'
try:
    con_db = connect(read_default_file='/Users/neeraj/Downloads/sql.config')
    print("Database connected successfully")
    con_db.close()

except Exception as ex:
    print(f"Database Connection Error: {traceback.format_exc()}")
