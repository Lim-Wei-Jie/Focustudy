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
("b@gmail.com", "2022-03-25", 2313),

/* test order by */
("esdg2t1@gmail.com", "2022-03-24", 7583),

/* test group by */
("esdg2t1@gmail.com", "2022-03-25", 4135),
("esdg2t1@gmail.com", "2022-03-25", 4263),
("esdg2t1@gmail.com", "2022-03-25", 7654),

("esdg2t1@gmail.com", "2022-03-23", 1453),
("esdg2t1@gmail.com", "2022-03-23", 5143),

("esdg2t1@gmail.com", "2022-03-22", 4326),
("esdg2t1@gmail.com", "2022-03-22", 3825),
("esdg2t1@gmail.com", "2022-03-22", 1453),
("esdg2t1@gmail.com", "2022-03-22", 5143),

("esdg2t1@gmail.com", "2022-03-21", 3422),
("esdg2t1@gmail.com", "2022-03-21", 6754)