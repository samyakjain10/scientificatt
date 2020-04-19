-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2020 at 08:30 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(4, 'ISHAAN KAMRA', 'ishaan1091@gmail.com', '9876543210', 'sha256$JFAsZDCW$cb81d8365a8bb4e85aa31a53f4bc6c262c83c858a56f31635005bdb63433ebf8', 'NOT ASSIGNED', 'NOT ASSIGNED', 'Founder'),
(10, 'Samyak Jain', 'sjsamyak2001@gmail.com', '8810433039', 'sha256$oTYEI8fM$e7afd5524809a99eab35431cf19401152acc6bc9e3f6bdc46a79dee77bb6caa4', 'mumbai', 'marketing', 'Employee'),
(14, 'ABCD', 'ishaanrng@gmail.com', '9876543210', 'sha256$uhbmmZv8$5caec40c04f83fdba3b34eb430c37c32a2677fedd25c48fa323893ad5c6af965', 'NOT ASSIGNED', 'NOT ASSIGNED', 'Branch Head'),
(15, 'ABCDEF', 'ABCD@gmail.com', '9876543210', 'sha256$NWVOlAf3$b097c130cdc9783ae59c404f45399702c89cbff71292cec972366aa055f1d25d', 'NOT ASSIGNED', 'NOT ASSIGNED', 'Employee');

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
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`sno`, `name`, `department`, `employee`, `branch`, `date`, `status`, `description`) VALUES
(1, 'test 1', 'NOT ASSIGNED', 'ABCD@gmail.com', 'NOT ASSIGNED', '0000-00-00', 'ACTIVE', 'test test test test'),
(2, 'test 2', 'NOT ASSIGNED', 'ABCD@gmail.com', 'NOT ASSIGNED', '0000-00-00', 'ACTIVE', 'test2 test2 test2 test2'),
(3, 'test3 ', 'NOT ASSIGNED', 'ishaanrng@gmail.com', 'NOT ASSIGNED', '0000-00-00', 'ACTIVE', 'T E S T        T E S T             T E S T'),
(4, 'test4', 'NOT ASSIGNED', 'ABCD@gmail.com', 'NOT ASSIGNED', '0000-00-00', 'COMPLETED', 'test4 test4 test4 test4 test4');

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
  MODIFY `Sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `new`
--
ALTER TABLE `new`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
