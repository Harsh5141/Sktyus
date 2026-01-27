--Count total number of students
SELECT COUNT(*) AS total_students
FROM students;


--Find average marks of students
SELECT AVG(marks) AS average_marks
FROM students;

--Find highest and lowest marks

SELECT 
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM students;

--Find department-wise average marks
 select Department, AVG(marks)AS
 average_marks
 from students
 group by department;

 --Display departments where average marks > 70
SELECT department, AVG(marks) AS average_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
