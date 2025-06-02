# Movie Knight

This is a full-stack app that I use with my wife to keep track of movies that we like/dislike. It helps us figure out what we want to watch next

## Getting Started

### System Requirements

- Docker

### Setup the app locally

clone this repo and create a `.env` at the root of the project based on `.env.example`. Be sure to set passwords in here.

From there just run the docker compose and all of the app services will be started and you can begin using the app.

```bash
docker-compose up
```

- tags table
- tag junctions table

  - move genre level 3 into tags, "cheesey", "culinary" etc

Up Next:

Need to have an environment file to hold the DB info and pass it to the API service as well.
