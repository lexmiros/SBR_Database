-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2022 at 09:29 AM
-- Server version: 8.0.28
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_db_3`
--

-- --------------------------------------------------------

--
-- Table structure for table `buggies`
--

CREATE TABLE `buggies` (
  `VehicleID` int NOT NULL,
  `NumberOfSeats` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `buggies`
--

INSERT INTO `buggies` (`VehicleID`, `NumberOfSeats`) VALUES
(11, 2),
(12, 4),
(13, 4),
(14, 4);

-- --------------------------------------------------------

--
-- Table structure for table `cattle`
--

CREATE TABLE `cattle` (
  `CattleID` int NOT NULL,
  `Sex` enum('Male','Female') DEFAULT NULL,
  `Breed` enum('Belmont Red','Angus','Cross') DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Weight` double DEFAULT NULL,
  `PaddockName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DateMoved` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cattle`
--

INSERT INTO `cattle` (`CattleID`, `Sex`, `Breed`, `DateOfBirth`, `Weight`, `PaddockName`, `DateMoved`) VALUES
(3, 'Male', 'Angus', '2020-11-21', 1100, 'Paddock1', '2020-11-21'),
(21, 'Male', 'Belmont Red', '2020-12-12', 870, 'Paddock1', '2020-12-12'),
(22, 'Male', 'Belmont Red', '2020-12-12', 870, 'Paddock1', '2020-12-12'),
(23, 'Female', 'Belmont Red', '2020-12-12', 920, 'Paddock1', '2020-12-12'),
(24, 'Male', 'Belmont Red', '2020-12-12', 840, 'Paddock1', '2020-12-12'),
(25, 'Female', 'Belmont Red', '2020-12-12', 1000, 'Paddock1', '2020-12-12'),
(26, 'Male', 'Belmont Red', '2020-12-12', 999, 'Paddock1', '2020-12-12'),
(27, 'Male', 'Belmont Red', '2020-12-12', 870, 'Paddock1', '2020-12-12'),
(28, 'Female', 'Belmont Red', '2020-12-12', 920, 'Paddock1', '2020-12-12'),
(29, 'Male', 'Belmont Red', '2020-12-12', 840, 'Paddock1', '2020-12-12'),
(30, 'Female', 'Belmont Red', '2020-12-12', 1000, 'Paddock1', '2020-12-12'),
(31, 'Male', 'Belmont Red', '2020-12-12', 999, 'Paddock1', '2020-12-12'),
(32, 'Male', 'Angus', '2020-12-12', 500, 'Paddock2', '2020-12-12'),
(33, 'Female', 'Angus', '2020-12-12', 700, 'Paddock2', '2020-12-12'),
(34, 'Male', 'Angus', '2020-12-12', 560, 'Paddock2', '2020-12-12'),
(35, 'Female', 'Angus', '2020-12-12', 600, 'Paddock2', '2020-12-12'),
(36, 'Male', 'Angus', '2020-12-12', 670, 'Paddock2', '2020-12-12'),
(37, 'Male', 'Cross', '2020-12-12', 870, 'Paddock3', '2020-12-12'),
(38, 'Female', 'Cross', '2020-12-12', 800, 'Paddock3', '2020-12-12'),
(39, 'Male', 'Cross', '2020-12-12', 840, 'Paddock3', '2020-12-12'),
(40, 'Female', 'Cross', '2020-12-12', 1000, 'Paddock3', '2020-12-12'),
(41, 'Male', 'Cross', '2020-12-12', 999, 'Paddock3', '2020-12-12');

-- --------------------------------------------------------

--
-- Table structure for table `farm`
--

CREATE TABLE `farm` (
  `FarmName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `farm`
--

INSERT INTO `farm` (`FarmName`, `Address`) VALUES
('Farm1', 'Address 1, QLD, 4111'),
('Farm2', 'Address 2, QLD, 4120'),
('Farm3', 'Address 3, QLD, 4001'),
('Farm4', 'Address 4, QLD, 4120'),
('Farm5', 'Address 5');

-- --------------------------------------------------------

--
-- Table structure for table `feed_bins`
--

