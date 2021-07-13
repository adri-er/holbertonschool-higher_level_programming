-- creates the database hbtn_0d_usa and the table states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT PRIMARY KEY AUTO_INCREMENT,
name NOT NULL VARCHAR(256));
