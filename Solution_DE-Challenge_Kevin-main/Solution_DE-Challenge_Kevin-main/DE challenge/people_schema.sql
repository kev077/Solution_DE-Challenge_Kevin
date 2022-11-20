drop table if exists people;

create table `people`(
`given_name` varchar(40),
`family_name` varchar(40),
`date_of_birth` date,
`place_of_birth` varchar(40),

FOREIGN KEY (`place_of_birth`) REFERENCES `places`(`city`)
);