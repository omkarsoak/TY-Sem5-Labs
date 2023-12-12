CREATE DATABASE STORE_MANAGEMENT;
USE STORE_MANAGEMENT;

DROP DATABASE store_management1;
CREATE DATABASE STORE_MANAGEMENT2;
USE STORE_MANAGEMENT2;

SET time_zone = "+00:00";


CREATE TABLE `bill` (
  `B_ID` int(11) NOT NULL,
  `BANK` varchar(20) DEFAULT NULL,
  `DATE_OF_BILL` date DEFAULT NULL,
  `TRANSACTION_ID` varchar(20) DEFAULT NULL,
  `AMOUNT` float NOT NULL,
  `C_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- --------------------------------------------------------

--
-- Table structure for table `contains`
--

CREATE TABLE `contains` (
  `STORE_ID` int(11) NOT NULL,
  `ITEM_ID` int(11) NOT NULL,
  `Quantity` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `C_ID` int(11) NOT NULL,
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Qualification` varchar(20) DEFAULT NULL,
  `ADDRESS` varchar(50) DEFAULT NULL,
  `Locality` varchar(20) DEFAULT NULL,
  `CITY` varchar(20) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone_NO` varchar(10) DEFAULT NULL,
  `DOP` date NOT NULL,
  `E_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `E_ID` int(11) NOT NULL,
  `First_Name` varchar(30) DEFAULT NULL,
  `Last_Name` varchar(30) NOT NULL,
  `MGR_ID` int(11) DEFAULT NULL,
  `GENDER` varchar(1) NOT NULL,
  `SALARY` float NOT NULL,
  `DOB` date NOT NULL,
  `Phone_no` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `ITEM_ID` int(11) NOT NULL,
  `Item_Name` varchar(30) DEFAULT NULL,
  `PRICE` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`ITEM_ID`, `Item_Name`, `PRICE`) VALUES
(4000, 'Shirt', 900),
(4001, 'Shirt', 1499),
(4002, 'Shirt', 999),
(4010, 'Pant', 2999),
(4011, 'Pant', 4000),
(4030, 'Coat', 15000),
(4041, 'Gown', 7999),
(4042, 'Gown', 4999),
(4050, 'Cap/Hat', 499),
(4060, 'Sweater', 999),
(4061, 'Sweater', 1799),
(4070, 'Jacket', 900),
(4071, 'Jacket', 600),
(4080, 'Legging', 400),
(4081, 'Legging', 349),
(4082, 'Legging', 499),
(4083, 'Legging', 550),
(4090, 'Jeggings', 700),
(4091, 'Jeggings', 599),
(4092, 'Jeggings', 445),
(4100, 'Tops', 250),
(4101, 'Tops', 399),
(4102, 'Tops', 549),
(4110, 'Saree', 1749),
(4111, 'Saree', 2499),
(4112, 'Saree', 3999),
(4120, 'Chudidhar', 799),
(4121, 'Chudidhar', 999),
(4122, 'Chudidhar', 1599),
(4130, 'Frock', 1199),
(4131, 'Frock', 1499),
(4140, 'Lehenga', 3000),
(4150, 'Dhoti', 400),
(4151, 'Dhoti', 500),
(4160, 'Tshirt', 799),
(4161, 'Tshirt', 699),
(4162, 'Tshirt', 1000),
(4163, 'Tshirt', 900),
(4170, 'Shorts', 500),
(4171, 'Shorts', 599),
(4180, 'Skirt', 699),
(4181, 'Skirt', 700),
(4190, 'Pyjama', 650),
(4200, 'Kurta', 999),
(4201, 'Kurta', 799),
(4300, 'Palazzo', 749),
(4400, 'Cigar Pant', 1999);


--
-- Table structure for table `item_category`
--

