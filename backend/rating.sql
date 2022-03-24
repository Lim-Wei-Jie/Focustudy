CREATE SCHEMA IF NOT EXISTS rating;
USE rating;

DROP TABLE IF EXISTS rating;
CREATE TABLE rating
(
    ratingId INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(320) NOT NULL,
    productivity INT  NOT NULL,
    DateInserted   datetime DEFAULT CURRENT_TIMESTAMP
);