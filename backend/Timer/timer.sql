CREATE SCHEMA IF NOT EXISTS timer;
USE timer;

DROP TABLE IF EXISTS timer;
CREATE TABLE timer (
	timeId INT AUTO_INCREMENT PRIMARY KEY,
	startDate DATE NOT NULL,
	duration INT NOT NULL);