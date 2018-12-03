-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 03, 2018 at 04:32 AM
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
  `imgs` varchar(100) DEFAULT NULL,
  `duration` varchar(20) NOT NULL DEFAULT '3 hours',
  `Date` date NOT NULL,
  `Time1` time NOT NULL,
  `horc` int(1) NOT NULL COMMENT '0-h 1-r',
  `Org` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `competitions`
--

INSERT INTO `competitions` (`Compid`, `cName`, `Typecmp`, `Des`, `imgs`, `duration`, `Date`, `Time1`, `horc`, `Org`) VALUES
('1', 'August Circuits', 0, 'We are conducting a marathon competitive programming challenge August Circuits starting from 17th August 2018. The objective of August Circuits is to challenge the talented and creative minds in competitive programming with some interesting algorithmic problems.', 'sample-1.jpg', '3 hours', '2018-08-17', '05:00:00', 1, 'IBM'),
('2', 'June easy', 0, 'We are running a short 3 hour contest on 1st June. There will be 6 algorithmic problems, for beginners in competitive coding. This contest is a Rated contest and open for all.', 'desk.jpg', '3 hours', '2018-06-01', '05:25:34', 0, 'WeByte'),
('3', 'August Easy', 3, 'You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.', 'loft.jpg', '3 hours', '2018-11-29', '14:10:00', 1, 'Infosys'),
('4', 'Winds of Winter', 0, 'The Winds of Winter will take readers farther north than any of the previous books, and the Others will appear in the book.', 'sample-1.jpg', '3 hours', '2018-11-29', '14:00:00', 0, 'HBO'),
('5', 'September Codethon', 0, 'We are conducting a marathon competitive programming challenge August Circuits starting from 17th August 2018. The objective of August Circuits is to challenge the talented and creative minds in competitive programming with some interesting algorithmic problems.', 'sample-1.jpg', '3 hours', '2018-09-17', '05:00:00', 1, 'IBM'),
('6', 'January easy', 2, 'We are running a short 3 hour contest on 1st January. There will be 6 algorithmic problems, for beginners in competitive coding. This contest is a Rated contest and open for all.', 'desk.jpg', '3 hours', '2019-01-01', '05:25:34', 1, 'WeByte'),
('7', 'Dance of Dragons', 0, 'The Dance of Dragons will take readers farther north than any of the previous books, and the Others will appear in the book.', 'sample-1.jpg', '3 hours', '2018-11-13', '13:00:00', 0, 'HBO'),
('8', 'October Easy', 0, 'We are conducting a marathon competitive programming challenge August Circuits starting from 17th August 2018. The objective of August Circuits is to challenge the talented and creative minds in competitive programming with some interesting algorithmic problems.', 'sample-1.jpg', '3 hours', '2018-10-17', '05:00:00', 1, 'Mphasis'),
('9', 'February easy', 2, 'We are running a short 3 hour contest on 1st february. There will be 6 algorithmic problems, for beginners in competitive coding. This contest is a Rated contest and open for all.', 'desk.jpg', '3 hours', '2019-02-01', '05:25:34', 0, 'WeByte');

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

