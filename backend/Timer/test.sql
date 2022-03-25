INSERT INTO timer (email, startDate, duration) VALUES

/* test email filter */
("b@gmail.com", "2022-03-25", 3600),

/* test group by */
("a@gmail.com", "2022-03-25", 3600),
("a@gmail.com", "2022-03-25", 3600),
("a@gmail.com", "2022-03-25", 5400),

("a@gmail.com", "2022-03-24", 1800),
("a@gmail.com", "2022-03-23", 7200),
("a@gmail.com", "2022-03-22", 5438),
("a@gmail.com", "2022-03-21", 3297),
("a@gmail.com", "2022-03-20", 4327),
("a@gmail.com", "2022-03-19", 9437),

/* test last 7 days */
("a@gmail.com", "2022-03-18", 3154),

/* test this month */
("a@gmail.com", "2022-03-01", 8503),

/* test this year */
("a@gmail.com", "2022-02-01", 2349),

/* test all time */
("a@gmail.com", "2021-03-01", 1234)