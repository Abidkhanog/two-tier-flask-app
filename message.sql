CREATE DATABASE IF NOT EXISTS messagedb;

USE messagedb;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO messages (name, message) VALUES ('Abid', 'Welcome to my Two-Tier DevOps project!');