DROP TABLE IF EXISTS `contactus`;
CREATE TABLE `contactus` (
  `Name` varchar(100) NOT NULL,
  `Email` varchar(1000) NOT NULL,
  `Subject` varchar(10000) NOT NULL,
  `Message` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contactus`
--

INSERT INTO `contactus` (`Name`, `Email`, `Subject`, `Message`) VALUES
('suck_balls_deep', 'admin@gmail.com', 'General Issue', 'Apples and oranges for me.'),
('suck_balls_deep', 'admin@gmail.com', 'General Issue', 'Apples and oranges for me. Also a Pepsi.');

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
  `probinput` longtext NOT NULL,
  `proboutput` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `problems`
--

INSERT INTO `problems` (`Compid`, `probno`, `probstmt`, `probname`, `testcase`, `probinput`, `proboutput`) VALUES
('1', 1, 'In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.\r\n\r\nINPUT :\r\n\r\nGiven a series of numbers(inputs) and each number(N) on a newline.\r\n\r\nOUTPUT :\r\n\r\nFor the given input , Output the required ans.\r\n\r\nNOTE :\r\n\r\nNo. of test cases are unknown.\r\n\r\nUse Faster I/O Techniques.\r\n\r\nCONSTRAINTS :\r\n\r\n0<= N <= 10^18', 'MYSTERY', 1, 'HCFJDPASAVRBRVXTDOSIAYMGQLMKII.txt', 'sadfasdfsdafasdf.txt'),
('1', 1, 'In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.\r\n\r\nINPUT :\r\n\r\nGiven a series of numbers(inputs) and each number(N) on a newline.\r\n\r\nOUTPUT :\r\n\r\nFor the given input , Output the required ans.\r\n\r\nNOTE :\r\n\r\nNo. of test cases are unknown.\r\n\r\nUse Faster I/O Techniques.\r\n\r\nCONSTRAINTS :\r\n\r\n0<= N <= 10^18', 'MYSTERY', 2, '36c2ad6c84-input-36c27e1.txt.clean.txt', 'NDDEELMJBZSXVGRYEDEBOBQNFTOTYL.txt'),
('1', 2, 'Suzie came over to Monk\'s place today with a box of Monk\'s favorite cookies! But Monk has to play a game with her in order to win the cookies.\r\nSuzie takes out N balls from her bag, each ball having an integer on it. All the integers are 32-bit. She places all these balls in a box and closes it. The game starts by Monk choosing an integer from 0 to 31, representing a bit position. It is called as Monk\'s chosen bit. Post this, Suzie draws 1 balls from the box randomly and notes the integers on them. The rule is simple, Monk wins if Monk\'s chosen bit is set in the binary representation of the drawn ball. Help Monk choose a bit that maximizes his probability of winning the game! If there are multiple bit positions having the same probability, choose the smallest one.\r\n\r\nInput:\r\nThe first line consists of an integer T. T testcases follow. The first line of each testcase consists of an integer N.\r\nIn next N lines, each line will contain 1 integer denoting the integers on the ball.\r\n\r\nOutput:\r\nFor each testcase, print the answer in a single line.', 'Monk and the box of cookies', 1, 'CXHMGTUEQZXRXUBSKJNOGZNWGXROLK.txt', 'CXHMGTUEQZXRXUBSKJNOGZNWG234XROLK.txt'),
('1', 2, 'Suzie came over to Monk\'s place today with a box of Monk\'s favorite cookies! But Monk has to play a game with her in order to win the cookies.\r\nSuzie takes out N balls from her bag, each ball having an integer on it. All the integers are 32-bit. She places all these balls in a box and closes it. The game starts by Monk choosing an integer from 0 to 31, representing a bit position. It is called as Monk\'s chosen bit. Post this, Suzie draws 1 balls from the box randomly and notes the integers on them. The rule is simple, Monk wins if Monk\'s chosen bit is set in the binary representation of the drawn ball. Help Monk choose a bit that maximizes his probability of winning the game! If there are multiple bit positions having the same probability, choose the smallest one.\r\n\r\nInput:\r\nThe first line consists of an integer T. T testcases follow. The first line of each testcase consists of an integer N.\r\nIn next N lines, each line will contain 1 integer denoting the integers on the ball.\r\n\r\nOutput:\r\nFor each testcase, print the answer in a single line.', 'Monk and the box of cookies', 2, 'ee3f3fb025-input-ee3ed76.txt.clean.txt', 'e9886f5a11-input-e988145.txt.cleanss.txt'),
('1', 3, 'Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project named 21 Lane, but he is stuck at a tricky segment of his code.\r\n\r\nHihi wants to assign some random IP addresses to users, but he won\'t use rand(). He wants to change the current IP of the user\'s computer to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.\r\n\r\nSmart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed IP to the required IP X as mentioned above.\r\n\r\nOK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form\r\n\r\nInput :\r\n\r\nFirst line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)\r\n\r\nOutput :\r\n\r\nPrint T lines, each containing an integer X, the required IP.(don\'t worry Hihi will decode X to obtain final IP address)', 'Hihi and Crazy Bits', 1, '00bee00c11-sample-input-00be49f.txt', '01f3c4d811-sample-output-01f3124.txt'),
('1', 3, 'Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project named 21 Lane, but he is stuck at a tricky segment of his code.\r\n\r\nHihi wants to assign some random IP addresses to users, but he won\'t use rand(). He wants to change the current IP of the user\'s computer to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.\r\n\r\nSmart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed IP to the required IP X as mentioned above.\r\n\r\nOK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form\r\n\r\nInput :\r\n\r\nFirst line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)\r\n\r\nOutput :\r\n\r\nPrint T lines, each containing an integer X, the required IP.(don\'t worry Hihi will decode X to obtain final IP address)', 'Hihi and Crazy Bits', 2, 'e9886f5a11-input-e988145.txt.clean (1).txt', 'e9cc5c2411-output-e988165.txt'),
('1', 4, 'Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.\r\n\r\nSo, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.\r\n\r\nHe gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is \"101\", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.\r\n\r\nHelp Subham to solve this problem.\r\n\r\n\r\nINPUT:\r\nThe first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.\r\n\r\nOUTPUT:\r\nPrint the answer for every test case in a new line.', 'Subham and Binary Strings', 1, '3e6748eef8-sample-input-3e6699c.txt', '42a6303cf8-sample-output-42a5bb0.txt'),
('1', 4, 'Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.\r\n\r\nSo, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.\r\n\r\nHe gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is \"101\", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.\r\n\r\nHelp Subham to solve this problem.\r\n\r\n\r\nINPUT:\r\nThe first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.\r\n\r\nOUTPUT:\r\nPrint the answer for every test case in a new line.', 'Subham and Binary Strings', 2, 'c674ff08f8-in09.txt', 'c69115bcf8-out09.txt'),
('2', 1, 'In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.\r\n\r\nINPUT :\r\n\r\nGiven a series of numbers(inputs) and each number(N) on a newline.\r\n\r\nOUTPUT :\r\n\r\nFor the given input , Output the required ans.\r\n\r\nNOTE :\r\n\r\nNo. of test cases are unknown.\r\n\r\nUse Faster I/O Techniques.\r\n\r\nCONSTRAINTS :\r\n\r\n0<= N <= 10^18', 'MYSTERY', 1, 'HCFJDPASAVRBRVXTDOSIAYMGQLMKII.txt', 'sadfasdfsdafasdf.txt'),
('2', 1, 'In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.\r\n\r\nINPUT :\r\n\r\nGiven a series of numbers(inputs) and each number(N) on a newline.\r\n\r\nOUTPUT :\r\n\r\nFor the given input , Output the required ans.\r\n\r\nNOTE :\r\n\r\nNo. of test cases are unknown.\r\n\r\nUse Faster I/O Techniques.\r\n\r\nCONSTRAINTS :\r\n\r\n0<= N <= 10^18', 'MYSTERY', 2, '36c2ad6c84-input-36c27e1.txt.clean.txt', 'NDDEELMJBZSXVGRYEDEBOBQNFTOTYL.txt'),
('2', 2, 'Suzie came over to Monk\'s place today with a box of Monk\'s favorite cookies! But Monk has to play a game with her in order to win the cookies.\r\nSuzie takes out N balls from her bag, each ball having an integer on it. All the integers are 32-bit. She places all these balls in a box and closes it. The game starts by Monk choosing an integer from 0 to 31, representing a bit position. It is called as Monk\'s chosen bit. Post this, Suzie draws 1 balls from the box randomly and notes the integers on them. The rule is simple, Monk wins if Monk\'s chosen bit is set in the binary representation of the drawn ball. Help Monk choose a bit that maximizes his probability of winning the game! If there are multiple bit positions having the same probability, choose the smallest one.\r\n\r\nInput:\r\nThe first line consists of an integer T. T testcases follow. The first line of each testcase consists of an integer N.\r\nIn next N lines, each line will contain 1 integer denoting the integers on the ball.\r\n\r\nOutput:\r\nFor each testcase, print the answer in a single line.', 'Monk and the box of cookies', 1, 'CXHMGTUEQZXRXUBSKJNOGZNWGXROLK.txt', 'CXHMGTUEQZXRXUBSKJNOGZNWG234XROLK.txt'),
('2', 2, 'Suzie came over to Monk\'s place today with a box of Monk\'s favorite cookies! But Monk has to play a game with her in order to win the cookies.\r\nSuzie takes out N balls from her bag, each ball having an integer on it. All the integers are 32-bit. She places all these balls in a box and closes it. The game starts by Monk choosing an integer from 0 to 31, representing a bit position. It is called as Monk\'s chosen bit. Post this, Suzie draws 1 balls from the box randomly and notes the integers on them. The rule is simple, Monk wins if Monk\'s chosen bit is set in the binary representation of the drawn ball. Help Monk choose a bit that maximizes his probability of winning the game! If there are multiple bit positions having the same probability, choose the smallest one.\r\n\r\nInput:\r\nThe first line consists of an integer T. T testcases follow. The first line of each testcase consists of an integer N.\r\nIn next N lines, each line will contain 1 integer denoting the integers on the ball.\r\n\r\nOutput:\r\nFor each testcase, print the answer in a single line.', 'Monk and the box of cookies', 2, 'ee3f3fb025-input-ee3ed76.txt.clean.txt', 'e9886f5a11-input-e988145.txt.cleanss.txt'),
('2', 3, 'Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project named 21 Lane, but he is stuck at a tricky segment of his code.\r\n\r\nHihi wants to assign some random IP addresses to users, but he won\'t use rand(). He wants to change the current IP of the user\'s computer to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.\r\n\r\nSmart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed IP to the required IP X as mentioned above.\r\n\r\nOK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form\r\n\r\nInput :\r\n\r\nFirst line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)\r\n\r\nOutput :\r\n\r\nPrint T lines, each containing an integer X, the required IP.(don\'t worry Hihi will decode X to obtain final IP address)', 'Hihi and Crazy Bits', 1, '00bee00c11-sample-input-00be49f.txt', '01f3c4d811-sample-output-01f3124.txt'),
('2', 3, 'Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project named 21 Lane, but he is stuck at a tricky segment of his code.\r\n\r\nHihi wants to assign some random IP addresses to users, but he won\'t use rand(). He wants to change the current IP of the user\'s computer to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.\r\n\r\nSmart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed IP to the required IP X as mentioned above.\r\n\r\nOK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form\r\n\r\nInput :\r\n\r\nFirst line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)\r\n\r\nOutput :\r\n\r\nPrint T lines, each containing an integer X, the required IP.(don\'t worry Hihi will decode X to obtain final IP address)', 'Hihi and Crazy Bits', 2, 'e9886f5a11-input-e988145.txt.clean (1).txt', 'e9cc5c2411-output-e988165.txt'),
('2', 4, 'Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.\r\n\r\nSo, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.\r\n\r\nHe gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is \"101\", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.\r\n\r\nHelp Subham to solve this problem.\r\n\r\n\r\nINPUT:\r\nThe first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.\r\n\r\nOUTPUT:\r\nPrint the answer for every test case in a new line.', 'Subham and Binary Strings', 1, '3e6748eef8-sample-input-3e6699c.txt', '42a6303cf8-sample-output-42a5bb0.txt'),
('2', 4, 'Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.\r\n\r\nSo, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.\r\n\r\nHe gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is \"101\", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.\r\n\r\nHelp Subham to solve this problem.\r\n\r\n\r\nINPUT:\r\nThe first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.\r\n\r\nOUTPUT:\r\nPrint the answer for every test case in a new line.', 'Subham and Binary Strings', 2, 'c674ff08f8-in09.txt', 'c69115bcf8-out09.txt'),
('3', 1, 'In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.\r\n\r\nINPUT :\r\n\r\nGiven a series of numbers(inputs) and each number(N) on a newline.\r\n\r\nOUTPUT :\r\n\r\nFor the given input , Output the required ans.\r\n\r\nNOTE :\r\n\r\nNo. of test cases are unknown.\r\n\r\nUse Faster I/O Techniques.\r\n\r\nCONSTRAINTS :\r\n\r\n0<= N <= 10^18', 'MYSTERY', 1, 'HCFJDPASAVRBRVXTDOSIAYMGQLMKII.txt', 'sadfasdfsdafasdf.txt'),
('3', 1, 'In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.\r\n\r\nINPUT :\r\n\r\nGiven a series of numbers(inputs) and each number(N) on a newline.\r\n\r\nOUTPUT :\r\n\r\nFor the given input , Output the required ans.\r\n\r\nNOTE :\r\n\r\nNo. of test cases are unknown.\r\n\r\nUse Faster I/O Techniques.\r\n\r\nCONSTRAINTS :\r\n\r\n0<= N <= 10^18', 'MYSTERY', 2, '36c2ad6c84-input-36c27e1.txt.clean.txt', 'NDDEELMJBZSXVGRYEDEBOBQNFTOTYL.txt'),
('3', 2, 'Suzie came over to Monk\'s place today with a box of Monk\'s favorite cookies! But Monk has to play a game with her in order to win the cookies.\r\nSuzie takes out N balls from her bag, each ball having an integer on it. All the integers are 32-bit. She places all these balls in a box and closes it. The game starts by Monk choosing an integer from 0 to 31, representing a bit position. It is called as Monk\'s chosen bit. Post this, Suzie draws 1 balls from the box randomly and notes the integers on them. The rule is simple, Monk wins if Monk\'s chosen bit is set in the binary representation of the drawn ball. Help Monk choose a bit that maximizes his probability of winning the game! If there are multiple bit positions having the same probability, choose the smallest one.\r\n\r\nInput:\r\nThe first line consists of an integer T. T testcases follow. The first line of each testcase consists of an integer N.\r\nIn next N lines, each line will contain 1 integer denoting the integers on the ball.\r\n\r\nOutput:\r\nFor each testcase, print the answer in a single line.', 'Monk and the box of cookies', 1, 'CXHMGTUEQZXRXUBSKJNOGZNWGXROLK.txt', 'CXHMGTUEQZXRXUBSKJNOGZNWG234XROLK.txt'),
('3', 2, 'Suzie came over to Monk\'s place today with a box of Monk\'s favorite cookies! But Monk has to play a game with her in order to win the cookies.\r\nSuzie takes out N balls from her bag, each ball having an integer on it. All the integers are 32-bit. She places all these balls in a box and closes it. The game starts by Monk choosing an integer from 0 to 31, representing a bit position. It is called as Monk\'s chosen bit. Post this, Suzie draws 1 balls from the box randomly and notes the integers on them. The rule is simple, Monk wins if Monk\'s chosen bit is set in the binary representation of the drawn ball. Help Monk choose a bit that maximizes his probability of winning the game! If there are multiple bit positions having the same probability, choose the smallest one.\r\n\r\nInput:\r\nThe first line consists of an integer T. T testcases follow. The first line of each testcase consists of an integer N.\r\nIn next N lines, each line will contain 1 integer denoting the integers on the ball.\r\n\r\nOutput:\r\nFor each testcase, print the answer in a single line.', 'Monk and the box of cookies', 2, 'ee3f3fb025-input-ee3ed76.txt.clean.txt', 'e9886f5a11-input-e988145.txt.cleanss.txt'),
('3', 3, 'Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project named 21 Lane, but he is stuck at a tricky segment of his code.\r\n\r\nHihi wants to assign some random IP addresses to users, but he won\'t use rand(). He wants to change the current IP of the user\'s computer to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.\r\n\r\nSmart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed IP to the required IP X as mentioned above.\r\n\r\nOK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form\r\n\r\nInput :\r\n\r\nFirst line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)\r\n\r\nOutput :\r\n\r\nPrint T lines, each containing an integer X, the required IP.(don\'t worry Hihi will decode X to obtain final IP address)', 'Hihi and Crazy Bits', 1, '00bee00c11-sample-input-00be49f.txt', '01f3c4d811-sample-output-01f3124.txt'),
('3', 3, 'Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project named 21 Lane, but he is stuck at a tricky segment of his code.\r\n\r\nHihi wants to assign some random IP addresses to users, but he won\'t use rand(). He wants to change the current IP of the user\'s computer to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.\r\n\r\nSmart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed IP to the required IP X as mentioned above.\r\n\r\nOK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form\r\n\r\nInput :\r\n\r\nFirst line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)\r\n\r\nOutput :\r\n\r\nPrint T lines, each containing an integer X, the required IP.(don\'t worry Hihi will decode X to obtain final IP address)', 'Hihi and Crazy Bits', 2, 'e9886f5a11-input-e988145.txt.clean (1).txt', 'e9cc5c2411-output-e988165.txt'),
('3', 4, 'Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.\r\n\r\nSo, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.\r\n\r\nHe gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is \"101\", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.\r\n\r\nHelp Subham to solve this problem.\r\n\r\n\r\nINPUT:\r\nThe first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.\r\n\r\nOUTPUT:\r\nPrint the answer for every test case in a new line.', 'Subham and Binary Strings', 1, '3e6748eef8-sample-input-3e6699c.txt', '42a6303cf8-sample-output-42a5bb0.txt'),
('3', 4, 'Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.\r\n\r\nSo, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.\r\n\r\nHe gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is \"101\", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.\r\n\r\nHelp Subham to solve this problem.\r\n\r\n\r\nINPUT:\r\nThe first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.\r\n\r\nOUTPUT:\r\nPrint the answer for every test case in a new line.', 'Subham and Binary Strings', 2, 'c674ff08f8-in09.txt', 'c69115bcf8-out09.txt');

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

--
-- Dumping data for table `ranks`
--

INSERT INTO `ranks` (`Email`, `Competionid`, `Rank`) VALUES
('bubs@bubs.com', '3', 3),
('dylaniansld@gmail.com', '3', 1),
('qwerty@qwerty.com', '3', 2);

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
  `Submettime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Language` varchar(100) NOT NULL DEFAULT 'Python'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `results`
--

INSERT INTO `results` (`competitionsid`, `Email`, `problemid`, `submission`, `Solved`, `Submettime`, `Language`) VALUES
('3', 'bubs@bubs.com', 1, 'def noofbits(n):\r\n    sum =0\r\n    while(n):\r\n        n = n & (n-1)\r\n        sum = sum+1\r\n    return sum\r\ntry:\r\n    while 1:\r\n        num = input()\r\n        print(noofbits(int(num)))\r\nexcept EOFError:\r\n    pass', 0, '2018-08-10 04:29:59', 'Python'),
('3', 'bubs@bubs.com', 2, 'def noofbits(n):\r\n    sum =0\r\n    while(n):\r\n        n = n & (n-1)\r\n        sum = sum+1\r\n    return sum\r\ntry:\r\n    while 1:\r\n        num = input()\r\n        print(noofbits(int(num)))\r\nexcept EOFError:\r\n    pass        ', 0, '2018-08-10 04:30:16', 'Python'),
('3', 'bubs@bubs.com', 3, 'def noofbits(n):\r\n    sum =0\r\n    while(n):\r\n        n = n & (n-1)\r\n        sum = sum+1\r\n    return sum\r\ntry:\r\n    while 1:\r\n        num = input()\r\n        print(noofbits(int(num)))\r\nexcept EOFError:\r\n    pass                    ', 0, '2018-08-10 04:30:38', 'Python'),
('3', 'dylaniansld@gmail.com', 1, 'import math\r\nfor i in range(5):\r\n    if i == 2:\r\n        print(i)\r\n    print(i)\r\n', 0, '2018-11-29 10:15:23', 'Python'),
('3', 'dylaniansld@gmail.com', 3, 'from sys import stdout,stdin\r\nt=int(stdin.readline())\r\nfor i in range(t):\r\n    n=int(stdin.readline())\r\n    binary=bin(n)[2:]\r\n    if \'0\' in binary:\r\n        for j in range(len(binary)-1,0,-1):\r\n            if binary[j]==\'0\':\r\n                pos=j\r\n                break\r\n        ans=int(binary[:pos]+\"1\"+binary[pos+1:],2)\r\n    else:\r\n        ans=int(\"1\"+binary,2)\r\n    stdout.write(str(ans)+\"\\n\")', 1, '2018-08-12 10:37:21', 'Python'),
('3', 'dylaniansld@gmail.com', 4, 'def ans():\r\n    for _ in range(int(input())):\r\n        input()\r\n        yield input().count(\"0\")\r\nprint(*ans(), sep=\"\\n\")', 1, '2018-08-12 10:38:05', 'Python'),
('3', 'qwerty@qwerty.com', 1, 'def noofbits(n):\r\n    sum =0\r\n    while(n):\r\n        n = n & (n-1)\r\n        sum = sum+1\r\n    return sum\r\ntry:\r\n    while 1:\r\n        num = input()\r\n        print(noofbits(int(num)))\r\nexcept EOFError:\r\n    pass\r\n ', 0, '2018-08-10 09:09:35', 'Python'),
('3', 'qwerty@qwerty.com', 2, '\r\n\r\n\r\n\r\n    \r\n\r\n    \r\n\r\ndef noofbits(n):\r\n    sum =0\r\n    while(n):\r\n        n = n & (n-1)\r\n        sum = sum+1\r\n    return sum\r\ntry:\r\n    while 1:\r\n        num = input()\r\n        print(noofbits(int(num)))\r\nexcept EOFError:\r\n    pass\r\n    \r\n\r\n\r\n\r\n    \r\n\r\n\r\n                            \r\n    \r\n\r\n\r\n                            ', 0, '2018-08-10 06:59:37', 'Python'),
('3', 'qwerty@qwerty.com', 3, '\r\n\r\n\r\n\r\n\r\nfrom sys import stdout,stdin\r\nt=int(stdin.readline())\r\nfor i in range(t):\r\n    n=int(stdin.readline())\r\n    binary=bin(n)[2:]\r\n    if \'0\' in binary:\r\n        for j in range(len(binary)-1,0,-1):\r\n            if binary[j]==\'0\':\r\n                pos=j\r\n                break\r\n        ans=int(binary[:pos]+\"1\"+binary[pos+1:],2)\r\n    else:\r\n        ans=int(\"1\"+binary,2)\r\n    stdout.write(str(ans)+\"\\n\")\r\n    \r\n\r\n\r\n                            \r\n    \r\n\r\n\r\n                            \r\n    \r\n\r\n\r\n                            \r\n    \r\n\r\n\r\n                            \r\n    \r\n\r\n\r\n                            ', 1, '2018-08-10 09:59:05', 'Python');

-- --------------------------------------------------------

--
-- Table structure for table `resulttrack`
--

DROP TABLE IF EXISTS `resulttrack`;
CREATE TABLE `resulttrack` (
  `CompId` varchar(100) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `Problem 1` int(11) NOT NULL,
  `Problem 2` int(11) NOT NULL,
  `Problem 3` int(11) NOT NULL,
  `Problem 4` int(11) NOT NULL,
  `Time1` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Time2` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Time3` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Time4` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Total marks` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `resulttrack`
--

INSERT INTO `resulttrack` (`CompId`, `Email`, `Problem 1`, `Problem 2`, `Problem 3`, `Problem 4`, `Time1`, `Time2`, `Time3`, `Time4`, `Total marks`) VALUES
('3', 'bubs@bubs.com', 0, 0, 0, 0, '2018-08-09 22:59:59', '2018-08-09 23:00:16', '2018-08-09 23:00:38', '0000-00-00 00:00:00', 0),
('3', 'dylaniansld@gmail.com', 0, 0, 90, 100, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '2018-08-12 05:07:21', '2018-08-12 05:08:05', 190),
('3', 'qwerty@qwerty.com', 0, 0, 90, 0, '2018-08-10 03:39:35', '2018-08-10 01:29:37', '2018-08-10 04:29:05', '0000-00-00 00:00:00', 90),
('3', 'bubs@bubs.com', 0, 0, 0, 0, '2018-08-10 04:29:59', '2018-08-10 04:30:16', '2018-08-10 04:30:38', '0000-00-00 00:00:00', 0),
('3', 'dylaniansld@gmail.com', 0, 0, 90, 100, '2018-11-29 10:15:23', '0000-00-00 00:00:00', '2018-08-12 10:37:21', '2018-08-12 10:38:05', 190),
('3', 'qwerty@qwerty.com', 0, 0, 90, 0, '2018-08-10 09:09:35', '2018-08-10 06:59:37', '2018-08-10 09:59:05', '0000-00-00 00:00:00', 90);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `Email` varchar(60) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(60) NOT NULL,
  `joindate` datetime DEFAULT CURRENT_TIMESTAMP,
  `actives` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 for false 1 for true'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Email`, `Username`, `Password`, `joindate`, `actives`) VALUES
