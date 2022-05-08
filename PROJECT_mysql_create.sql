CREATE TABLE `ΠΕΛΑΤΗΣ` (
	`EMAIL` varchar(40) NOT NULL,
	`ΤΗΛΕΦΩΝΟ` varchar(14) NOT NULL,
	`ΑΡΙΘΜΟΣ` INT(3) NOT NULL,
	`ΤΚ` INT(5) NOT NULL,
	`ΟΔΟΣ` varchar(20) NOT NULL,
	`ΟΝΟΜΑ` varchar(20) NOT NULL,
	`ΕΠΩΝΥΜΟ` varchar(20) NOT NULL,
	`ID_ΠΕΛΑΤΗ` varchar(20) NOT NULL,
	`ΦΥΛΟ` varchar(10) NOT NULL,
	`ΗΛΙΚΙΑ` INT(4) NOT NULL,
	PRIMARY KEY (`ID_ΠΕΛΑΤΗ`)
);

CREATE TABLE `ΧΩΡΟΣ` (
	`ΟΝΟΜΑ_ΧΩΡΟΥ` varchar(20) NOT NULL,
	`ID_ΧΩΡΟΥ` varchar(20) NOT NULL,
	`ΤΗΛΕΦΩΝΟ` varchar(14) NOT NULL,
	`ΟΝΟΜΑ` varchar(20) NOT NULL,
	`ΕΠΩΝΥΜΟ` varchar(20) NOT NULL,
	`ΘΕΣΕΙΣ` INT(10) NOT NULL,
	`ΠΡΟΣΒΑΣΗ_ΑΜΕΑ` varchar(3) NOT NULL,
	`ΑΡΙΘΜΟΣ` INT(3) NOT NULL,
	`ΝΟΜΟΣ` varchar(20) NOT NULL,
	`ΠΟΛΗ` varchar(20) NOT NULL,
	`ΟΔΟΣ` varchar(50) NOT NULL,
	PRIMARY KEY (`ID_ΧΩΡΟΥ`)
);

CREATE TABLE `ΕΙΣΗΤΗΡΙΟ` (
	`ΚΟΣΤΟΣ` INT(5) NOT NULL,
	`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ` varchar(20) NOT NULL,
	`ΗΜΕΡΟΜΗΝΙΑ_ΚΡΑΤΗΣΗΣ` DATE NOT NULL,
	`ΚΩΔΙΚΟΣ_ΠΕΛΑΤΗ` varchar(20) NOT NULL,
	`ΤΥΠΟΣ_ΕΙΣΗΤΗΡΙΟΥ` varchar(10) NOT NULL,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ`)
);

CREATE TABLE `ΕΚΔΗΛΩΣΗ` (
	`TARGET_GROUP` varchar(50) NOT NULL,
	`ΗΜΕΡΟΜΗΝΙΑ_ΔΙΕΞΑΓΩΓΗΣ` DATE NOT NULL,
	`ID_ΕΚΔΗΛΩΣΗΣ` varchar(20) NOT NULL,
	`ΩΡΑ_ΕΝΑΡΞΗΣ` TIME NOT NULL,
	`ΚΩΔΙΚΟΣ_ΧΩΡΟΥ` varchar(20) NOT NULL,
	`ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ` varchar(30) NOT NULL,
	`ΔΙΑΘΕΣΙΜΑ_ΕΙΣΗΤΗΡΙΑ` varchar(6) NOT NULL,
	PRIMARY KEY (`ID_ΕΚΔΗΛΩΣΗΣ`)
);

CREATE TABLE `ΚΑΤΗΓΟΡΙΑ` (
	`ID_ΚΑΤΗΓΟΡΙΑΣ` varchar(20) NOT NULL,
	`ΕΙΔΟΣ` varchar(20) NOT NULL,
	`ΟΝΟΜΑ_ΚΑΤΗΓΟΡΙΑΣ` varchar(30) NOT NULL,
	PRIMARY KEY (`ID_ΚΑΤΗΓΟΡΙΑΣ`)
);

CREATE TABLE `ΚΑΛΛΙΤΕΧΝΗΣ` (
	`ΟΝΟΜΑ` varchar(20) NOT NULL,
	`ΕΠΩΝΥΜΟ` varchar(20) NOT NULL,
	`ΚΑΛΛΙΤΕΧΝΙΚΟ_ΟΝΟΜΑ` varchar(30) NOT NULL,
	`ΕΙΔΟΣ` varchar(20) NOT NULL,
	`ID_ΚΑΛΛΙΤΕΧΝΗ` varchar(20) NOT NULL,
	PRIMARY KEY (`ID_ΚΑΛΛΙΤΕΧΝΗ`)
);

CREATE TABLE `ΔΙΟΡΓΑΝΩΤΗΣ` (
	`ΤΗΛΕΦΩΝΟ` varchar(14) NOT NULL,
	`EMAIL` varchar(40) NOT NULL,
	`ΟΝΟΜΑ` varchar(20) NOT NULL,
	`ΕΠΩΝΥΜΟ` varchar(20) NOT NULL,
	`ID_ΔΙΟΡΓΑΝΩΤΗ` varchar(20) NOT NULL,
	`ΔΙΟΡΓΑΝΩΤΡΙΑ_ΕΤΑΙΡΕΙΑ` varchar(30) NOT NULL,
	PRIMARY KEY (`ID_ΔΙΟΡΓΑΝΩΤΗ`)
);

CREATE TABLE `ΕΧΕΙ` (
	`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ_ΕΙΣΗΤΗΡΙΟΥ` varchar(20) NOT NULL,
	`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` varchar(20) NOT NULL,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ_ΕΙΣΗΤΗΡΙΟΥ`,`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`)
);

