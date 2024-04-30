-- Create table for NBA teams
DROP TABLE team CASCADE CONSTRAINTS;
CREATE TABLE Team (
    name VARCHAR(15),
    num_players number(4) not null,
    record VARCHAR(6),
    location VARCHAR(50),
    primary key (name)
);

-- Create table for NBA players
DROP TABLE player CASCADE CONSTRAINTS;
CREATE TABLE Player (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    team VARCHAR(50),
    jersey_number varchar(2),
    age char(2),
    height char(2),
    PRIMARY KEY (first_name, last_name, team, jersey_number),
    FOREIGN KEY (team) REFERENCES Team(name)
);

-- Create table for NBA coaches
DROP TABLE coach CASCADE CONSTRAINTS;
CREATE TABLE Coach (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    team VARCHAR(50),
    age INT,
    primary key (last_name, team),
    FOREIGN KEY (team) REFERENCES Team(name)
);

-- Create table for mascots
DROP TABLE mascot CASCADE CONSTRAINTS;
CREATE TABLE Mascot (
    name VARCHAR(50) PRIMARY KEY,
    team VARCHAR(50),
    type VARCHAR(50),
    FOREIGN KEY (team) REFERENCES Team(name)
);