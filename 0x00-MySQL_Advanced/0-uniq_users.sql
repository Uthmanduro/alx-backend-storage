-- creates a table users
USE holberton;
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
