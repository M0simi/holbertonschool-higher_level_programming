-- Create database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database
USE hbtn_0d_usa;

-- Creates table states with id as primary key, auto-increment, not null, unique
-- and name VARCHAR(256) NOT NULL
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);