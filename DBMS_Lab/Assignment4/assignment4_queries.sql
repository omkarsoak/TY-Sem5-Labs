use railway;
alter table trainhalts 
add constraint time_verify CHECK( timein <= timeout);

alter table trainhalts add constraint train_fk
FOREIGN KEY (id) REFERENCES train(id) ON DELETE
CASCADE; 

insert into trainhalts values("AS34", 10, "DR", "20.12", "20.08");

CREATE DATABASE EXAM_CENTRE;
USE EXAM_CENTRE;

CREATE TABLE IF NOT EXISTS remotecentre(
	centreID varchar(255),
	college varchar(255), 
	town varchar(255), 
	state varchar(255),
	PRIMARY KEY (centreID)
);

create table person(
	ID varchar(255), 
	name varchar(255), 
	email varchar(255),
	PRIMARY KEY (ID)
);

create table programme(
	progId varchar(255), 
	title varchar(255), 
	fromdate date, 
	todate date,
	PRIMARY KEY (progId)
);

create table coordinator(
	ID varchar(255), 
	progID varchar(255), 
	centreId varchar(255),
	FOREIGN KEY (ID) references person (id),
	FOREIGN KEY (progID) references programme (progID),
	FOREIGN KEY (centreID) references remotecentre (centreID)
);

create table participant(
	ID varchar(255), 
	progID varchar(255), 
	centreId varchar(255),
	FOREIGN KEY (ID) references person (id),
	FOREIGN KEY (progID) references programme (progID),
	FOREIGN KEY (centreID) references remotecentre (centreID)
);

