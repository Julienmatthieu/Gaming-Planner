CREATE TABLE `discordLocation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `guildId` text NOT NULL,
  `channelId` text NOT NULL,
  `messageId` text,
  `eventId` int NOT NULL,
  `on_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `on_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ID` (`id`) USING BTREE,
  KEY `eventID` (`eventId`),
  CONSTRAINT `discordLocation_ibfk_1` FOREIGN KEY (`eventId`) REFERENCES `event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=307 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `players` text,
  `time` text,
  `slots` int NOT NULL DEFAULT '1',
  `authorId` int NOT NULL,
  `role` text,
  `step` int NOT NULL DEFAULT '0',
  `players_id` text,
  `game_id` int DEFAULT NULL,
  `late` text,
  `on_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `on_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `author` (`authorId`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`authorId`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=278 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `game` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `image` text,
  `on_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `on_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `discordId` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `avatarUrl` text,
  `displayName` text,
  `mention` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `on_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `on_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