CREATE TABLE `item_category` (
  `ITEM_ID` int(11) NOT NULL,
  `Item_Name` varchar(30) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `BRAND` varchar(20) DEFAULT 'SMS Textiles',
  `COLOUR` varchar(20) DEFAULT NULL,
  `SIZE` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `item_category`
--

INSERT INTO `item_category` (`ITEM_ID`, `Item_Name`, `Gender`, `BRAND`, `COLOUR`, `SIZE`) VALUES
(4000, 'Shirt', 'M', 'Ramraj', 'Red', '38'),
(4001, 'Shirt', 'M', 'Allen Solly', 'Blue', '40'),
(4002, 'Shirt', 'M', 'Peterson', 'Green', '42'),
(4010, 'Pant', 'M', 'Buffallo', 'Black', '38'),
(4011, 'Pant', 'M', 'Polo', 'Brown', '40'),
(4030, 'Coat', 'F', 'Raymond', 'Grey', 'XXL'),
(4041, 'Gown', 'F', 'Chennai Silks', 'Pink', 'XXL'),
(4042, 'Gown', 'M', 'ARRS Silks', 'Green', 'XL'),
(4050, 'Cap/Hat', 'M', 'MAX', 'Cyan', ''),
(4060, 'Sweater', 'F', 'Deccathlon', 'Navyblue', 'XL'),
(4061, 'Sweater', 'M', 'Deccathlon', 'Light_Brown', 'L'),
(4070, 'Jacket', 'M', 'Kumaran Tex', 'Red', 'L'),
(4071, 'Jacket', 'M', 'Vittal Dresses', 'Brown', 'XXL'),
(4080, 'Legging', 'F', 'Chennai Silks', 'Maroon', 'XL'),
(4081, 'Legging', 'F', 'ARRS Silks', 'White', 'M'),
(4082, 'Legging', 'F', 'Kumaran Tex', 'Black', 'XXL'),
(4083, 'Legging', 'F', 'Pothys', 'Dark_Blue', 'XXXL'),
(4090, 'Jeggings', 'F', 'Chennai Silks', 'Purple', 'XXL'),
(4091, 'Jeggings', 'F', 'ARRS Silks', 'Grey', 'XL'),
(4092, 'Jeggings', 'F', 'Kumaran Tex', 'Yellow', 'L'),
(4100, 'Tops', 'F', 'Pothys', 'Black', 'XL'),
(4101, 'Tops', 'F', 'Trends', 'Red', 'XL'),
(4102, 'Tops', 'F', 'Trends', 'Blue', 'XXL'),
(4110, 'Saree', 'F', 'Chennai Silks', 'Pink', ''),
(4111, 'Saree', 'F', 'Kanchipuram Textiles', 'Purple', ''),
(4112, 'Saree', 'F', 'Kanchipuram Textiles', 'Blue', ''),
(4120, 'Chudidhar', 'F', 'Chennai Silks', 'Yellow', 'L'),
(4121, 'Chudidhar', 'F', 'ARRS Silks', 'Orange', 'XL'),
(4122, 'Chudidhar', 'F', 'Pothys', 'Green', 'XXL'),
(4130, 'Frock', 'F', 'Ramraj', 'Rainbow', '38'),
(4131, 'Frock', 'F', 'MAX', 'Violet', '42'),
(4140, 'Lehenga', 'F', 'Raymond', 'Baby_Pink', 'XL'),
(4150, 'Dhoti', 'M', 'Ramraj', 'White', '40'),
(4151, 'Dhoti', 'M', 'Pothys', 'Light_Brown', '50'),
(4160, 'Tshirt', 'M', 'Van Hussen', 'Red', '42'),
(4161, 'Tshirt', 'M', 'Van Hussen', 'Black', '44'),
(4162, 'Tshirt', 'M', 'MAX', 'Brown', '40'),
(4163, 'Tshirt', 'M', 'Polo', 'Grey', '38'),
(4170, 'Shorts', 'M', 'Polo', 'Green', '36'),
(4171, 'Shorts', 'M', 'Buffallo', 'Blue', '38'),
(4180, 'Skirt', 'F', 'Kanchipuram Tex', 'Light_Green', '42'),
(4181, 'Skirt', 'F', 'Kumaran Tex', 'Pink', '38'),
(4190, 'Pyjama', 'M', 'Chennai Silks', 'Grey', '40'),
(4200, 'Kurta', 'M', 'Raymond', 'White', '42'),
(4201, 'Kurta', 'M', 'Trends', 'Red', '36'),
(4300, 'Palazzo', 'F', 'Prisma', 'Cyan', 'XXL'),
(4400, 'Cigar Pant', 'F', 'Twinbirds', 'Maroon', 'XL');


--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `C_ID` int(11) NOT NULL,
  `ITEM_ID` int(11) NOT NULL,
  `Price` float DEFAULT NULL,
  `QUANTITY` int(5) NOT NULL,
  `O_Date` date DEFAULT NULL,
  `O_Amount` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`C_ID`, `ITEM_ID`, `Price`, `QUANTITY`, `O_Date`, `O_Amount`) VALUES
