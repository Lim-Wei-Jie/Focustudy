CREATE SCHEMA IF NOT EXISTS activity_log;
USE activity_log;

DROP TABLE IF EXISTS activity_log;
CREATE TABLE activity_log
(
    activityId INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(320) NOT NULL,
    date VARCHAR(320) NOT NULL,
    duration INT NOT NULL,
    tasks VARCHAR(1000) NOT NULL
);