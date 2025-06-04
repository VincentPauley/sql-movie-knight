For now this runs in container, have not set it up to run locally yet.

API Design

## movies

GET /movies - paginated way to look through movies - QUERY params: allow for genres, year, year range, and rating, reviews to be queried for

POST /movie - add a movie with all the extra stuff like genres etc

PATCH /movie - update anything related to a movie

## genres

[X] - GET /genres - receive all genre data

POST /genre - add a new genre

PATCH /genre - change either name or level of a genre

up next: ability to pass genres into movie search...
