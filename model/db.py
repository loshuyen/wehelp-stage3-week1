from mysql.connector.pooling import MySQLConnectionPool
import os

dbconfig = {
  "host": "rds-mysql-shuyen.c7wya4me63ty.us-west-2.rds.amazonaws.com",
  "database": "demoTask",
  "user": "admin",
  "password": os.getenv("RDS_PASSWORD")
}

pool = MySQLConnectionPool(pool_name = "mypool", pool_size = 20, **dbconfig)

def create_message(content, image_name):
    try:
        db = pool.get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO message (content, image_name) VALUES (%s, %s)", (content, image_name))
        db.commit()
    finally:
        cursor.close()
        db.close()
def all_message() -> list[dict]:
    try:
        db = pool.get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT content, image_name FROM message;")
        messages = cursor.fetchall()
        data = []
        if not messages:
            return None
        for message in messages:
            data.append({"content": message[0], "image": message[1]})
        return data
    finally:
        cursor.close()
        db.close()