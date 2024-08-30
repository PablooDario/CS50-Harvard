-- Create Schema for LinkedIn Database
CREATE DATABASE `linkedin`;
USE `linkedin`;

CREATE TABLE users (
    id INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    password VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE schools (
    id MEDIUMINT AUTO_INCREMENT NOT NULL,
    name VARCHAR(60) UNIQUE NOT NULL,
    type ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    location VARCHAR(30) NOT NULL,
    foundation_year SMALLINT UNSIGNED,
    PRIMARY KEY (id)
);

CREATE TABLE companies (
    id MEDIUMINT AUTO_INCREMENT NOT NULL,
    name VARCHAR(40) UNIQUE NOT NULL,
    industry ENUM('Technology', 'Education', 'Business'),
    location VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

-- Since 2 people can't have duplicated connections the PK is their id
CREATE TABLE people_connections (
    user_id_a INT NOT NULL,
    user_id_b INT NOT NULL,
    connection_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id_a, user_id_b),
    FOREIGN KEY (user_id_a) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id_b) REFERENCES users(id) ON DELETE CASCADE,
    CHECK (user_id_a != user_id_b)
);

-- A user can have multiple connections with a school i.e. (Primary, Secondary, etc...)
CREATE TABLE school_people_connections (
    id INT AUTO_INCREMENT NOT NULL,
    school_id MEDIUMINT NOT NULL,
    user_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    degree_type VARCHAR(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- A user can have multiple connections with a company, i.e. (Working from 2019-2021 and then return in 2024)
CREATE TABLE company_people_connections (
    id INT AUTO_INCREMENT NOT NULL,
    company_id MEDIUMINT NOT NULL,
    user_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
