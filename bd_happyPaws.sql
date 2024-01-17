create database happyPaws;
use happyPaws;

CREATE TABLE `tUsuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20),
  `ap1` varchar (25),
  `ap2` varchar (25),
  `correo` varchar (50),
  `url_imagen` varchar(3000) DEFAULT NULL,
   `telefono` char(9),
  `dirreccion` varchar(35) NOT NULL,
  `nombreUsuario` varchar(20) DEFAULT NULL,
   `cp` int,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tCanciones` DISABLE KEYS */;
INSERT INTO `tUsuarios` VALUES 
(1,'Juan','Gómez','Jimenez','juanjo@gmail.com','https://phantom-marca.unidadeditorial.es/d3812e417d3460b97ba0f791388324a0/resize/660/f/webp/assets/multimedia/imagenes/2023/05/31/16855351834075.jpg','673928310','Calle Juan, nº 3','juanFeliz',15012),
(2,'María','Fernando','Dolores','maridor@gmail.com','https://madreclelia.org/wp-content/uploads/2018/05/maria-1024x683.jpg','672683910','Calle María, nº 14','mariaDores',15004);
(3,'Esteban','Pan','Seco','estevomojado@gmail.com','https://phantom-marca.unidadeditorial.es/0837d63f10252ab5d3fd738bf8954c52/resize/660/f/webp/assets/multimedia/imagenes/2023/04/26/16825001443589.jpg','673920296','Calle Mirabeñ, nº 5','guapitoPlaya',15022),
(4,'Prasamsa','Castelao','López','prasita@gmail.com','https://img.freepik.com/fotos-premium/hermosa-chica-morena-posando-fotos-naturaleza_208861-7008.jpg?w=360','639519310','Calle Nepal, nº 67','praGuapa',15035),
(5,'Diana','Shevchenko','Alonso','shevchenkita@gmail.com','https://fotos.perfil.com/2022/08/28/trim/987/555/princesa-diana-1409510.jpg?webp','673836110','Calle Olmos, nº 34','dianitaMantequilla',15005),
(7,'Fran','Gómez','Segura','franuwuntu@gmail.com','https://estaticos-cdn.prensaiberica.es/clip/c7b63af7-f1e8-42af-9b7d-c063b20d60e9_media-libre-aspect-ratio_default_0.jpg','619528310','Calle Tonto, nº 2','franVuelve',14999),
(8,'Carlos','Luis','Arguiñano','juanjo@gmail.com','https://phantom-marca.unidadeditorial.es/d3812e417d3460b97ba0f791388324a0/resize/660/f/webp/assets/multimedia/imagenes/2023/05/31/16855351834075.jpg','673928310','Calle Cocina conmigo, nº 5','pepitoTernero',15012);
/*!40000 ALTER TABLE `tCanciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tComentarios`
--

CREATE TABLE `tAnimales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25),
  `url_imagen` varchar(3000),
  `edad` varchar (20),
  `especie` varchar(20),
  `raza` varchar(20),
  `genero` varchar(15),
  `descripcion` varchar(200),
  PRIMARY KEY (`id`)
); ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


LOCK TABLES `tAnimales` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
INSERT INTO `tAnimales` VALUES
(1,'Lucas','https://www.turismodeobservacion.com/media/fotografias/pato-criollo-117022-xl.jpg','2 meses','Pato','Criollo','Hembra','Bonita patita de plumaje oscuro'),
(2,'Bongo','https://www.aon.es/personales/seguro-perro-gato/wp-content/uploads/sites/2/2021/05/perro-boxer.jpg','11 años','Canino','Boxer','Macho','Bebito salvaje'),
(3,'Jerry','https://imagenes.20minutos.es/files/image_990_auto/files/fp/uploads/imagenes/2023/04/21/cobaya-peruana.r_d.591-389.jpeg','7 meses','Cobaya','Peruano','Macho','Es muy tranquilo, aunque le cuesta dormir'),
(4,'Leonardo','https://static.wikia.nocookie.net/reinoanimalia/images/d/d7/Tortuga_de_Orejas_Amarillas.jpg/revision/latest/scale-to-width-down/1000?cb=20171108105601&path-prefix=es','4 años','Tortuga','Orejas amarillas','Macho','Está un poco sordo'),
(5,'Terry','https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Laika01.jpg/1024px-Laika01.jpg','12 años','Canino','Terrier','Macho','Blanco como la nieve'),
(6,'Mikaela','https://www.cibsub.cat/rcs_gene/Serranus_cabrilla12.jpg','2 años','Pez','Cabrilla','Hembra','Es muy bonita'),
(8,'Copito','https://animales.me/wp-content/uploads/2020/04/Conejo-enano-blanco.jpg','1 año','Conejo','Toy','Hembra','Es muy apacible');

/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `tProductos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50),
  `url_imagen` varchar(3000),
  `precio` decimal(4,2),
  `marca` varchar(25),
  `stock` int,
  `tipoProducto` varchar(30),
  `tipoAnimal` varchar(30),
  `descripcion` varchar(300),
  PRIMARY KEY (`id`)
); ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
LOCK TABLES `tProductos` WRITE;
/*!40000 ALTER TABLE `tCanciones` DISABLE KEYS */;
INSERT INTO `tProductos` VALUES
(1,'PACIFIC SALMÓN PIENSO','https://www.kiwoko.com/dw/image/v2/BDLQ_PRD/on/demandware.static/-/Sites-kiwoko-master-catalog/default/dw7f7ca364/images/pienso_perros_true_origins_wild_pacific_adult_TRU70953_M.jpg?sw=385&sh=385','6.99','TRUE ORIGINS WILD','35','Pienso','Perros','Pienso con prebioticos, sin cereales y sabor a salmón para perros adultos.'),
(2,'POLLO PIENSO','https://www.kiwoko.com/dw/image/v2/BDLQ_PRD/on/demandware.static/-/Sites-kiwoko-master-catalog/default/dw1abaf86d/images/pienso_para_gatos_esterilizados_pollo_true_origins_TRU88968_M.jpg?sw=528&sh=528','20.99','TRUE ORIGINS PURE','30','pienso','Gatos','El True Origins Pure Adult Sterilised es un alimento seco con sabor a pollo para tus gatos esterilizados'),
(3,'KARLIE CUBO 4 BLOQUES JUEGO DE INTELIGENCIA ','https://www.roedorespark.com/777-large_default_2x/karlie-cubo-4-bloques-juego-de-inteligencia-para-conejos-y-roedores.jpg','16.79','KARLIE','20','Juguete','Conejos y roedores','Este juego de inteligencia es un cubo alargado con 4 bloques de madera que ocultan premios en su interior. Cada cubo lleva unida una pequeña cuerda. Estimula su inteligencia. Para conejos, cobayas, chinchillas, degus, ratas, hamsters sirios.'),
(4,'COLLAR PERRO','https://www.perrogato.net/10764-large_default/bolfo-perro-collar-70-cm-antiparasitario-externo.jpg','27.75','BOLFO','20','Collar','Perro','Infestaciones por moscas, garrapatas, pulgas y piojos'),
(5,'Plataforma de Tortuga de Césped','https://m.media-amazon.com/images/I/71tJQkBertL._AC_SL1500_.jpg','15.99','Yoaeyok','40','Plataforma de Tortuga','Tortuga','Yoaeyok Plataforma de Tortuga de Césped, Guaridas Hábitats Reptiles Tortugas Basking Plataforma con Ventosas, Tortuga Rampa Reptil Ladder Descanso Terraza, para Contenedor de Vidrio'),
(7,'FraPecera Betta','https://m.media-amazon.com/images/I/610SwaJlC3L._AC_SL1003_.jpg','21.39','UKCOCO','10','Pecera','Peces','Pecera Pequeña Pecera Transparente Pecera Pequeña con Partición Móvil Pecera Pecera para Peces Dorados Betta'),
(8,'Caseta para Patos ','https://m.media-amazon.com/images/I/71XM1oedZPL._AC_SL1500_.jpg','99.20','FINCA CASAREJO','10','Nido para Patos','Patos','espléndido nido de patos fabricado en madera tratada. Idóneo para Tarros, Corredor Indio o Dendrocygnas.');
/*!40000 ALTER TABLE `tCanciones` ENABLE KEYS */;
UNLOCK TABLES;
CREATE TABLE `tNoticias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50),
  `tituloPortada` date NOT NULL,
  `url_imagen` varchar(3000),
  `info_noticia` varchar(1000),
  PRIMARY KEY (`id`)
); ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `tNoticias` WRITE;
/*!40000 ALTER TABLE `tCanciones` DISABLE KEYS */;
INSERT INTO `tNoticias` VALUES
(1,'Adopción','Un perro consigue un hogar justo por Navidad tras pasar 500 días de refugio','https://fotografias.antena3.com/clipping/cmsimages01/2020/01/01/48D79222-01FD-4E42-9C5E-3A9BB0F96E2C/60.jpg','Bonita, un pit bull de seis años, pasó encerrada casi dos años en un refugio para animales abandonados de Nueva York. Todo el mundo daba por perdido que la adoptaran por su edad, pero no pudo tener mejor regalo de Navidad.'),
(2,'LOS FELINOS ESTÁN ENCANTADOS','Ikea dona camas de muñecas a un refugio de animales para que los gatos no duerman en el suelo','https://media.ambito.com/p/67e1cdc69057c1863724eddcd8269faa/adjuntos/239/imagenes/040/456/0040456799/gatos-portadajpg.jpg','Desde el refugio canadiense Etobicoke Humane Society, los voluntarios han dado las gracias a la empresa porque aunque sus suelos están limpios "no son cómodos para tumbarse".'),
(3,'Adopción','Una estupenda familia adopta a Copito','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ondavasca.com%2Fconejo-la-sociable-mascota-de-cuidado-facil-pero-especifico%2F&psig=AOvVaw1mkLvzxHK4UXUx7_SkUYv_&ust=1705518419223000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKjQ6LfN4oMDFQAAAAAdAAAAABAD','Copito fue adoptado por una estupensa familia con niños'),
(4,'Año Nuevo','Ayer dimos las campanadas','https://elrefugio.org/contenido/noticias/El-Refugio-PortadawebSanpe023_1.jpg','Ayer fue un día precioso. Volvió a ser fantástico compartir una soleada mañana junto tantas personas que se pusieron en marcha contra el abandono de animales.'),
(5,'Vacunación','Campaña de vacunación 2023.','https://elrefugio.org/contenido/noticias/El-Refugio-PortadawebVacunas023.jpg','Como cada año por estas fechas, El Refugio pone en marcha su Campaña de vacunación e identificación de perros y gatos.'),
(7,'Ternura','Una pizca de ternura','https://www.centroveterinariobarbanza.es/manejo-y-comportamiento_img8825t1m0w640h480.jpg','Nuevos integrantes de nuestro refugio, tres adorables conejos'),
(8,'Rescate','Patos rescatados de una granja','https://www.bbva.com/wp-content/uploads/2020/07/Patos-de-LAnec-5-Aglans-Gastronomia-Sostenible-de-BBVA-y-El-Celler-de-Can-Roca-768x550.jpg','Hace más de un mes que rescatamos a 8 patos de una granja.');
/*!40000 ALTER TABLE `tCanciones` ENABLE KEYS */;
UNLOCK TABLES;