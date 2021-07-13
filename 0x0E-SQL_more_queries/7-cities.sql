-- creates the database hbtn_0d_usa and the table cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT AUTO_INCREMENT PRIMARY KEY,
       state_id INT FOREIGN KEY REFERENCES states(id),
       name VARCHAR(256) NOT NULL);
