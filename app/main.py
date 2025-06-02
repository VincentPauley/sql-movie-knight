import os

import mysql.connector
from fastapi import FastAPI

app = FastAPI()

MYSQL_HOST = os.getenv("MYSQL_HOST", "db")  # Use the container name as the hostname
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "default_database")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")


@app.get("/10-random-movies")
def read_root():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            database=MYSQL_DATABASE,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
        )
        cursor = conn.cursor()

        # Example query: Fetch all rows from a table named 'movies'
        cursor.execute("SELECT * FROM movies ORDER BY RAND() LIMIT 10")
        movies = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        return {"message": "here are 10 random movies", "movies": movies}
    except mysql.connector.Error as err:
        return {"error": f"error happened: {err}"}