(2001, 4002, 999, 3, '2022-12-09', 2997),
(2001, 4011, 4000, 4, '2022-12-09', 16000),
(2001, 4090, 700, 10, '2022-12-09', 7000),
(2002, 4002, 999, 2, '2022-10-16', 2000),
(2002, 4080, 400, 4, '2022-08-16', 1600),
(2002, 4102, 549, 5, '2022-10-16', 2750),
(2002, 4121, 999, 2, '2022-10-16', 1998),
(2003, 4000, 900, 10, '2022-10-25', 8000),
(2003, 4090, 700, 7, '2022-10-25', 4900),
(2003, 4151, 500, 5, '2022-10-25', 2500),
(2003, 4171, 599, 9, '2022-10-25', 5400),
(2004, 4082, 499, 12, '2022-08-22', 6000),
(2004, 4170, 500, 7, '2022-08-22', 3500),
(2005, 4002, 999, 1, '2022-09-10', 1000),
(2005, 4081, 349, 5, '2022-09-10', 1750),
(2005, 4082, 499, 3, '2022-09-10', 1500),
(2006, 4120, 799, 7, '2022-07-10', 5600),
(2006, 4140, 3000, 3, '2022-07-10', 9000),
(2006, 4201, 799, 8, '2022-01-08', 7992),
(2007, 4042, 4999, 1, '2022-08-21', 5000),
(2007, 4122, 1599, 3, '2022-08-21', 4797),
(2007, 4140, 3000, 7, '2022-08-21', 21000),
(2008, 4002, 999, 3, '2022-07-19', 3000),
(2008, 4010, 2999, 6, '2022-07-19', 18000),
(2008, 4061, 1799, 4, '2022-07-19', 7200),
(2009, 4083, 550, 6, '2022-08-31', 3300),
(2009, 4200, 999, 4, '2022-08-31', 3200),
(2010, 4071, 600, 4, '2022-02-08', 2400),
(2010, 4092, 445, 7, '2022-02-08', 3150),
(2011, 4122, 1599, 3, '2022-07-10', 4797),
(2011, 4130, 1199, 7, '2022-07-10', 8393),
(2012, 4060, 999, 1, '2022-10-17', 1000),
(2012, 4061, 1799, 3, '2022-10-17', 5400),
(2012, 4091, 599, 6, '2022-10-17', 3600),
(2012, 4121, 999, 5, '2022-10-17', 4995),
(2013, 4070, 900, 1, '2022-09-18', 900),
(2013, 4102, 549, 3, '2022-09-18', 1650),
(2014, 4160, 799, 8, '2022-08-29', 6400),
(2015, 4002, 999, 5, '2022-10-30', 5000),
(2015, 4011, 4000, 2, '2022-10-30', 8000),
(2015, 4111, 2499, 3, '2022-10-30', 7500),
(2016, 4030, 15000, 1, '2022-07-08', 15000),
(2016, 4061, 1799, 3, '2022-07-08', 3600),
(2016, 4180, 699, 5, '2022-07-08', 3500),
(2016, 4200, 999, 9, '2022-07-08', 7200),
(2017, 4030, 15000, 2, '2022-09-23', 30000),
(2017, 4100, 250, 9, '2022-09-23', 2250),
(2018, 4131, 1499, 4, '2022-10-27', 5996),
(2018, 4160, 799, 5, '2022-10-27', 4000),
(2018, 4190, 650, 11, '2022-10-27', 4400),
(2019, 4041, 7999, 2, '2022-09-26', 16000),
(2019, 4050, 499, 3, '2022-09-26', 1500),
(2019, 4090, 700, 3, '2022-09-26', 2100),
(2020, 4100, 250, 15, '2022-08-14', 3750),
(2020, 4110, 1749, 9, '2022-08-14', 15750),
(2020, 4163, 900, 6, '2022-08-14', 5400),
(2021, 4030, 15000, 1, '2022-11-23', 15000),
(2021, 4061, 1799, 1, '2022-11-23', 1799),
(2021, 4161, 699, 2, '2022-11-23', 1398),
(2022, 4080, 400, 4, '2022-11-19', 1600),
(2022, 4121, 999, 3, '2022-11-20', 2997),
(2022, 4140, 3000, 2, '2022-11-19', 6000);


--
-- Table structure for table `shipment`
--

