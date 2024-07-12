-- File: V1.1.1__intial_object.sql
CREATE or replace TABLE users (
    id INT AUTOINCREMENT,
    name STRING,
    email STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users (name, email)
VALUES 
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Alice Johnson', 'alice.johnson@example.com');

