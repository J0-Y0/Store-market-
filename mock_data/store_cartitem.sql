-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: store_market
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `store_cartitem`
--

LOCK TABLES `store_cartitem` WRITE;
/*!40000 ALTER TABLE `store_cartitem` DISABLE KEYS */;
INSERT INTO `store_cartitem` VALUES (1,49,'293b6d5ba95b41de9a1adfd799ea8277',96),(2,9,'82b4c9ecb10f4241b952f44ddd3db7c4',53),(3,31,'0c35823f522e432889d1d90fff3af356',28),(4,41,'4615094041774657b899599369fa7fab',15),(5,9,'9ee88c1512354e6a81ed2d38eda68da1',4),(6,8,'f05ac658b61749f3afc10430cdd3e73c',19),(7,50,'9ee88c1512354e6a81ed2d38eda68da1',40),(8,31,'e84e9bf567d34280a51f996155a1ef95',2),(9,31,'539efd2c92934b7da999569b8862d070',86),(10,13,'946ec94fba094854b0a36241c478a820',87),(11,12,'617d7a0bfa554b9781b1e88f71f758b9',68),(12,23,'cec61b2f910a498f98401b230c4782b7',71),(13,47,'9ee88c1512354e6a81ed2d38eda68da1',67),(14,4,'8e7485934049429aa6e83e264c937afb',74),(15,12,'293b6d5ba95b41de9a1adfd799ea8277',57),(16,25,'946ec94fba094854b0a36241c478a820',6),(17,37,'539efd2c92934b7da999569b8862d070',20),(18,36,'82b4c9ecb10f4241b952f44ddd3db7c4',89),(19,5,'8565deac46594b0d81a3220764cf5735',96),(20,5,'d4948d34c215442d8e7d496826e256c5',68),(21,24,'c0c0d11501be48b1b3ba67130fc30c4f',27),(22,49,'293b6d5ba95b41de9a1adfd799ea8277',26),(23,4,'ba0a6258d87d4907a99b56cf6ffc0275',26),(24,31,'9ee88c1512354e6a81ed2d38eda68da1',25),(25,17,'8565deac46594b0d81a3220764cf5735',72),(26,13,'dbc0ebad6c3345e384dbc8cf1b30a770',39),(27,16,'a4ada82c97e344b5a10d32c4823d6468',76),(28,46,'8565deac46594b0d81a3220764cf5735',10),(29,23,'3a689cca8fb5445d83fb165a0266e18c',20),(30,20,'086a69b48ada4814be07f4792986d54a',33),(31,25,'293b6d5ba95b41de9a1adfd799ea8277',62),(32,25,'a4ada82c97e344b5a10d32c4823d6468',90),(33,27,'cec61b2f910a498f98401b230c4782b7',49),(34,49,'cec61b2f910a498f98401b230c4782b7',65),(35,47,'946ec94fba094854b0a36241c478a820',5),(36,38,'9ee88c1512354e6a81ed2d38eda68da1',12),(37,28,'c0c0d11501be48b1b3ba67130fc30c4f',90),(38,21,'5c961eda14b74a16879770bb7d731648',18),(39,40,'539efd2c92934b7da999569b8862d070',87),(40,39,'2b897913a615443e84a1fad0987dff94',94),(41,33,'4615094041774657b899599369fa7fab',70),(42,4,'293b6d5ba95b41de9a1adfd799ea8277',38),(43,24,'2ea1f0c904344583befa51659d0c7d68',7),(44,32,'617d7a0bfa554b9781b1e88f71f758b9',21),(45,14,'3a689cca8fb5445d83fb165a0266e18c',32),(46,47,'f5dbd0777ae745d4a889908f6a79a1cd',13),(47,35,'56b67068a7fe40408786cc3e5669cabe',3),(48,19,'4037bfc3ce2f47e5881a525c7332447f',33),(49,9,'9ce7b5e67bbf40eaa18d115f00e2be8f',61),(50,4,'cec61b2f910a498f98401b230c4782b7',87),(51,21,'82b4c9ecb10f4241b952f44ddd3db7c4',93),(52,12,'617a72fdb5804ca1840ff9e250819cec',16),(53,28,'2ea1f0c904344583befa51659d0c7d68',15),(54,49,'617a72fdb5804ca1840ff9e250819cec',72),(55,9,'f05ac658b61749f3afc10430cdd3e73c',86),(56,22,'ba0a6258d87d4907a99b56cf6ffc0275',53),(57,25,'c0c0d11501be48b1b3ba67130fc30c4f',28),(58,35,'4615094041774657b899599369fa7fab',34),(59,49,'8565deac46594b0d81a3220764cf5735',8),(60,28,'d4948d34c215442d8e7d496826e256c5',70),(61,16,'e60b9566c8574be38b88822c2fc0b5fc',78),(62,10,'293b6d5ba95b41de9a1adfd799ea8277',48),(63,23,'2ce81c5dc7434bcb9412e8aa9aa2934f',26),(64,40,'5c961eda14b74a16879770bb7d731648',20),(65,43,'56b67068a7fe40408786cc3e5669cabe',65),(66,38,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',95),(67,35,'c0c0d11501be48b1b3ba67130fc30c4f',55),(68,10,'2ce81c5dc7434bcb9412e8aa9aa2934f',99),(69,29,'fb57f67e9c8a4c13b03f24444e322396',21),(70,38,'086a69b48ada4814be07f4792986d54a',86),(71,3,'c0c0d11501be48b1b3ba67130fc30c4f',11),(72,3,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',14),(73,26,'afbd162a23604a21bf7289ab7ce88e76',9),(74,26,'5c961eda14b74a16879770bb7d731648',9),(75,17,'4615094041774657b899599369fa7fab',82),(76,22,'2ce81c5dc7434bcb9412e8aa9aa2934f',11),(77,14,'c27bd56e7b334b22a7c9c3078ea5641d',85),(78,3,'0c35823f522e432889d1d90fff3af356',41),(79,41,'ef086b11baee46d491d832273ca9f5b1',27),(80,48,'c27bd56e7b334b22a7c9c3078ea5641d',40),(81,8,'946ec94fba094854b0a36241c478a820',74),(82,3,'8e7485934049429aa6e83e264c937afb',23),(83,32,'8565deac46594b0d81a3220764cf5735',79),(84,50,'82b4c9ecb10f4241b952f44ddd3db7c4',97),(85,39,'ef086b11baee46d491d832273ca9f5b1',75),(86,39,'539efd2c92934b7da999569b8862d070',15),(87,35,'d4948d34c215442d8e7d496826e256c5',25),(88,26,'9b72931109454537b7cb48544db5ffd6',37),(89,5,'2ea1f0c904344583befa51659d0c7d68',78),(90,17,'f05ac658b61749f3afc10430cdd3e73c',62),(91,20,'293b6d5ba95b41de9a1adfd799ea8277',93),(92,50,'0c35823f522e432889d1d90fff3af356',13),(93,26,'3a689cca8fb5445d83fb165a0266e18c',65),(94,8,'f05ac658b61749f3afc10430cdd3e73c',14),(95,40,'9a2e38f1d0fc4c9798d20d862a891c14',68),(96,28,'4037bfc3ce2f47e5881a525c7332447f',3),(97,1,'617d7a0bfa554b9781b1e88f71f758b9',42),(98,17,'514efe473dd04503abdb499025b758e1',63),(99,41,'9b72931109454537b7cb48544db5ffd6',90),(100,49,'bd564e8a2e7845d69956d2a0aec91ab0',88),(101,46,'9a2e38f1d0fc4c9798d20d862a891c14',21),(102,20,'8e7485934049429aa6e83e264c937afb',56),(104,44,'5c961eda14b74a16879770bb7d731648',48),(105,24,'4615094041774657b899599369fa7fab',59),(106,43,'a4ada82c97e344b5a10d32c4823d6468',52),(107,43,'9b72931109454537b7cb48544db5ffd6',68),(108,41,'cec61b2f910a498f98401b230c4782b7',11),(110,21,'ba0a6258d87d4907a99b56cf6ffc0275',18),(111,38,'8565deac46594b0d81a3220764cf5735',67),(112,46,'c27bd56e7b334b22a7c9c3078ea5641d',18),(113,47,'a1d58084aed349f699d6fc8ce5d593b4',34),(114,30,'c27bd56e7b334b22a7c9c3078ea5641d',26),(115,4,'afbd162a23604a21bf7289ab7ce88e76',62),(116,20,'4037bfc3ce2f47e5881a525c7332447f',1),(117,23,'8565deac46594b0d81a3220764cf5735',14),(118,11,'086a69b48ada4814be07f4792986d54a',72),(119,41,'2ea1f0c904344583befa51659d0c7d68',44),(120,41,'ef086b11baee46d491d832273ca9f5b1',57),(121,38,'2ce81c5dc7434bcb9412e8aa9aa2934f',64),(122,10,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',93),(123,38,'9ce7b5e67bbf40eaa18d115f00e2be8f',88),(124,21,'2ea1f0c904344583befa51659d0c7d68',86),(125,13,'9ee88c1512354e6a81ed2d38eda68da1',14),(126,4,'8e7485934049429aa6e83e264c937afb',59),(127,26,'82b4c9ecb10f4241b952f44ddd3db7c4',77),(128,50,'f05ac658b61749f3afc10430cdd3e73c',6),(129,36,'a1d58084aed349f699d6fc8ce5d593b4',10),(130,39,'2ea1f0c904344583befa51659d0c7d68',69),(131,40,'d4948d34c215442d8e7d496826e256c5',39),(132,35,'a1d58084aed349f699d6fc8ce5d593b4',66),(133,20,'0c35823f522e432889d1d90fff3af356',6),(134,30,'2ce81c5dc7434bcb9412e8aa9aa2934f',67),(135,18,'a1d58084aed349f699d6fc8ce5d593b4',80),(136,13,'a1d58084aed349f699d6fc8ce5d593b4',45),(137,6,'4cf8906deb2e4d8f8faf65f1986a19ba',49),(138,3,'f05ac658b61749f3afc10430cdd3e73c',31),(139,44,'4037bfc3ce2f47e5881a525c7332447f',26),(140,43,'086a69b48ada4814be07f4792986d54a',95),(141,14,'4037bfc3ce2f47e5881a525c7332447f',37),(142,16,'cec61b2f910a498f98401b230c4782b7',57),(143,18,'0c35823f522e432889d1d90fff3af356',96),(144,5,'82b4c9ecb10f4241b952f44ddd3db7c4',75),(145,3,'2ea1f0c904344583befa51659d0c7d68',59),(146,24,'ef086b11baee46d491d832273ca9f5b1',7),(147,49,'82b4c9ecb10f4241b952f44ddd3db7c4',47),(148,21,'8e7485934049429aa6e83e264c937afb',89),(149,48,'8e7485934049429aa6e83e264c937afb',71),(150,25,'c0c0d11501be48b1b3ba67130fc30c4f',79),(151,20,'617a72fdb5804ca1840ff9e250819cec',73),(152,7,'cec61b2f910a498f98401b230c4782b7',34),(153,31,'e60b9566c8574be38b88822c2fc0b5fc',75),(154,25,'e60b9566c8574be38b88822c2fc0b5fc',24),(155,30,'4615094041774657b899599369fa7fab',23),(156,40,'9a2e38f1d0fc4c9798d20d862a891c14',32),(157,21,'5c961eda14b74a16879770bb7d731648',62),(158,8,'9b72931109454537b7cb48544db5ffd6',65),(159,48,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',40),(160,26,'4cf8906deb2e4d8f8faf65f1986a19ba',73),(161,13,'cec61b2f910a498f98401b230c4782b7',31),(162,24,'cec61b2f910a498f98401b230c4782b7',13),(163,28,'82b4c9ecb10f4241b952f44ddd3db7c4',8),(164,39,'afbd162a23604a21bf7289ab7ce88e76',74),(165,30,'9b72931109454537b7cb48544db5ffd6',89),(166,2,'4615094041774657b899599369fa7fab',9),(167,9,'5c961eda14b74a16879770bb7d731648',77),(168,14,'9ce7b5e67bbf40eaa18d115f00e2be8f',36),(169,29,'e84e9bf567d34280a51f996155a1ef95',70),(170,40,'a1d58084aed349f699d6fc8ce5d593b4',33),(171,20,'617d7a0bfa554b9781b1e88f71f758b9',31),(172,8,'4037bfc3ce2f47e5881a525c7332447f',56),(173,38,'f5dbd0777ae745d4a889908f6a79a1cd',57),(174,23,'cec61b2f910a498f98401b230c4782b7',53),(175,41,'514efe473dd04503abdb499025b758e1',83),(176,22,'e60b9566c8574be38b88822c2fc0b5fc',63),(177,21,'5c961eda14b74a16879770bb7d731648',87),(178,31,'617a72fdb5804ca1840ff9e250819cec',13),(179,25,'2b897913a615443e84a1fad0987dff94',20),(180,15,'086a69b48ada4814be07f4792986d54a',7),(181,33,'bd564e8a2e7845d69956d2a0aec91ab0',41),(182,4,'539efd2c92934b7da999569b8862d070',7),(183,11,'c0c0d11501be48b1b3ba67130fc30c4f',20),(184,28,'8e7485934049429aa6e83e264c937afb',33),(185,34,'9ee88c1512354e6a81ed2d38eda68da1',17),(186,43,'ba0a6258d87d4907a99b56cf6ffc0275',32),(187,45,'ef086b11baee46d491d832273ca9f5b1',63),(188,36,'4cf8906deb2e4d8f8faf65f1986a19ba',8),(189,24,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',67),(190,1,'293b6d5ba95b41de9a1adfd799ea8277',8),(191,15,'fb57f67e9c8a4c13b03f24444e322396',42),(192,4,'539efd2c92934b7da999569b8862d070',81),(193,26,'2b897913a615443e84a1fad0987dff94',60),(194,38,'4615094041774657b899599369fa7fab',88),(195,6,'ef086b11baee46d491d832273ca9f5b1',14),(196,30,'d4948d34c215442d8e7d496826e256c5',74),(197,31,'afbd162a23604a21bf7289ab7ce88e76',71),(198,15,'9a2e38f1d0fc4c9798d20d862a891c14',27),(199,31,'d4948d34c215442d8e7d496826e256c5',42),(200,20,'4cf8906deb2e4d8f8faf65f1986a19ba',58),(201,34,'9ce7b5e67bbf40eaa18d115f00e2be8f',68),(202,25,'a4ada82c97e344b5a10d32c4823d6468',21),(203,37,'fb57f67e9c8a4c13b03f24444e322396',83),(204,6,'fb57f67e9c8a4c13b03f24444e322396',37),(205,33,'82b4c9ecb10f4241b952f44ddd3db7c4',11),(206,17,'617a72fdb5804ca1840ff9e250819cec',100),(207,5,'d4948d34c215442d8e7d496826e256c5',59),(208,49,'9b72931109454537b7cb48544db5ffd6',22),(209,17,'2b897913a615443e84a1fad0987dff94',16),(210,17,'d4948d34c215442d8e7d496826e256c5',60),(211,5,'3a689cca8fb5445d83fb165a0266e18c',36),(212,26,'617d7a0bfa554b9781b1e88f71f758b9',20),(213,48,'82b4c9ecb10f4241b952f44ddd3db7c4',36),(214,24,'5c961eda14b74a16879770bb7d731648',28),(215,10,'4037bfc3ce2f47e5881a525c7332447f',100),(216,17,'a1d58084aed349f699d6fc8ce5d593b4',7),(217,23,'9ce7b5e67bbf40eaa18d115f00e2be8f',74),(218,32,'ef086b11baee46d491d832273ca9f5b1',64),(219,23,'e84e9bf567d34280a51f996155a1ef95',69),(220,21,'9ee88c1512354e6a81ed2d38eda68da1',23),(221,49,'8565deac46594b0d81a3220764cf5735',6),(222,8,'ef086b11baee46d491d832273ca9f5b1',74),(223,4,'514efe473dd04503abdb499025b758e1',47),(224,1,'8565deac46594b0d81a3220764cf5735',28),(225,30,'539efd2c92934b7da999569b8862d070',53),(226,13,'617d7a0bfa554b9781b1e88f71f758b9',83),(228,33,'3a689cca8fb5445d83fb165a0266e18c',77),(229,21,'cec61b2f910a498f98401b230c4782b7',48),(230,28,'c0c0d11501be48b1b3ba67130fc30c4f',37),(231,1,'f5dbd0777ae745d4a889908f6a79a1cd',77),(233,44,'e60b9566c8574be38b88822c2fc0b5fc',52),(234,22,'ef086b11baee46d491d832273ca9f5b1',35),(235,6,'c0c0d11501be48b1b3ba67130fc30c4f',8),(236,17,'82b4c9ecb10f4241b952f44ddd3db7c4',9),(237,30,'617d7a0bfa554b9781b1e88f71f758b9',81),(238,18,'a1d58084aed349f699d6fc8ce5d593b4',61),(239,17,'5c961eda14b74a16879770bb7d731648',85),(240,15,'4037bfc3ce2f47e5881a525c7332447f',63),(241,1,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',41),(242,38,'bd564e8a2e7845d69956d2a0aec91ab0',15),(243,26,'617d7a0bfa554b9781b1e88f71f758b9',16),(244,15,'9ee88c1512354e6a81ed2d38eda68da1',73),(245,25,'4037bfc3ce2f47e5881a525c7332447f',92),(246,47,'d4948d34c215442d8e7d496826e256c5',53),(247,26,'9a2e38f1d0fc4c9798d20d862a891c14',26),(248,11,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',72),(249,13,'c0c0d11501be48b1b3ba67130fc30c4f',88),(250,26,'ba0a6258d87d4907a99b56cf6ffc0275',93),(251,9,'9a2e38f1d0fc4c9798d20d862a891c14',62),(252,25,'3a689cca8fb5445d83fb165a0266e18c',75),(253,41,'e84e9bf567d34280a51f996155a1ef95',12),(255,16,'086a69b48ada4814be07f4792986d54a',80),(256,25,'afbd162a23604a21bf7289ab7ce88e76',85),(257,2,'2b897913a615443e84a1fad0987dff94',67),(258,41,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',91),(259,34,'e84e9bf567d34280a51f996155a1ef95',47),(260,49,'2ea1f0c904344583befa51659d0c7d68',23),(261,21,'0c35823f522e432889d1d90fff3af356',72),(262,39,'afbd162a23604a21bf7289ab7ce88e76',29),(263,47,'e84e9bf567d34280a51f996155a1ef95',11),(265,7,'539efd2c92934b7da999569b8862d070',31),(266,20,'bd564e8a2e7845d69956d2a0aec91ab0',53),(267,38,'946ec94fba094854b0a36241c478a820',95),(269,50,'e60b9566c8574be38b88822c2fc0b5fc',37),(270,24,'9b72931109454537b7cb48544db5ffd6',5),(271,37,'82b4c9ecb10f4241b952f44ddd3db7c4',10),(272,2,'56b67068a7fe40408786cc3e5669cabe',92),(273,2,'cec61b2f910a498f98401b230c4782b7',35),(274,6,'2b897913a615443e84a1fad0987dff94',88),(275,37,'4037bfc3ce2f47e5881a525c7332447f',29),(276,49,'2ce81c5dc7434bcb9412e8aa9aa2934f',18),(277,25,'2b897913a615443e84a1fad0987dff94',26),(279,45,'a4ada82c97e344b5a10d32c4823d6468',26),(280,1,'e84e9bf567d34280a51f996155a1ef95',25),(281,19,'ba0a6258d87d4907a99b56cf6ffc0275',4),(282,47,'946ec94fba094854b0a36241c478a820',93),(283,6,'9a2e38f1d0fc4c9798d20d862a891c14',100),(284,8,'086a69b48ada4814be07f4792986d54a',87),(285,46,'086a69b48ada4814be07f4792986d54a',25),(286,49,'a1d58084aed349f699d6fc8ce5d593b4',64),(288,41,'514efe473dd04503abdb499025b758e1',93),(289,33,'fb57f67e9c8a4c13b03f24444e322396',43),(290,46,'ba0a6258d87d4907a99b56cf6ffc0275',46),(291,8,'9a2e38f1d0fc4c9798d20d862a891c14',71),(292,12,'56b67068a7fe40408786cc3e5669cabe',50),(293,34,'2b897913a615443e84a1fad0987dff94',98),(294,21,'4615094041774657b899599369fa7fab',20),(295,38,'fb57f67e9c8a4c13b03f24444e322396',2),(296,26,'d4948d34c215442d8e7d496826e256c5',75),(297,30,'bd564e8a2e7845d69956d2a0aec91ab0',51),(298,19,'c27bd56e7b334b22a7c9c3078ea5641d',21),(299,30,'afbd162a23604a21bf7289ab7ce88e76',24),(300,44,'56b67068a7fe40408786cc3e5669cabe',54),(301,43,'4037bfc3ce2f47e5881a525c7332447f',68),(302,31,'8565deac46594b0d81a3220764cf5735',44),(303,15,'afbd162a23604a21bf7289ab7ce88e76',80),(304,7,'fb57f67e9c8a4c13b03f24444e322396',41),(305,13,'8565deac46594b0d81a3220764cf5735',92),(306,10,'4cf8906deb2e4d8f8faf65f1986a19ba',51),(307,18,'9b72931109454537b7cb48544db5ffd6',2),(308,44,'dbc0ebad6c3345e384dbc8cf1b30a770',46),(309,5,'ef086b11baee46d491d832273ca9f5b1',82),(310,11,'c0c0d11501be48b1b3ba67130fc30c4f',97),(312,18,'9b72931109454537b7cb48544db5ffd6',63),(313,30,'293b6d5ba95b41de9a1adfd799ea8277',15),(314,8,'9b72931109454537b7cb48544db5ffd6',82),(315,50,'2ea1f0c904344583befa51659d0c7d68',25),(316,21,'9b72931109454537b7cb48544db5ffd6',36),(317,18,'f5dbd0777ae745d4a889908f6a79a1cd',76),(318,22,'afbd162a23604a21bf7289ab7ce88e76',12),(319,37,'9ce7b5e67bbf40eaa18d115f00e2be8f',48),(320,2,'f05ac658b61749f3afc10430cdd3e73c',69),(321,36,'9a2e38f1d0fc4c9798d20d862a891c14',39),(322,1,'fb57f67e9c8a4c13b03f24444e322396',95),(323,9,'4cf8906deb2e4d8f8faf65f1986a19ba',89),(324,35,'2b897913a615443e84a1fad0987dff94',23),(325,45,'afbd162a23604a21bf7289ab7ce88e76',34),(326,25,'dbc0ebad6c3345e384dbc8cf1b30a770',21),(327,11,'2ce81c5dc7434bcb9412e8aa9aa2934f',41),(329,3,'56b67068a7fe40408786cc3e5669cabe',80),(330,49,'086a69b48ada4814be07f4792986d54a',77),(331,30,'539efd2c92934b7da999569b8862d070',4),(332,3,'946ec94fba094854b0a36241c478a820',88),(333,23,'2ea1f0c904344583befa51659d0c7d68',46),(334,36,'2ea1f0c904344583befa51659d0c7d68',61),(335,47,'3a689cca8fb5445d83fb165a0266e18c',87),(336,10,'539efd2c92934b7da999569b8862d070',66),(337,43,'afbd162a23604a21bf7289ab7ce88e76',41),(338,46,'82b4c9ecb10f4241b952f44ddd3db7c4',13),(339,28,'56b67068a7fe40408786cc3e5669cabe',71),(340,49,'56b67068a7fe40408786cc3e5669cabe',91),(341,4,'c27bd56e7b334b22a7c9c3078ea5641d',99),(342,47,'d4948d34c215442d8e7d496826e256c5',76),(343,10,'fb57f67e9c8a4c13b03f24444e322396',12),(344,38,'bd564e8a2e7845d69956d2a0aec91ab0',19),(345,50,'c0c0d11501be48b1b3ba67130fc30c4f',48),(346,45,'617a72fdb5804ca1840ff9e250819cec',94),(347,8,'f05ac658b61749f3afc10430cdd3e73c',48),(348,46,'d4948d34c215442d8e7d496826e256c5',16),(350,15,'a4ada82c97e344b5a10d32c4823d6468',85),(351,48,'f5dbd0777ae745d4a889908f6a79a1cd',18),(352,37,'fb57f67e9c8a4c13b03f24444e322396',78),(353,35,'617d7a0bfa554b9781b1e88f71f758b9',82),(354,50,'ef086b11baee46d491d832273ca9f5b1',59),(355,7,'56b67068a7fe40408786cc3e5669cabe',61),(356,37,'d4948d34c215442d8e7d496826e256c5',55),(357,18,'d4948d34c215442d8e7d496826e256c5',10),(374,21,'946ec94fba094854b0a36241c478a820',17),(375,2,'d4948d34c215442d8e7d496826e256c5',79),(376,10,'c27bd56e7b334b22a7c9c3078ea5641d',73),(377,15,'293b6d5ba95b41de9a1adfd799ea8277',17),(378,49,'be62ae7e0a0b4c2cbf7bbb3726f7d55a',70),(379,27,'086a69b48ada4814be07f4792986d54a',14),(380,25,'afbd162a23604a21bf7289ab7ce88e76',56),(426,13,'dbc0ebad6c3345e384dbc8cf1b30a770',63),(427,20,'539efd2c92934b7da999569b8862d070',55),(428,35,'afbd162a23604a21bf7289ab7ce88e76',75),(429,42,'4615094041774657b899599369fa7fab',6),(430,48,'a4ada82c97e344b5a10d32c4823d6468',89),(431,30,'fb57f67e9c8a4c13b03f24444e322396',9),(433,42,'539efd2c92934b7da999569b8862d070',6),(434,34,'dbc0ebad6c3345e384dbc8cf1b30a770',37),(435,47,'0c35823f522e432889d1d90fff3af356',94),(496,49,'8565deac46594b0d81a3220764cf5735',46),(497,30,'4cf8906deb2e4d8f8faf65f1986a19ba',47),(498,27,'8e7485934049429aa6e83e264c937afb',14),(499,17,'a1d58084aed349f699d6fc8ce5d593b4',42),(500,33,'539efd2c92934b7da999569b8862d070',69),(501,10,'ba0a6258d87d4907a99b56cf6ffc0275',95),(502,20,'2ea1f0c904344583befa51659d0c7d68',99),(503,50,'e84e9bf567d34280a51f996155a1ef95',90),(504,25,'82b4c9ecb10f4241b952f44ddd3db7c4',4),(505,9,'293b6d5ba95b41de9a1adfd799ea8277',55),(506,15,'56b67068a7fe40408786cc3e5669cabe',2),(507,6,'9b72931109454537b7cb48544db5ffd6',99),(508,10,'ef086b11baee46d491d832273ca9f5b1',21),(509,24,'e84e9bf567d34280a51f996155a1ef95',8),(510,47,'4615094041774657b899599369fa7fab',18),(511,33,'539efd2c92934b7da999569b8862d070',97),(512,15,'539efd2c92934b7da999569b8862d070',65),(513,44,'dbc0ebad6c3345e384dbc8cf1b30a770',59),(514,46,'2ea1f0c904344583befa51659d0c7d68',13),(515,45,'3a689cca8fb5445d83fb165a0266e18c',91),(516,34,'4615094041774657b899599369fa7fab',81),(517,10,'2ea1f0c904344583befa51659d0c7d68',14),(518,12,'3a689cca8fb5445d83fb165a0266e18c',100),(519,2,'9b72931109454537b7cb48544db5ffd6',66),(521,32,'086a69b48ada4814be07f4792986d54a',1);
/*!40000 ALTER TABLE `store_cartitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-02 13:23:09
