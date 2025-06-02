import os

import mysql.connector
from fastapi import Depends, FastAPI

app = FastAPI()

MYSQL_HOST = os.getenv("MYSQL_HOST", "db")  # Use the container name as the hostname
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "default_database")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")


def get_db_connection():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
    )
    try:
        yield conn
    finally:
        conn.close()


@app.get("/10-random-movies")
def get_random_movies(
    conn: mysql.connector.connection.MySQLConnection = Depends(get_db_connection),
):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM movies ORDER BY RAND() LIMIT 10")
        movies = cursor.fetchall()

        cursor.close()

        return {"message": "here are 10 random movies", "movies": movies}
    except mysql.connector.Error as err:
        return {"error": f"error happened: {err}"}


@app.get("/genres")
def get_genres(
    conn: mysql.connector.connection.MySQLConnection = Depends(get_db_connection),
):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()

        cursor.close()

        return {"genres": genres}
    except mysql.connector.Error as err:
        return {"error": f"error happened: {err}"}
