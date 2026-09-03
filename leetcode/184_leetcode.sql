WITH employee_department AS(
    SELECT d.name AS Department, 
        e.name AS Employee, 
        e.salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC)
    FROM Employee e
    LEFT JOIN Department d
        ON d.id = e.departmentId
)

SELECT Department, Employee, Salary 
FROM employee_department
WHERE dense_rank = 1