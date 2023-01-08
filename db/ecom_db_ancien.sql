-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: ecom_db
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `release_date` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `artist_id` int DEFAULT NULL,
  `price` int NOT NULL,
  `stock_qty` int NOT NULL,
  `description` varchar(255) NOT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `artist_id` (`artist_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `album_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `album_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES (1,'Consequuntur sapiente dolorum.','2022-02-02T05:28:31.977Z','https://images.unsplash.com/photo-1470229538611-16ba8c7ffbd7?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODN8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',9,147,31,'Repudiandae culpa nisi fugiat cum quaerat dolores quidem voluptate officiis animi laborum asperiores eius earum.',10),(2,'Inventore saepe at.','2022-01-20T16:44:28.732Z','https://images.unsplash.com/photo-1518349182890-dea0f36534d0?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODJ8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',3,89,91,'Aliquam sequi voluptatibus expedita expedita occaecati velit itaque possimus aperiam suscipit hic reiciendis accusantium quibusdam.',3),(3,'Minima cupiditate occaecati.','2022-03-01T01:50:23.889Z','https://images.unsplash.com/photo-1595623075129-6dfb68aca674?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODV8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',3,121,48,'Labore quae eveniet inventore aliquid neque mollitia ipsa eaque hic cum voluptates labore maxime corporis.',10),(4,'Culpa quo.','2022-05-07T07:14:09.110Z','https://images.unsplash.com/photo-1578416489575-d90958228a5f?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODR8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',7,174,52,'Unde nostrum id magnam ex aut quibusdam itaque vero a ut vitae repellendus quam ab.',9),(5,'Sed sequi.','2022-05-07T12:39:19.812Z','https://images.unsplash.com/photo-1455997299803-0c4649ca02fa?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODZ8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',5,187,84,'Omnis culpa tempora commodi voluptates ullam recusandae ex recusandae nobis molestiae dolore similique suscipit.',7),(6,'Nisi quo dicta.','2022-08-12T23:14:30.962Z','https://images.unsplash.com/photo-1576269601089-aad0bbfa4f11?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODF8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',8,133,63,'Voluptatem officia laudantium facere dignissimos sit sapiente libero repellat sint iste quis corporis qui illum.',10),(7,'Alias voluptate dolore.','2022-01-27T21:13:04.981Z','https://images.unsplash.com/photo-1492560704044-e15259ca1c61?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTB8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',3,107,81,'Molestiae illo aliquam sit debitis assumenda aspernatur quasi eius nemo perspiciatis quos sequi autem magni.',10),(8,'Aperiam inventore.','2022-04-24T21:40:55.916Z','https://images.unsplash.com/photo-1544815633-1a8065078285?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODh8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',4,96,76,'Dicta maxime cupiditate illum nostrum quia molestias excepturi doloribus ipsam labore quo numquam dolorem recusandae corrupti.',5),(9,'Eum ad fuga.','2022-11-17T23:29:05.855Z','https://images.unsplash.com/photo-1510731491328-7363eecd7b2d?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODl8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',5,152,89,'Ea ad porro architecto eos cum ducimus vitae maxime doloribus quia commodi maxime ratione.',10),(10,'Nemo natus.','2022-01-21T23:28:25.510Z','https://images.unsplash.com/photo-1513269798455-b0c23c9e4d5b?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0ODd8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',7,110,46,'Debitis accusantium quam cum adipisci quia praesentium adipisci qui reprehenderit placeat assumenda molestiae praesentium similique omnis.',6),(11,'Nobis assumenda.','2022-02-08T04:13:51.785Z','https://images.unsplash.com/photo-1578125769963-ef5edfa5b0fc?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTR8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',5,164,86,'Aliquid iste nihil laboriosam est tempore adipisci quam perferendis consequatur minus ratione pariatur sed quibusdam maxime.',10),(12,'Odit ab.','2022-11-11T22:11:45.959Z','https://images.unsplash.com/photo-1465821185615-20b3c2fbf41b?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTV8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',10,123,60,'Blanditiis eligendi veritatis ratione voluptatem consequuntur voluptatibus officiis dolore dolorem ad minima aliquid ipsum.',5),(13,'Aliquid magnam facere.','2022-07-10T05:49:47.263Z','https://images.unsplash.com/photo-1579214449843-cab18dee2869?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTN8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',3,200,91,'Nemo expedita fugiat numquam porro est accusantium sequi unde temporibus natus animi aperiam molestias.',2),(15,'Facilis voluptas nihil.','2022-08-21T09:06:30.925Z','https://images.unsplash.com/photo-1445985543470-41fba5c3144a?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTJ8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',3,173,70,'Ullam error optio omnis ab quidem vel facilis doloremque recusandae autem sit totam odit.',5),(16,'Molestiae ducimus.','2022-04-29T18:41:31.061Z','https://images.unsplash.com/photo-1450044804117-534ccd6e6a3a?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTF8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',9,107,27,'Quo cupiditate blanditiis adipisci fugit quo sunt dolorum quasi quia eveniet corporis aliquid iure.',6),(17,'Molestiae officiis.','2022-08-04T12:12:58.870Z','https://images.unsplash.com/photo-1474752651386-dc296d69dc90?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTl8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',8,109,23,'Eligendi vel doloremque dolorem alias esse beatae numquam suscipit eum dolorem fugit laudantium autem quaerat.',6),(18,'Necessitatibus reiciendis.','2022-03-01T19:20:16.500Z','https://images.unsplash.com/photo-1505841993706-c8d90b412bc4?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTh8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',2,165,62,'Sapiente repudiandae similique ullam perferendis beatae repellendus debitis nam numquam sit earum eius laboriosam maxime.',5),(19,'Quidem quidem asperiores.','2022-11-22T19:52:03.049Z','https://images.unsplash.com/photo-1471275287446-f463543ee84f?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0OTd8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',8,155,61,'Labore illum vero facere eligendi quas autem ut aliquam culpa maxime ea vitae architecto.',9),(21,'Explicabo provident labore.','2022-06-07T19:57:52.155Z','https://images.unsplash.com/photo-1483101974978-cf266fdf1139?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MDR8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',7,102,20,'Dolores voluptates natus quae est repellendus deleniti iusto illum maiores laudantium eius eos voluptas.',6),(22,'Ullam illum odit.','2022-11-30T15:41:21.383Z','https://images.unsplash.com/photo-1517230878791-4d28214057c2?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MDV8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',10,96,59,'Culpa hic dicta voluptatem repellendus eum fugiat eaque nisi voluptates quas quo cumque repellat quos.',4),(23,'Adipisci reprehenderit.','2022-08-01T11:30:45.323Z','https://images.unsplash.com/photo-1485278537138-4e8911a13c02?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MDN8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',2,166,47,'Nam cum optio laudantium illo voluptatum odio voluptatibus voluptate dolor cum quasi consequuntur corrupti.',2),(25,'Sit suscipit.','2022-05-06T05:11:58.454Z','https://images.unsplash.com/photo-1550924972-6d13419fb0c7?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MDB8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',6,156,58,'Tempora ut mollitia placeat eius ipsam incidunt rerum alias quisquam eaque ullam ipsum vero nihil quia.',3),(27,'Quae ullam.','2022-11-15T04:38:31.984Z','https://images.unsplash.com/photo-1470345961863-06d4b12d93b3?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MDh8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',6,150,92,'Doloribus doloribus totam rerum provident sed possimus rerum quas blanditiis rerum eaque odit neque.',7),(29,'Natus neque consectetur.','2022-08-19T22:58:47.083Z','https://images.unsplash.com/photo-1593697909777-138e8c90ac91?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MTB8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',5,100,36,'Laborum error fugiat facere nulla consequatur enim aliquid fugit magnam fugiat quisquam magnam error harum placeat.',9),(30,'Libero beatae.','2022-10-17T10:30:27.141Z','https://images.unsplash.com/photo-1602973240044-ac77578f6dc5?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1MDd8fG11c2ljfGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',4,200,60,'Et debitis nulla dicta atque laudantium earum impedit consequatur necessitatibus itaque minima possimus dolores.',10);
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `date_of_birth` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES (1,'Assomption Cousin','Liétald Olivier','2008-09-12T09:44:22.932Z','https://images.unsplash.com/photo-1491609154219-ffd3ffafd992?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzMXx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(2,'Annabelle Dufour','Pie Garnier','2013-05-23T19:38:57.509Z','https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzM3x8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(3,'Charline Rey','Ferdinand Lefebvre','2007-09-23T00:50:57.568Z','https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzMnx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(4,'Aphélie Dupont','Ascelin Dubois DVM','1995-06-30T23:35:40.979Z','https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzNXx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(5,'Léonie Morin','Arthème Adam','2008-05-02T01:13:11.943Z','https://images.unsplash.com/photo-1664574654561-4c54605b1372?ixid=MnwxMDkyNjJ8MXwxfHNlYXJjaHwzNnx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(6,'Josselin Charpentier','Dieudonnée Marie','2003-08-04T21:01:26.832Z','https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzNHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(7,'Wandrille Adam','Zaché Jacquet','2021-05-05T05:46:47.023Z','https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0MHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(8,'Martine Riviere','Doriane Lefevre','2018-12-19T07:19:32.511Z','https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzOXx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(9,'Aymeric Robin','Annibal Lucas','2004-03-06T16:06:50.162Z','https://images.unsplash.com/photo-1554727242-741c14fa561c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzOHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000'),(10,'Barbe Paul','Mlle Fabien Henry IV','1996-07-14T14:41:59.865Z','https://images.unsplash.com/photo-1544723795-3fb6469f5b39?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzN3x8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0Mg&ixlib=rb-4.0.3&w=500&h=1000');
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'At.'),(2,'Repellendus beatae.'),(3,'Hic.'),(4,'Fugiat.'),(5,'Sapiente deleniti.'),(6,'Tempore.'),(7,'Eaque.'),(8,'Fugiat.'),(9,'Unde.'),(10,'Dolore.');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promo`
--

DROP TABLE IF EXISTS `promo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `start_date` varchar(255) NOT NULL,
  `end_date` varchar(255) NOT NULL,
  `rate` int NOT NULL,
  `album_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promo`
--

LOCK TABLES `promo` WRITE;
/*!40000 ALTER TABLE `promo` DISABLE KEYS */;
INSERT INTO `promo` VALUES (1,'2022-08-18T21:54:28.050Z','2022-11-06T19:26:41.810Z',19,39),(2,'2022-10-29T02:29:13.863Z','2022-09-29T00:12:34.308Z',29,3),(3,'2022-11-28T08:26:09.713Z','2022-07-06T14:46:05.210Z',20,25),(4,'2022-07-25T04:56:07.770Z','2022-09-22T12:41:44.673Z',17,9),(5,'2022-09-28T08:46:48.910Z','2022-11-11T07:23:21.921Z',30,3),(6,'2022-10-18T14:29:11.329Z','2022-11-29T17:58:17.870Z',24,17),(7,'2022-07-13T15:42:47.825Z','2022-09-19T00:37:36.238Z',19,33),(8,'2022-08-20T12:15:03.853Z','2022-08-09T12:40:17.188Z',20,19),(9,'2022-12-09T03:10:44.862Z','2022-11-02T05:47:37.084Z',23,38),(10,'2022-08-30T00:32:11.924Z','2022-08-14T23:11:33.716Z',16,39),(11,'2022-09-11T17:24:38.660Z','2022-08-12T17:04:17.411Z',17,16),(12,'2022-09-20T20:20:29.914Z','2022-12-10T16:55:52.795Z',26,26),(13,'2022-07-13T07:37:41.327Z','2022-12-12T09:26:35.160Z',17,28),(14,'2022-08-29T01:54:50.514Z','2022-11-27T15:11:45.065Z',13,17),(15,'2022-11-15T16:59:09.956Z','2022-10-20T10:14:20.639Z',29,14),(16,'2022-10-24T20:45:09.383Z','2022-07-17T00:40:50.179Z',20,13),(17,'2022-11-23T17:12:27.814Z','2022-10-25T07:02:19.124Z',20,33),(18,'2022-10-18T06:19:38.472Z','2022-10-21T08:48:03.196Z',27,10),(19,'2022-10-16T07:17:39.502Z','2022-07-31T10:45:44.078Z',17,5),(20,'2022-08-12T21:56:32.114Z','2022-07-11T11:13:10.253Z',28,5);
/*!40000 ALTER TABLE `promo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song`
--

DROP TABLE IF EXISTS `song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `release_date` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `album_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `album_id` (`album_id`),
  CONSTRAINT `song_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song`
--

LOCK TABLES `song` WRITE;
/*!40000 ALTER TABLE `song` DISABLE KEYS */;
INSERT INTO `song` VALUES (2,'Aperiam aliquam animi.','2022-05-18T05:32:57.354Z','https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwyfHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',7),(3,'Perferendis eum.','2022-12-05T22:41:23.663Z','https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw0fHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',7),(4,'Dolores iusto sit.','2022-08-24T01:16:01.522Z','https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzfHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',25),(5,'Consequuntur ratione corporis.','2022-02-13T22:49:34.028Z','https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw1fHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',13),(6,'Quos eligendi maxime.','2022-11-12T08:57:12.629Z','https://images.unsplash.com/photo-1552058544-f2b08422138a?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw2fHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',22),(7,'Quam architecto optio.','2022-03-17T12:07:35.329Z','https://images.unsplash.com/photo-1554151228-14d9def656e4?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw3fHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',4),(8,'Aliquid earum.','2022-07-31T18:19:35.891Z','https://images.unsplash.com/photo-1491349174775-aaafddd81942?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwxMHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',5),(12,'Deserunt ullam.','2022-09-26T04:28:15.157Z','https://images.unsplash.com/photo-1499952127939-9bbf5af6c51c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwxMXx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',11),(14,'Quod ratione.','2022-08-15T21:54:34.535Z','https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHw5fHxwZXJzb258ZW58MHx8fHwxNjY3NjkzMjQx&ixlib=rb-4.0.3&w=500&h=1000',19),(16,'Neque ipsa.','2022-09-02T14:36:34.765Z','https://images.unsplash.com/photo-1496302662116-35cc4f36df92?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwxOXx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',2),(17,'A tempore.','2022-11-12T22:31:11.265Z','https://images.unsplash.com/photo-1580489944761-15a19d654956?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwyMHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',6),(20,'Quas necessitatibus.','2022-06-16T00:08:45.260Z','https://images.unsplash.com/photo-1473830394358-91588751b241?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwxOHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',16),(23,'Fugiat et quae.','2022-06-11T18:41:43.934Z','https://images.unsplash.com/photo-1499482125586-91609c0b5fd4?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwyNHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',2),(25,'Magnam eius.','2022-10-14T22:37:45.256Z','https://images.unsplash.com/photo-1555952517-2e8e729e0b44?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwyN3x8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',6),(27,'Perspiciatis laudantium quis.','2022-07-15T20:11:29.446Z','https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzMHx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',17),(28,'Necessitatibus accusamus.','2022-03-21T09:01:58.225Z','https://images.unsplash.com/photo-1657214059189-6bace4ad1ab8?ixid=MnwxMDkyNjJ8MXwxfHNlYXJjaHwyOXx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',25),(30,'Nam quae animi.','2022-07-12T04:26:06.221Z','https://images.unsplash.com/photo-1581456495146-65a71b2c8e52?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwyNnx8cGVyc29ufGVufDB8fHx8MTY2NzY5MzI0MQ&ixlib=rb-4.0.3&w=500&h=1000',25);
/*!40000 ALTER TABLE `song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-06 16:30:07
