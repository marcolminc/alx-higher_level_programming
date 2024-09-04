-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates table states in the hbtn_0d_usa db
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
