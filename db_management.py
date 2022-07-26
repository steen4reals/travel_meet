from mysql.connector import connect
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME


def get_db_connection():
    connection = connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME)
    return connection


def get_posts():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT * 
                                FROM Post AS p """)
            results = cursor.fetchall()
            return results


print(get_posts())