('abhi', 'fwfefq', 'fvrwbvrwrw', '2018-08-09 02:12:02', 0),
('admin@gmail.com', 'apple', '$2b$12$jF0Wqvs0eS0bAxeNFHSpquh8vo/Zh87rJo/4eOzZPzieoBJEzVY7W', '2018-08-09 04:30:25', 0),
('blueadmin@gmail.com', 'blueapple', '$2b$12$tScfwJYVNlEz4m0qwuJUsujLnr2.pgyVVc7BKtH.9fIIf39W7bN9S', '2018-08-09 04:34:04', 0),
('bubs@bubs.com', 'bubs', '$2b$12$l81YdYJdHGaPuZ0Z.7pgUOBk3tXD/ykPoZn/Rk.8Xo2LNAQSU3N2O', '2018-08-10 09:58:42', 0),
('dylaniansld@gmail.com', 'DylanSaldanha', '$2b$12$ZfIX33cl8BwNVHVhfi14aewidA38f75sFCV.s9Dp7pTHAjHzdvLme', '2018-08-12 15:52:56', 1),
('dylansaldanha@hotmail.com', 'Dylan', '$2b$12$jr5hurcwGdpjNhnfMA7FL.bKTm1LqP8DZ972gzOLEH6m8Ak1QBHoq', '2018-08-09 10:23:43', 0),
('greenadmin@gmail.com', 'greenapple', '$2b$12$f5aQdXw85Gr9.5r2WYEYM..HDM7SM4OEgJETO3xf.IcsC1/xz0jQK', '2018-08-09 04:32:49', 0),
('qweradmin@gmail.com', 'qwerapple', '$2b$12$olllkO802fvqjYCXXoKETuNykFkB5uaGJcCa48ltm7kvECNL3TWjm', '2018-08-09 04:36:35', 0),
('qwerty@qwerty.com', 'qwerty', '$2b$12$2EVWeXAWKdPRhoQ0GvZgLeWE0PeEtq79jf01rxEynbA0HBIZiYSCO', '2018-08-09 13:23:59', 0);

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
