import os

import mysql.connector
from fastapi import Depends, FastAPI, Query
from fastapi.responses import JSONResponse

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


async def validate_genre_ids(
    genre_ids: list, conn: mysql.connector.connection.MySQLConnection
):
    # Fetch all genres from the database
    all_genres = await get_all_genre_data(conn)

    # Extract genre IDs from the database result
    valid_genre_ids = {
        genre["id"] for genre in all_genres
    }  # Use a set for faster lookup

    # Find invalid genre IDs
    invalid_ids = [
        genre_id for genre_id in genre_ids if genre_id not in valid_genre_ids
    ]

    # Return a dictionary with "valid" and optionally "invalid_ids"
    return {
        "valid": len(invalid_ids) == 0,
        **({"invalid_ids": invalid_ids} if invalid_ids else {}),
    }


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


async def get_movies_by_genre_ids(
    genre_ids: list, conn: mysql.connector.connection.MySQLConnection
):
    try:
        # Create a cursor
        cursor = conn.cursor(dictionary=True)  # Fetch rows as dictionaries

        # Prepare the SQL query to fetch movies and all their associated genres
        query = """
            SELECT m.id AS movie_id, m.title, m.year, m.rated, g.id AS genre_id, g.genre_name AS genre_name
            FROM movies AS m
            INNER JOIN movie_genres AS mg ON m.id = mg.movie_id
            INNER JOIN genres AS g ON mg.genre_id = g.id
            WHERE m.id IN (
                SELECT DISTINCT mg.movie_id
                FROM movie_genres AS mg
                WHERE mg.genre_id IN (%s)
            )
        """ % (", ".join(["%s"] * len(genre_ids)))  # Dynamically create placeholders

        # Execute the query with genre IDs
        cursor.execute(query, genre_ids)

        # Fetch all rows
        rows = cursor.fetchall()

        # Close the cursor
        cursor.close()

        # Group genres by movie
        movies = {}
        for row in rows:
            movie_id = row["movie_id"]
            if movie_id not in movies:
                movies[movie_id] = {
                    "id": movie_id,
                    "title": row["title"],
                    "year": row["year"],
                    "rated": row["rated"],
                    "genres": [],
                }
            movies[movie_id]["genres"].append(
                {"id": row["genre_id"], "name": row["genre_name"]}
            )

        # Return the list of movies with all their associated genres
        return list(movies.values())
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
    # TODO: ideally would know what type of factors are being searched for
    # and then call specific queries that could perform task as needed.
    genre_list = []

    if genres and "," in genres:
        for genre_id in genres.split(","):
            genre_list.append(genre_id)
    elif genres:
        genre_list.append(genres)

    if len(genre_list):
        genre_validation_result = await validate_genre_ids(genre_list, conn)

        if not genre_validation_result["valid"]:
            return JSONResponse(
                status_code=400,
                content={
                    "message": "Invalid genre id(s) were provided",
                    "invalid_ids": genre_validation_result["invalid_ids"],
                },
            )
        else:
            result = await get_movies_by_genre_ids(genre_list, conn)

            return {"message": "ready for looking up with genres!", "result": result}

    return {"message": "hit the default response"}


@app.get("/genres")
async def get_genres(
    conn: mysql.connector.connection.MySQLConnection = Depends(get_db_connection),
):
    try:
        genres = await get_all_genre_data(conn)

        return {"genres": genres}
    except mysql.connector.Error as err:
        return {"error": f"error happened: {err}"}
