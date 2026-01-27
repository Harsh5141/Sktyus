use student;

--Find employees earning more than average salary
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

--Find department with highest total salary
SELECT d.dept_id, d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(e.salary) = (
    SELECT MAX(total_sal)
    FROM (
        SELECT SUM(salary) AS total_sal
        FROM employees
        GROUP BY dept_id
    ) t
);

--Display employee with second highest salary
select * from employees
where salary =(
select max(salary)
from employees
where salary<(select MAX (salary) from employees)
);

--Display employees working in the same department as "lalu"
 UPDATE employees
SET emp_name = 'Amit'
WHERE emp_name = 'keval';

select * from employees;

SELECT *
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);
