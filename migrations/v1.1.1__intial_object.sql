-- File: V1.1.1__intial_object.sql
CREATE TABLE users (
    id INT AUTOINCREMENT,
    name STRING,
    email STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
