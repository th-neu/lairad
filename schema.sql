-- --------------------------------------------------------
-- Host:                         192.168.1.6
-- Server-Version:               10.6.9-MariaDB - MariaDB Server
-- Server-Betriebssystem:        Linux
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Exportiere Datenbank-Struktur für lairad
DROP DATABASE IF EXISTS `lairad`;
CREATE DATABASE IF NOT EXISTS `lairad` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `lairad`;

-- Exportiere Struktur von Tabelle lairad.projects
DROP TABLE IF EXISTS `projects`;
CREATE TABLE IF NOT EXISTS `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` tinytext NOT NULL DEFAULT 'Name',
  `description` text NOT NULL DEFAULT 'description',
  `tasks` text NOT NULL DEFAULT 'tasks',
  `goal` text NOT NULL DEFAULT 'goal',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Daten-Export vom Benutzer nicht ausgewählt

-- Exportiere Struktur von Tabelle lairad.prompts
DROP TABLE IF EXISTS `prompts`;
CREATE TABLE IF NOT EXISTS `prompts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intro` text DEFAULT NULL,
  `constraints` text DEFAULT NULL,
  `commands` text DEFAULT NULL,
  `resources` text DEFAULT NULL,
  `performance_eval` text DEFAULT NULL,
  `response_form` text DEFAULT NULL,
  `outro` text DEFAULT NULL,
  `model` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Daten-Export vom Benutzer nicht ausgewählt

-- Exportiere Struktur von Tabelle lairad.thoughts
DROP TABLE IF EXISTS `thoughts`;
CREATE TABLE IF NOT EXISTS `thoughts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `thought_text` text NOT NULL,
  `reasoning_text` text NOT NULL,
  `criticism` text NOT NULL,
  `command` text NOT NULL,
  `command_args` text NOT NULL,
  `command_executed` set('True','False') NOT NULL DEFAULT 'False',
  `Timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `FK_thoughts_projects` (`project_id`),
  CONSTRAINT `FK_thoughts_projects` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Daten-Export vom Benutzer nicht ausgewählt

-- Exportiere Struktur von Tabelle lairad.users
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` tinytext DEFAULT NULL,
  `password` tinytext DEFAULT NULL,
  `theme` tinytext DEFAULT NULL,
  `is_admin` set('Value False','Value True') DEFAULT 'Value False',
  `user_groups` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- Daten-Export vom Benutzer nicht ausgewählt

-- Exportiere Struktur von Tabelle lairad.user_group
DROP TABLE IF EXISTS `user_group`;
CREATE TABLE IF NOT EXISTS `user_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` tinytext DEFAULT NULL,
  `created_by_admin` tinytext DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Daten-Export vom Benutzer nicht ausgewählt

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
