CREATE SCHEMA IF NOT EXISTS rating;
USE rating;

DROP TABLE IF EXISTS rating;
CREATE TABLE rating
(
    ratingId INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(320) NOT NULL,
    productivity INT  NOT NULL,
    currentDate VARCHAR(320) NOT NULL,
    partDay VARCHAR(320) NOT NULL,
    morningGPA INT  NOT NULL,
    afternoonGPA INT  NOT NULL,
    nightGPA INT  NOT NULL
);