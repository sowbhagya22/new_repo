create or replace schema if not exists new_db.new_sc;
 
 
-- Create the table
CREATE OR REPLACE TABLE if not exists new_sc.EMPLOYEES (
    ID INT,
    FIRST_NAME STRING,
    LAST_NAME STRING,
    DEPARTMENT STRING
);
 
-- Insert sample data
INSERT INTO new_sc.EMPLOYEES (ID, FIRST_NAME, LAST_NAME, DEPARTMENT) VALUES
    (1, 'John', 'Doe', 'Engineering'),
    (2, 'Jane', 'Smith', 'Marketing'),
    (3, 'Alice', 'Johnson', 'Finance'),
    (4, 'Bob', 'Brown', 'Human Resources');