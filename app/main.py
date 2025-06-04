import os

import mysql.connector
from fastapi import Depends, FastAPI, Query

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


async def get_all_genre_data(
    conn: mysql.connector.connection.MySQLConnection = Depends(get_db_connection),
):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM genres;")
        genres = cursor.fetchall()
        cursor.close()

        genre_list = []

        for genre in genres:
            genre_list.append({"id": genre[0], "name": genre[1], "level": genre[2]})
        return genre_list
    except mysql.connector.Error as err:
        return {"error": str(err)}


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


@app.get("/movies")
async def get_movies(
    conn: mysql.connector.connection.MySQLConnection = Depends(get_db_connection),
    genres: str = Query(None, description="one or more genre ids"),
):
    genre_list = []

    if genres and "," in genres:
        for genre_id in genres.split(","):
            genre_list.append(genre_id)
    elif genres:
        genre_list.append(genres)

    return {"genre_list": genre_list}


@app.get("/genres")
async def get_genres(
    conn: mysql.connector.connection.MySQLConnection = Depends(get_db_connection),
):
    try:
        genres = await get_all_genre_data(conn)

        return {"genres": genres}
    except mysql.connector.Error as err:
        return {"error": f"error happened: {err}"}
