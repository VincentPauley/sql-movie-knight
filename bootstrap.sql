CREATE DATABASE IF NOT EXISTS movieknight;

CREATE USER IF NOT EXISTS 'movieknight_user'@'%' IDENTIFIED BY 'abc123';

GRANT ALL PRIVILEGES ON movieknight.* TO 'movieknight_user'@'%';

FLUSH PRIVILEGES;

USE movieknight;

-- create all tables
CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    rating VARCHAR(10)
);
CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    level TINYINT NOT NULL CHECK (level BETWEEN 0 AND 9)
);
CREATE TABLE movie_genres (
    movie_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (movie_id, genre_id), -- < ensures no duplicate pairs
    -- this ensures movie_id and genre_id exist in the respective tables
    FOREIGN KEY (movie_id) REFERENCES movie(id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE reviews (
    movie_id INT NOT NULL,
    reviewer_id INT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 0 AND 100),
    PRIMARY KEY (movie_id, reviewer_id),
    FOREIGN KEY (movie_id) REFERENCES movie(id) ON DELETE CASCADE,
    FOREIGN KEY (reviewer_id) REFERENCES reviewers(id) ON DELETE CASCADE
);