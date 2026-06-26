CREATE DATABASE placement_db;

USE placement_db;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    cgpa DECIMAL(3,2),
    attendance INT,
    internships INT,
    projects INT,
    skills VARCHAR(100),
    placement_status VARCHAR(20)
);