CREATE TABLE `shipment` (
  `SHIP_ID` int(11) NOT NULL,
  `DATE_OF_SHIPMENT` date DEFAULT NULL,
  `STORE_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shipment`
--

INSERT INTO `shipment` (`SHIP_ID`, `DATE_OF_SHIPMENT`, `STORE_ID`) VALUES
(8001, '2022-05-22', 6001),
(8002, '2022-06-30', 6001),
(8003, '2022-09-05', 6001),
(8004, '2022-12-05', 6002),
(8005, '2022-04-21', 6004),
(8006, '2022-06-06', 6003),
(8007, '2022-06-25', 6004),
(8008, '2022-06-16', 6002),
(8009, '2022-05-31', 6003),
(8010, '2022-04-27', 6004);


--
-- Table structure for table `ships`
--

CREATE TABLE `ships` (
  `COST_OF_SHIPPING` float DEFAULT NULL,
  `MODE_OF_TRAVELLING` varchar(255) DEFAULT NULL,
  `SUPP_ID` int(11) NOT NULL,
  `SHIP_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ships`
--

INSERT INTO `ships` (`COST_OF_SHIPPING`, `MODE_OF_TRAVELLING`, `SUPP_ID`, `SHIP_ID`) VALUES
(5489, 'Roadways', 7001, 8005),
(4000, 'Airways', 7001, 8006),
(6597, 'Railways', 7002, 8001),
(870, 'Railways', 7002, 8009),
(5500, 'Railways', 7003, 8004),
(5500, 'Railways', 7003, 8008),
(7000, 'Airways', 7004, 8003),
(3500, 'Roadways', 7004, 8007),
(6290, 'Roadways', 7005, 8002),
(6290, 'Waterways', 7005, 8010);


--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `STORE_ID` int(11) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `ADDRESS` varchar(50) DEFAULT NULL,
  `MGR_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`STORE_ID`, `NAME`, `ADDRESS`, `MGR_ID`) VALUES
(6001, 'Bannerghatta', 'BG Road', 1002),
(6002, 'Jayanagar', 'Near Cool Joint', 1007),
(6003, 'Rajajinagar', 'Opposite to Rajarajeshwari Medical College', 1013),
(6004, 'Malleshwaram', 'Near Railway Station', 1010);


--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `SUPP_ID` int(11) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `ADDRESS` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`SUPP_ID`, `NAME`, `ADDRESS`) VALUES
(7001, 'Sukeerthan', 'Haritasa Apartments'),
(7002, 'Monisha', 'Mahaveer Marvel'),
(7003, 'Kavana', 'Tvs Emarold jordin'),
(7004, 'Roshan', 'Thayappa Garden'),
(7005, 'Satvik', 'Bhavani Apartments');

-- --------------------------------------------------------

ALTER TABLE `bill`
  ADD PRIMARY KEY (`B_ID`),
  ADD KEY `c_fid` (`C_ID`);

--
-- Indexes for table `contains`
--
ALTER TABLE `contains`
  ADD PRIMARY KEY (`STORE_ID`,`ITEM_ID`),
  ADD KEY `i_fid1` (`ITEM_ID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`C_ID`),
  ADD KEY `e_fid` (`E_ID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`E_ID`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`ITEM_ID`);

--
-- Indexes for table `item_category`
--
ALTER TABLE `item_category`
  ADD PRIMARY KEY (`ITEM_ID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`C_ID`,`ITEM_ID`),
  ADD KEY `item_fid2` (`ITEM_ID`);

--
-- Indexes for table `shipment`
--
ALTER TABLE `shipment`
  ADD PRIMARY KEY (`SHIP_ID`),
  ADD KEY `store_fid` (`STORE_ID`);

--
-- Indexes for table `ships`
--
ALTER TABLE `ships`
  ADD PRIMARY KEY (`SUPP_ID`,`SHIP_ID`),
  ADD KEY `ship_fid` (`SHIP_ID`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`STORE_ID`),
  ADD KEY `mgr_fid` (`MGR_ID`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`SUPP_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `c_fid` FOREIGN KEY (`C_ID`) REFERENCES `customers` (`C_ID`) ON DELETE CASCADE;

--
-- Constraints for table `contains`
--
ALTER TABLE `contains`
  ADD CONSTRAINT `i_fid1` FOREIGN KEY (`ITEM_ID`) REFERENCES `items` (`ITEM_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `store_fid1` FOREIGN KEY (`STORE_ID`) REFERENCES `store` (`STORE_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `e_fid` FOREIGN KEY (`E_ID`) REFERENCES `employee` (`E_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `item_category`
--
ALTER TABLE `item_category`
  ADD CONSTRAINT `item_fid` FOREIGN KEY (`ITEM_ID`) REFERENCES `items` (`ITEM_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `c_fid2` FOREIGN KEY (`C_ID`) REFERENCES `customers` (`C_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_fid2` FOREIGN KEY (`ITEM_ID`) REFERENCES `items` (`ITEM_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `shipment`
--
ALTER TABLE `shipment`
  ADD CONSTRAINT `shipment_fid` FOREIGN KEY (`SHIP_ID`) REFERENCES `ships` (`SHIP_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `store_fid` FOREIGN KEY (`STORE_ID`) REFERENCES `store` (`STORE_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ships`
--
ALTER TABLE `ships`
  ADD CONSTRAINT `supp_fid` FOREIGN KEY (`SUPP_ID`) REFERENCES `suppliers` (`SUPP_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `mgr_fid` FOREIGN KEY (`MGR_ID`) REFERENCES `employee` (`E_ID`) ON DELETE CASCADE ON UPDATE CASCADE;