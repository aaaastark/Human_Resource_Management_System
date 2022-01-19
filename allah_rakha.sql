-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2022 at 06:19 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `allah_rakha`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_leave_1`
--

CREATE TABLE `emp_leave_1` (
  `id` int(11) NOT NULL,
  `leave_employee_id` varchar(10) NOT NULL,
  `leave_employee_name` varchar(30) NOT NULL,
  `leave_designation_status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `emp_leave_2`
--

CREATE TABLE `emp_leave_2` (
  `id` int(11) NOT NULL,
  `leave_type` varchar(40) NOT NULL,
  `leave_from` date NOT NULL,
  `leave_to` date NOT NULL,
  `leave_days` int(6) NOT NULL,
  `leave_reason` varchar(50) NOT NULL,
  `leave_status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `emp_timesheet_1`
--

CREATE TABLE `emp_timesheet_1` (
  `id` int(11) NOT NULL,
  `timesheet_employee_id` varchar(10) NOT NULL,
  `timesheet_employee_name` varchar(30) NOT NULL,
  `timesheet_designation_status` varchar(30) NOT NULL,
  `timesheet_project` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `emp_timesheet_2`
--

CREATE TABLE `emp_timesheet_2` (
  `id` int(11) NOT NULL,
  `timesheet_dataissue` date NOT NULL,
  `timesheet_datedeadline` date NOT NULL,
  `timesheet_total_hours` int(6) NOT NULL,
  `timesheet_remaining_hours` int(6) NOT NULL,
  `timesheet_description` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `table_contacts`
--

CREATE TABLE `table_contacts` (
  `id` int(11) NOT NULL,
  `country` varchar(30) NOT NULL,
  `present_address` varchar(70) NOT NULL,
  `permanent_address` varchar(70) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `table_general`
--

CREATE TABLE `table_general` (
  `id` int(11) NOT NULL,
  `your_name` varchar(50) NOT NULL,
  `father_name` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `age` varchar(20) NOT NULL,
  `height_weight` varchar(50) NOT NULL,
  `date_of_birth` varchar(30) NOT NULL,
  `marital_status` varchar(30) NOT NULL,
  `languages_known` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `table_job`
--

CREATE TABLE `table_job` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `employee_id` varchar(50) NOT NULL,
  `date_of_appointment` varchar(30) NOT NULL,
  `date_of_confirmation` varchar(30) NOT NULL,
  `date_of_joining` varchar(30) NOT NULL,
  `department_code` varchar(10) NOT NULL,
  `designation_code` varchar(10) NOT NULL,
  `education_qualification` varchar(70) NOT NULL,
  `professional_qualification` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_department`
--

CREATE TABLE `tb_department` (
  `id` int(11) NOT NULL,
  `department_code` varchar(10) NOT NULL,
  `department_name` varchar(40) NOT NULL,
  `department_location` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_department`
--

INSERT INTO `tb_department` (`id`, `department_code`, `department_name`, `department_location`) VALUES
(1, 'dep_1', 'kdjkfadsjkjkvxjk', 'kdjkflas');

-- --------------------------------------------------------

--
-- Table structure for table `tb_designation`
--

CREATE TABLE `tb_designation` (
  `id` int(11) NOT NULL,
  `designation_code` varchar(10) NOT NULL,
  `designation_name` varchar(40) NOT NULL,
  `designation_status` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_designation`
--

INSERT INTO `tb_designation` (`id`, `designation_code`, `designation_name`, `designation_status`) VALUES
(1, 'des_1', 'ksdjfk', 'skdfj');

-- --------------------------------------------------------

--
-- Table structure for table `tb_holiday`
--

CREATE TABLE `tb_holiday` (
  `id` int(11) NOT NULL,
  `holiday_name` varchar(30) NOT NULL,
  `holiday_country` varchar(20) NOT NULL,
  `holiday_day` varchar(20) NOT NULL,
  `holiday_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_leave_1`
--
ALTER TABLE `emp_leave_1`
  ADD PRIMARY KEY (`id`,`leave_employee_id`),
  ADD KEY `leave_employee_id` (`leave_employee_id`),
  ADD KEY `leave_employee_name` (`leave_employee_name`),
  ADD KEY `leave_designation_status` (`leave_designation_status`);

--
-- Indexes for table `emp_leave_2`
--
ALTER TABLE `emp_leave_2`
  ADD PRIMARY KEY (`id`),
  ADD KEY `leave_type` (`leave_type`),
  ADD KEY `leave_from` (`leave_from`),
  ADD KEY `leave_to` (`leave_to`),
  ADD KEY `leave_days` (`leave_days`),
  ADD KEY `leave_reason` (`leave_reason`),
  ADD KEY `leave_status` (`leave_status`);

--
-- Indexes for table `emp_timesheet_1`
--
ALTER TABLE `emp_timesheet_1`
  ADD PRIMARY KEY (`id`,`timesheet_employee_id`),
  ADD KEY `timesheet_employee_id` (`timesheet_employee_id`),
  ADD KEY `timesheet_employee_name` (`timesheet_employee_name`),
  ADD KEY `timesheet_designation_status` (`timesheet_designation_status`),
  ADD KEY `timesheet_project` (`timesheet_project`);

--
-- Indexes for table `emp_timesheet_2`
--
ALTER TABLE `emp_timesheet_2`
  ADD PRIMARY KEY (`id`),
  ADD KEY `timesheet_dataissue` (`timesheet_dataissue`),
  ADD KEY `timesheet_datedeadline` (`timesheet_datedeadline`),
  ADD KEY `timesheet_total_hours` (`timesheet_total_hours`),
  ADD KEY `timesheet_remaining_hours` (`timesheet_remaining_hours`),
  ADD KEY `timesheet_description` (`timesheet_description`);

--
-- Indexes for table `table_contacts`
--
ALTER TABLE `table_contacts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `country` (`country`),
  ADD KEY `present_address` (`present_address`),
  ADD KEY `permanent_address` (`permanent_address`),
  ADD KEY `email` (`email`),
  ADD KEY `phone` (`phone`);

--
-- Indexes for table `table_general`
--
ALTER TABLE `table_general`
  ADD PRIMARY KEY (`id`),
  ADD KEY `your_name` (`your_name`),
  ADD KEY `father_name` (`father_name`),
  ADD KEY `gender` (`gender`),
  ADD KEY `age` (`age`),
  ADD KEY `height_weight` (`height_weight`),
  ADD KEY `date_of_birth` (`date_of_birth`),
  ADD KEY `marital_status` (`marital_status`),
  ADD KEY `languages_known` (`languages_known`);

--
-- Indexes for table `table_job`
--
ALTER TABLE `table_job`
  ADD PRIMARY KEY (`id`,`department_code`,`designation_code`,`employee_id`),
  ADD KEY `id` (`id`),
  ADD KEY `title` (`title`),
  ADD KEY `employee_id` (`employee_id`),
  ADD KEY `date_of_appointment` (`date_of_appointment`),
  ADD KEY `date_of_confirmation` (`date_of_confirmation`),
  ADD KEY `date_of_joining` (`date_of_joining`),
  ADD KEY `department_code` (`department_code`),
  ADD KEY `designation_code` (`designation_code`),
  ADD KEY `education_qualification` (`education_qualification`),
  ADD KEY `professional_qualification` (`professional_qualification`);

--
-- Indexes for table `tb_department`
--
ALTER TABLE `tb_department`
  ADD PRIMARY KEY (`id`,`department_code`),
  ADD KEY `id` (`id`),
  ADD KEY `department_code` (`department_code`);

--
-- Indexes for table `tb_designation`
--
ALTER TABLE `tb_designation`
  ADD PRIMARY KEY (`id`,`designation_code`),
  ADD KEY `id` (`id`),
  ADD KEY `designation_code` (`designation_code`);

--
-- Indexes for table `tb_holiday`
--
ALTER TABLE `tb_holiday`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp_leave_1`
--
ALTER TABLE `emp_leave_1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emp_leave_2`
--
ALTER TABLE `emp_leave_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emp_timesheet_1`
--
ALTER TABLE `emp_timesheet_1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emp_timesheet_2`
--
ALTER TABLE `emp_timesheet_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `table_contacts`
--
ALTER TABLE `table_contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `table_general`
--
ALTER TABLE `table_general`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `table_job`
--
ALTER TABLE `table_job`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_department`
--
ALTER TABLE `tb_department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_designation`
--
ALTER TABLE `tb_designation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_holiday`
--
ALTER TABLE `tb_holiday`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `emp_leave_1`
--
ALTER TABLE `emp_leave_1`
  ADD CONSTRAINT `fk_leava_1` FOREIGN KEY (`leave_employee_id`) REFERENCES `table_job` (`employee_id`) ON DELETE CASCADE;

--
-- Constraints for table `emp_leave_2`
--
ALTER TABLE `emp_leave_2`
  ADD CONSTRAINT `leave_id_foreign` FOREIGN KEY (`id`) REFERENCES `emp_leave_1` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `emp_timesheet_1`
--
ALTER TABLE `emp_timesheet_1`
  ADD CONSTRAINT `fk_time_1` FOREIGN KEY (`timesheet_employee_id`) REFERENCES `table_job` (`employee_id`) ON DELETE CASCADE;

--
-- Constraints for table `emp_timesheet_2`
--
ALTER TABLE `emp_timesheet_2`
  ADD CONSTRAINT `time_id_foreign` FOREIGN KEY (`id`) REFERENCES `emp_timesheet_1` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `table_contacts`
--
ALTER TABLE `table_contacts`
  ADD CONSTRAINT `contact_id_foreign` FOREIGN KEY (`id`) REFERENCES `table_general` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `table_job`
--
ALTER TABLE `table_job`
  ADD CONSTRAINT `fk_1` FOREIGN KEY (`department_code`) REFERENCES `tb_department` (`department_code`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_2` FOREIGN KEY (`designation_code`) REFERENCES `tb_designation` (`designation_code`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
