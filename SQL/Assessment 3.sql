create table employees(
  emp_id INT,
  emp_name VARCHAR(50),
  dept_id INT,
  salary INT
)

 create table departments(
  dept_id INT,
  dept_name VARCHAR(50)
)

insert into departments values
(1, 'IT'),
(2, 'HR'),
(3, 'QC');

insert into employees values
(1,'harsh',3,20000),
(2,'dev',2,18000),
(3,'mann',1,19000),
(4,'shubham',2,15000),
(5,'keval',1,18000),
(6,'lalu',3,19000),
(7,'bhargav',1,14000);

--Display all employee details with department details
SELECT e.emp_id, e.emp_name, e.salary, e.dept_id, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

UPDATE employees
SET salary = 66000
WHERE emp_name = 'bhargav';
select * from employees;

--Display all details of employees earning more than 50,000

SELECT e.emp_id, e.emp_name, e.salary, e.dept_id, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
WHERE e.salary > 50000;

--Display department-wise total salary (with department details)
select d.dept_id, d.dept_name,
SUM(e.salary)as total_salary
from employees e
inner join departments d
on e.dept_id = d.dept_id
group by d.dept_id, d.dept_name;

--Display all employee & department details where department has more than 2 employees
SELECT e.emp_id, e.emp_name, e.salary, d.dept_id, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
WHERE e.dept_id IN (
    SELECT dept_id
    FROM employees
    GROUP BY dept_id
    HAVING COUNT(emp_id) > 2
);

--Display all employee details without a department
SELECT e.emp_id,
       e.emp_name,
       e.salary,
       e.dept_id
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

