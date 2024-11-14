-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: used_car_management_system
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('5f61af4e57cc');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `user_id` int NOT NULL,
  `listing_id` int NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `listing_id` (`listing_id`),
  CONSTRAINT `favorites_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_account` (`id`),
  CONSTRAINT `favorites_ibfk_2` FOREIGN KEY (`listing_id`) REFERENCES `used_car_listing` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
INSERT INTO `favorites` VALUES (10007,13),(10007,15),(10007,14),(10008,16),(10008,15),(10008,14),(10010,13),(10010,15),(10008,13);
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `agent_id` int NOT NULL,
  `rating` int NOT NULL,
  `comment` varchar(2555) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`agent_id`) REFERENCES `user_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,10009,5,'fege'),(2,10009,1,'1'),(3,10009,4,'test'),(4,10009,4,'f2r'),(5,10012,2,'151251'),(6,10012,5,'g2g23'),(7,10012,1,'testing\r\n'),(8,10012,5,'1512512');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `used_car_listing`
--

DROP TABLE IF EXISTS `used_car_listing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `used_car_listing` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) NOT NULL,
  `model` varchar(50) NOT NULL,
  `year` int NOT NULL,
  `price` float NOT NULL,
  `description` text,
  `seller_username` varchar(50) NOT NULL,
  `seller_id` int NOT NULL,
  `view_count` int DEFAULT NULL,
  `agent_id` int NOT NULL,
  `shortlisted_count` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `seller_id` (`seller_id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `used_car_listing_ibfk_1` FOREIGN KEY (`seller_id`) REFERENCES `user_account` (`id`),
  CONSTRAINT `used_car_listing_ibfk_2` FOREIGN KEY (`agent_id`) REFERENCES `user_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `used_car_listing`
--

LOCK TABLES `used_car_listing` WRITE;
/*!40000 ALTER TABLE `used_car_listing` DISABLE KEYS */;
INSERT INTO `used_car_listing` VALUES (13,'BMW','M51',2011,216169,'af','buyeracc',10008,108,10009,3),(14,'wewe','2042',2000,3251510,'','buyeracc',10008,47,10012,2),(15,'BMW','ndfjoqn',2013,215125,'ddfsf','selleracc',10010,25,10009,3),(16,'BMW2','hsh2012',2012,15125100,'wdgwegweg','selleracc',10010,7,10009,1),(17,'BMW23','1425',2013,15125100,'ygiionop','selleracc',10010,0,10009,0),(18,'1412','124124',123,14125100,'1245','a2234244',10001,0,10009,0);
/*!40000 ALTER TABLE `used_car_listing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_account`
--

DROP TABLE IF EXISTS `user_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role_id` int NOT NULL,
  `role_name` varchar(50) NOT NULL,
  `is_suspended` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_account_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `user_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10014 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_account`
--

LOCK TABLES `user_account` WRITE;
/*!40000 ALTER TABLE `user_account` DISABLE KEYS */;
INSERT INTO `user_account` VALUES (10001,'feb123231@fia.com','61247412512512','a2234244','a23r23523',3,'Buyer',1),(10002,'feab12345@fia.comag','66538019','vvsfasawd','a23r23523',1,'Admin',0),(10003,'yeehau_123@hotmail.com','66538019','a23423523','a23r23523',3,'Seller',0),(10004,'feb2@fia.com','66538019','wgfwg1e1e','a23r23523',3,'Seller',0),(10005,'feb12345@fia.comag1','66538019','a23423523qgqre','scrypt:32768:8:1$0O7wocERrIL8uOQt$e444f9468e0eb2d29e103d74637273f49ff0f9e2ae8cbb3adc2d63afb95f0b74d68d0642bd4f13a998bf205ac5705c30c5103fd083fbf127b229187f53dd8fb6',2,'Buyer',0),(10006,'feb@fia.comwgw','66538019','test1234','scrypt:32768:8:1$Kr8FIxUU87iuVv8l$3f54b4b4cae3b1369d6d0ee2f6b7fe5042a8f749b12e7094ff22344b2da8a6118e448045b586995d161a1a5504433a2a83d579e91c7bca92b1a29e82afc1f4ba',1,'Admin',0),(10007,'admin@admin.cim','12345678','adminacc','scrypt:32768:8:1$otuA5h3NamiHN5rK$fe5a9636419370d785dddb75773c27478dfeed0cc4659aa4d72b6038418c60b51a85a33bf05f5a9acf9960a3867a5992f0459b49913f9ef9c78b8fe44e423676',1,'Admin',0),(10008,'webfhwe@bfkjwfj.cim','2622','buyeracc','scrypt:32768:8:1$BWHgcitD4Mu98lTj$bd10f66c8f00eddbba520987ac2b6379c2a4292af345204db76f5d7440c2a8c09945c6b7a5d35c709ee7a49ed86b29aedf4d70cedab1177c6332f80092675ad9',2,'Buyer',0),(10009,'feb12345@fia.comag','12345678','agentacc','scrypt:32768:8:1$BVILvVW8yFBNL8H1$39d1165bab860e8b350211c6621eb0d9f8100d3ab7ba4053dd7119763abac6350c5c43316391175b648e51cec13d7f1342b8cac346e84ebd7e1c072ff596381c',4,'Agent',0),(10010,'feb12345@fia.comagadf','66538019','selleracc','scrypt:32768:8:1$G8rJFZS3bJkPn1S7$12b0bad7dc3e1ed29dd1f6393b4802558f3646edcf87ffff8da2cc079dba6d060c1933bdb242fb84ea3ea1ce29df25f9f13e39e307683720c0e0f4e7a498b5df',3,'Seller',0),(10011,'admin@admin.cim12412','1241254','adminacc2','scrypt:32768:8:1$YlqjSIfCwD1YM1jE$8f60bbd4dad1da25bffae639666f684bce21be2d30600dff353fb1a4bcfb4242acfa9e15534051c9ebc1b427ab89351a88827da22f9713ca530bc9a500f530ff',1,'Admin',0),(10012,'fasfqwQsd@vdvw','66538019','agentacc2','scrypt:32768:8:1$kPoTkdA7fN3mhIGf$5d655052bff28065a3fe244ef4974cbbdd0adf966b8b7db85870f42d72f63519035c1c6a9c1f240cfec0e3b543bba42624d80729d8850a5be97ff75f6fbda828',4,'Agent',0),(10013,'feb@fia.com1','12345678','adminacc3','scrypt:32768:8:1$MiWnulUCaLjvgKuD$3fb5d870139676d99c1aeb653ce441870941509ffb0d054b2add7c53af3dc64483f3940bbd1946ba70ad32bc7f5f45e374bc984ba104d7a08ff84e17f027061c',1,'Admin',0);
/*!40000 ALTER TABLE `user_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(50) NOT NULL,
  `description` text,
  `is_suspended` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--

LOCK TABLES `user_profile` WRITE;
/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;
INSERT INTO `user_profile` VALUES (1,'Admin','user admin',0),(2,'Buyer','car buyer',0),(3,'Seller','Car seller',0),(4,'Agent','Used Car Agent',0);
/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-14  1:19:41
