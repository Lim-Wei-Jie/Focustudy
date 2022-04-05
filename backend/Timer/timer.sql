CREATE SCHEMA IF NOT EXISTS timer;
USE timer;

DROP TABLE IF EXISTS timer;
CREATE TABLE timer (
	timeId INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(320) NOT NULL,
	startDate DATE NOT NULL,
	duration INT NOT NULL);

INSERT INTO timer (email, startDate, duration) VALUES

/* test email filter */
("a@gmail.com", "2022-03-25", 2313),

("esdg2t1@gmail.com", "2022-03-25", 4135),
("esdg2t1@gmail.com", "2022-03-25", 4263),
("esdg2t1@gmail.com", "2022-03-25", 7654)