CREATE TABLE `feed_bins` (
  `BinNumber` int NOT NULL,
  `PaddockName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LastChecked` date DEFAULT NULL,
  `BinContains` enum('Wheat','Salt Lick','Sorghum') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `BinLevel` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `feed_bins`
--

INSERT INTO `feed_bins` (`BinNumber`, `PaddockName`, `LastChecked`, `BinContains`, `BinLevel`) VALUES
(1, 'New Paddock', '2022-05-03', 'Salt Lick', 0),
(1, 'Paddock1', '2022-04-11', 'Wheat', 0.76),
(1, 'Paddock2', '2022-03-01', 'Sorghum', 1),
(2, 'Paddock1', '2022-04-10', 'Salt Lick', 0.75),
(2, 'Paddock2', '2022-04-10', 'Wheat', 0),
(3, 'Paddock1', '2022-04-10', 'Wheat', 1);

-- --------------------------------------------------------

--
-- Table structure for table `motorbikes`
--

CREATE TABLE `motorbikes` (
  `VehicleID` int NOT NULL,
  `EngineCC` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `motorbikes`
--

INSERT INTO `motorbikes` (`VehicleID`, `EngineCC`) VALUES
(1, 200),
(2, 300),
(3, 300),
(4, 200),
(5, 275);

-- --------------------------------------------------------

--
-- Table structure for table `paddock`
--

CREATE TABLE `paddock` (
  `PaddockName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Size` double DEFAULT NULL,
  `GrassCondition` enum('Dry','Green') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `FarmName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `paddock`
--

INSERT INTO `paddock` (`PaddockName`, `Size`, `GrassCondition`, `FarmName`) VALUES
('New Paddock', 1000, 'Dry', 'Farm1'),
('Paddock1', 500, 'Green', 'Farm1'),
('Paddock2', 250, 'Green', 'Farm2'),
('Paddock3', 900, 'Dry', 'Farm3');

-- --------------------------------------------------------

--
-- Table structure for table `quadbikes`
--

CREATE TABLE `quadbikes` (
  `VehicleID` int NOT NULL,
  `RollCage` enum('Yes','No') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quadbikes`
--

INSERT INTO `quadbikes` (`VehicleID`, `RollCage`) VALUES
(6, 'Yes'),
(7, 'No'),
(8, 'Yes'),
(9, 'Yes'),
(10, 'No');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `StaffID` int NOT NULL,
  `FirstName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `LastName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `FarmName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `ManagerID` int DEFAULT NULL,
  `PrimaryContactNumber` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`StaffID`, `FirstName`, `LastName`, `DateOfBirth`, `FarmName`, `StartDate`, `ManagerID`, `PrimaryContactNumber`) VALUES
(2, 'Jane', 'Smith', '1999-05-09', 'Farm1', '2020-01-19', 3, '346346241'),
(3, 'Shelly', 'Ward', '1993-11-21', 'Farm2', '2022-04-12', 2, '235242'),
(4, 'Leo', 'Harding', '1996-03-28', 'Farm2', '2021-01-01', 3, '23412351'),
(5, 'Paul', 'Saint', '1979-05-13', 'Farm2', '2006-02-02', 3, '412415324');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `VehicleID` int NOT NULL,
  `Model` varchar(255) DEFAULT NULL,
  `FarmName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `PurchaseDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`VehicleID`, `Model`, `FarmName`, `PurchaseDate`) VALUES
(1, 'Motorbike_M_1', 'Farm1', '2018-01-01'),
(2, 'Motorbike_M_2', 'Farm1', '2019-03-11'),
(3, 'Motorbike_M_3', 'Farm2', '2020-06-21'),
(4, 'Motorbike_M_4', 'Farm2', '2021-07-10'),
(5, 'Motorbike_M_5', 'Farm2', '2022-01-01'),
(6, 'Quadbike_M_1', 'Farm2', '2018-01-01'),
(7, 'Quadbike_M_2', 'Farm2', '2019-03-11'),
(8, 'Quadbike_M_3', 'Farm2', '2020-06-21'),
(9, 'Quadbike_M_4', 'Farm1', '2021-07-10'),
(10, 'Quadbike_M_5', 'Farm1', '2022-01-01'),
(11, 'Buggie_M_1', 'Farm1', '2018-01-01'),
(12, 'Buggie_M_2', 'Farm2', '2019-03-11'),
(13, 'Buggie_M_3', 'Farm1', '2020-06-21'),
(14, 'Buggie_M_4', 'Farm2', '2021-07-10');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_brands`
--

CREATE TABLE `vehicle_brands` (
  `VehicleID` int NOT NULL,
  `Brand` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `vehicle_brands`
--

INSERT INTO `vehicle_brands` (`VehicleID`, `Brand`) VALUES
(1, 'Mitsubishi'),
(2, 'Kawasaki'),
(3, 'Honda'),
(4, 'Honda'),
(5, 'Holden'),
(6, 'TGB'),
(7, 'Kawaski'),
(8, 'Kawaski'),
(9, 'Hyundi'),
(10, 'Toyota'),
(11, 'Toyota'),
(12, 'TGB'),
(13, 'Holden'),
(14, 'Mitsubishi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buggies`
--
ALTER TABLE `buggies`
  ADD PRIMARY KEY (`VehicleID`);

--
-- Indexes for table `cattle`
--
ALTER TABLE `cattle`
  ADD PRIMARY KEY (`CattleID`),
  ADD KEY `Paddock_name` (`PaddockName`);

--
-- Indexes for table `farm`
--
ALTER TABLE `farm`
  ADD PRIMARY KEY (`FarmName`);

--
-- Indexes for table `feed_bins`
--
ALTER TABLE `feed_bins`
  ADD PRIMARY KEY (`BinNumber`,`PaddockName`),
  ADD KEY `Paddock_name` (`PaddockName`);

--
-- Indexes for table `motorbikes`
--
ALTER TABLE `motorbikes`
  ADD PRIMARY KEY (`VehicleID`);

--
-- Indexes for table `paddock`
--
ALTER TABLE `paddock`
  ADD PRIMARY KEY (`PaddockName`),
  ADD KEY `Farm_name` (`FarmName`);

--
-- Indexes for table `quadbikes`
--
ALTER TABLE `quadbikes`
  ADD PRIMARY KEY (`VehicleID`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`StaffID`),
  ADD KEY `Farm_name` (`FarmName`),
  ADD KEY `Manager_ID` (`ManagerID`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`VehicleID`),
  ADD KEY `Farm_name` (`FarmName`);

--
-- Indexes for table `vehicle_brands`
--
ALTER TABLE `vehicle_brands`
  ADD PRIMARY KEY (`VehicleID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cattle`
--
ALTER TABLE `cattle`
  MODIFY `CattleID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `StaffID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `VehicleID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buggies`
--
ALTER TABLE `buggies`
  ADD CONSTRAINT `BUGGIES_ibfk_1` FOREIGN KEY (`VehicleID`) REFERENCES `vehicles` (`VehicleID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cattle`
--
ALTER TABLE `cattle`
  ADD CONSTRAINT `CATTLE_ibfk_1` FOREIGN KEY (`PaddockName`) REFERENCES `paddock` (`PaddockName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `feed_bins`
--
ALTER TABLE `feed_bins`
  ADD CONSTRAINT `FEED_BINS_ibfk_1` FOREIGN KEY (`PaddockName`) REFERENCES `paddock` (`PaddockName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `motorbikes`
--
ALTER TABLE `motorbikes`
  ADD CONSTRAINT `MOTORBIKES_ibfk_1` FOREIGN KEY (`VehicleID`) REFERENCES `vehicles` (`VehicleID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `paddock`
--
ALTER TABLE `paddock`
  ADD CONSTRAINT `PADDOCK_ibfk_1` FOREIGN KEY (`FarmName`) REFERENCES `farm` (`FarmName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `quadbikes`
--
ALTER TABLE `quadbikes`
  ADD CONSTRAINT `QUADBIKES_ibfk_1` FOREIGN KEY (`VehicleID`) REFERENCES `vehicles` (`VehicleID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `STAFF_ibfk_1` FOREIGN KEY (`FarmName`) REFERENCES `farm` (`FarmName`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `STAFF_ibfk_2` FOREIGN KEY (`ManagerID`) REFERENCES `staff` (`StaffID`) ON UPDATE CASCADE;

--
-- Constraints for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD CONSTRAINT `VEHICLES_ibfk_1` FOREIGN KEY (`FarmName`) REFERENCES `farm` (`FarmName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vehicle_brands`
--
ALTER TABLE `vehicle_brands`
  ADD CONSTRAINT `VEHICLE_BRANDS_ibfk_1` FOREIGN KEY (`VehicleID`) REFERENCES `vehicles` (`VehicleID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
