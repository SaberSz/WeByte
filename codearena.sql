-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 07, 2018 at 05:48 AM
-- Server version: 5.6.34-log
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codearena`
--
CREATE DATABASE IF NOT EXISTS `codearena` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `codearena`;

-- --------------------------------------------------------

--
-- Table structure for table `competitions`
--

DROP TABLE IF EXISTS `competitions`;
CREATE TABLE `competitions` (
  `Compid` varchar(100) NOT NULL,
  `cName` varchar(100) NOT NULL,
  `Typecmp` int(1) NOT NULL DEFAULT '2' COMMENT '0,1,2',
  `Des` varchar(1000) NOT NULL,
  `imgs` longblob,
  `duration` varchar(20) NOT NULL DEFAULT '3 hours',
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `problems`
--

DROP TABLE IF EXISTS `problems`;
CREATE TABLE `problems` (
  `Compid` varchar(100) NOT NULL,
  `probno` int(11) NOT NULL,
  `probstmt` mediumtext NOT NULL,
  `probname` varchar(100) NOT NULL,
  `testcase` int(11) NOT NULL COMMENT '0,1,2',
  `probinput` varchar(200) NOT NULL,
  `proboutput` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ranks`
--

DROP TABLE IF EXISTS `ranks`;
CREATE TABLE `ranks` (
  `Email` varchar(60) NOT NULL,
  `Competionid` varchar(100) NOT NULL,
  `Rank` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
CREATE TABLE `results` (
  `competitionsid` varchar(100) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `problemid` int(11) NOT NULL,
  `submission` varchar(10000) NOT NULL,
  `Solved` tinyint(1) NOT NULL DEFAULT '0',
  `Submettime` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `Email` varchar(60) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `competitions`
--
ALTER TABLE `competitions`
  ADD PRIMARY KEY (`Compid`);

--
-- Indexes for table `problems`
--
ALTER TABLE `problems`
  ADD PRIMARY KEY (`Compid`,`probno`,`testcase`);

--
-- Indexes for table `ranks`
--
ALTER TABLE `ranks`
  ADD PRIMARY KEY (`Email`,`Competionid`,`Rank`),
  ADD KEY `Competionid` (`Competionid`);

--
-- Indexes for table `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`competitionsid`,`Email`,`problemid`),
  ADD KEY `Email` (`Email`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Email`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `problems`
--
ALTER TABLE `problems`
  ADD CONSTRAINT `problems_ibfk_1` FOREIGN KEY (`Compid`) REFERENCES `competitions` (`Compid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ranks`
--
ALTER TABLE `ranks`
  ADD CONSTRAINT `ranks_ibfk_1` FOREIGN KEY (`Email`) REFERENCES `users` (`Email`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ranks_ibfk_2` FOREIGN KEY (`Competionid`) REFERENCES `competitions` (`Compid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `results`
--
ALTER TABLE `results`
  ADD CONSTRAINT `results_ibfk_2` FOREIGN KEY (`Email`) REFERENCES `users` (`Email`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `results_ibfk_3` FOREIGN KEY (`competitionsid`) REFERENCES `competitions` (`Compid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
