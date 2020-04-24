-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2020 at 10:47 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scientificatt`
--

-- --------------------------------------------------------

--
-- Table structure for table `branches`
--

CREATE TABLE `branches` (
  `Sno` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Head` text NOT NULL,
  `Address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branches`
--

INSERT INTO `branches` (`Sno`, `Name`, `Head`, `Address`) VALUES
(2, 'Delhi', 'Samyak Jain', 'new delhi'),
(3, 'Mumbai', 'ABCD', 'andheri');

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `image` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`sno`, `name`, `image`) VALUES
(3, 'Marketing', 'Company_logo.png'),
(4, 'test', ' '),
(5, 'test 2', ' ');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Phone` varchar(12) NOT NULL,
  `Password` text NOT NULL,
  `Branch` text DEFAULT NULL,
  `Department` text NOT NULL,
  `Designation` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `Name`, `Email`, `Phone`, `Password`, `Branch`, `Department`, `Designation`) VALUES
(4, 'ISHAAN KAMRA', 'ishaan1091@gmail.com', '9876543210', 'sha256$JFAsZDCW$cb81d8365a8bb4e85aa31a53f4bc6c262c83c858a56f31635005bdb63433ebf8', 'Delhi', 'NOT ASSIGNED', 'Founder'),
(10, 'Samyak Jain', 'sjsamyak2001@gmail.com', '8810433039', 'sha256$oTYEI8fM$e7afd5524809a99eab35431cf19401152acc6bc9e3f6bdc46a79dee77bb6caa4', 'Delhi', 'marketing', 'Founder'),
(14, 'ABCD', 'ishaanrng@gmail.com', '9876543210', 'sha256$uhbmmZv8$5caec40c04f83fdba3b34eb430c37c32a2677fedd25c48fa323893ad5c6af965', 'Mumbai', 'NOT ASSIGNED', 'Branch Head'),
(18, 'tushar', 'tushar@gmail.com', '9876544321', 'sha256$08v1BAGp$20dc823cefd0cbe8b675ce27f8fd2cbacdc87581129711a19e3abfc537698b52', 'Delhi', '', 'Employee'),
(19, 'ABCD', 'ABCD@gmail.com', '9876544321', 'sha256$sof4SkEb$c8300e5ff4eb737da0aaee7294a9263a9a69601291a988dcc3524af0714a9ea2', 'Delhi', 'Marketing', 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `new`
--

CREATE TABLE `new` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `phone_no` int(100) NOT NULL,
  `branch` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `department` text NOT NULL,
  `employee` varchar(100) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `date` date DEFAULT current_timestamp(),
  `status` text NOT NULL,
  `description` text NOT NULL,
  `report` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`sno`, `name`, `department`, `employee`, `branch`, `date`, `status`, `description`, `report`) VALUES
(3, 'test30 ', 'Marketing', '[\"ishaan1091@gmail.com\"]', 'Mumbai', '0000-00-00', 'ACTIVE', 'T E S T        T E S T             T E S T', '[\"Completed project\"]'),
(4, 'test4', 'NOT ASSIGNED', '[\"ABCD@gmail.com\"]', 'NOT ASSIGNED', '0000-00-00', 'COMPLETED', 'test4 test4 test4 test4 test4', '[]'),
(5, 'test5', 'Marketing', '[\"ishaan1091@gmail.com\"]', 'Delhi', '2020-04-21', 'ACTIVE', 'tttttttttt', '[]'),
(6, 'test3', 'Marketing', '[\"ishaanrng@gmail.com\"]', 'Delhi', '2020-04-23', 'ACTIVE', 'tttttttttteeeeeeeeesssssssssttttttttt', '[]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `branches`
--
ALTER TABLE `branches`
  ADD PRIMARY KEY (`Sno`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `new`
--
ALTER TABLE `new`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `branches`
--
ALTER TABLE `branches`
  MODIFY `Sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `new`
--
ALTER TABLE `new`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