CREATE TABLE `ΑΝΗΚΕΙ` (
	`ΚΩΔΙΚΟΣ_ΚΑΤΗΓΟΡΙΑΣ` varchar(20) NOT NULL,
	`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` varchar(20) NOT NULL,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ_ΚΑΤΗΓΟΡΙΑΣ`,`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`)
);

CREATE TABLE `ΔΙΟΡΓΑΝΩΝΕΙ` (
	`ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ` varchar(20) NOT NULL,
	`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` varchar(20) NOT NULL,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ`,`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`)
);

CREATE TABLE `ΣΥΜΜΕΤΕΧΕΙ` (
	`ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ` varchar(20) NOT NULL,
	`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` varchar(20) NOT NULL,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ`,`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`)
);

ALTER TABLE `ΕΙΣΗΤΗΡΙΟ` ADD CONSTRAINT `ΕΙΣΗΤΗΡΙΟ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΠΕΛΑΤΗ`) REFERENCES `ΠΕΛΑΤΗΣ`(`ID_ΠΕΛΑΤΗ`);

ALTER TABLE `ΕΚΔΗΛΩΣΗ` ADD CONSTRAINT `ΕΚΔΗΛΩΣΗ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΧΩΡΟΥ`) REFERENCES `ΧΩΡΟΣ`(`ID_ΧΩΡΟΥ`);

ALTER TABLE `ΕΧΕΙ` ADD CONSTRAINT `ΕΧΕΙ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ_ΕΙΣΗΤΗΡΙΟΥ`) REFERENCES `ΕΙΣΗΤΗΡΙΟ`(`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ`);

ALTER TABLE `ΕΧΕΙ` ADD CONSTRAINT `ΕΧΕΙ_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) REFERENCES `ΕΚΔΗΛΩΣΗ`(`ID_ΕΚΔΗΛΩΣΗΣ`);

ALTER TABLE `ΑΝΗΚΕΙ` ADD CONSTRAINT `ΑΝΗΚΕΙ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΚΑΤΗΓΟΡΙΑΣ`) REFERENCES `ΚΑΤΗΓΟΡΙΑ`(`ID_ΚΑΤΗΓΟΡΙΑΣ`);

ALTER TABLE `ΑΝΗΚΕΙ` ADD CONSTRAINT `ΑΝΗΚΕΙ_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) REFERENCES `ΕΚΔΗΛΩΣΗ`(`ID_ΕΚΔΗΛΩΣΗΣ`);

ALTER TABLE `ΔΙΟΡΓΑΝΩΝΕΙ` ADD CONSTRAINT `ΔΙΟΡΓΑΝΩΝΕΙ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ`) REFERENCES `ΔΙΟΡΓΑΝΩΤΗΣ`(`ID_ΔΙΟΡΓΑΝΩΤΗ`);

ALTER TABLE `ΔΙΟΡΓΑΝΩΝΕΙ` ADD CONSTRAINT `ΔΙΟΡΓΑΝΩΝΕΙ_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) REFERENCES `ΕΚΔΗΛΩΣΗ`(`ID_ΕΚΔΗΛΩΣΗΣ`);

ALTER TABLE `ΣΥΜΜΕΤΕΧΕΙ` ADD CONSTRAINT `ΣΥΜΜΕΤΕΧΕΙ_fk0` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ`) REFERENCES `ΚΑΛΛΙΤΕΧΝΗΣ`(`ID_ΚΑΛΛΙΤΕΧΝΗ`);

ALTER TABLE `ΣΥΜΜΕΤΕΧΕΙ` ADD CONSTRAINT `ΣΥΜΜΕΤΕΧΕΙ_fk1` FOREIGN KEY (`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) REFERENCES `ΕΚΔΗΛΩΣΗ`(`ID_ΕΚΔΗΛΩΣΗΣ`);

