-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `TaskList` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `TaskList`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `task_list`;
CREATE TABLE IF NOT EXISTS `task_list` (
    `task_id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` varchar(64) NOT NULL,
    `task_description` varchar(30) NOT NULL,
    `status` boolean NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `task_list`
--

INSERT INTO `task_list` (`email`, `task_description`, `status`) VALUES
('huiqing.koh.2020@smu.edu.sg', 'esm change report', 'false'),
('huiqing.koh.2020@smu.edu.sg', 'analytics wireframe', 'false'),
('huiqing.koh.2020@smu.edu.sg', 'task list backend', 'false'),
('sanchanag.2020@smu.edu.sg', 'spotify api', 'false'),
('sanchanag.2020@smu.edu.sg', 'gcal api', 'false'),
('sophia.chow.2020@smu.edu.sg', 'sleep', 'false'),
('sophia.chow.2020@smu.edu.sg', 'sleep more', 'false');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
