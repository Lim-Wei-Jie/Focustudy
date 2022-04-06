CREATE SCHEMA IF NOT EXISTS rating;
USE rating;

DROP TABLE IF EXISTS rating;
CREATE TABLE rating (
	ratingId INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(320) NOT NULL,
	currentDate DATE NOT NULL,
	rating INT NOT NULL);

INSERT INTO rating (email, currentDate, rating) VALUES

/* test email filter */
("c@gmail.com", "2022-03-25", 5),

/* test order by */
("esdg2t1@gmail.com", "2022-03-24", 5),

/* test group by */
("esdg2t1@gmail.com", "2022-03-25", 4),
("esdg2t1@gmail.com", "2022-03-25", 4),
("esdg2t1@gmail.com", "2022-03-25", 2),

("esdg2t1@gmail.com", "2022-03-23", 1),
("esdg2t1@gmail.com", "2022-03-23", 5),

("esdg2t1@gmail.com", "2022-03-22", 4),
("esdg2t1@gmail.com", "2022-03-22", 3),
("esdg2t1@gmail.com", "2022-03-22", 1),
("esdg2t1@gmail.com", "2022-03-22", 5),

("esdg2t1@gmail.com", "2022-03-21", 3),
("esdg2t1@gmail.com", "2022-03-21", 2)