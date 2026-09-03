WITH cte_employee_department AS (
    SELECT d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    LEFT JOIN Department d
        ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM cte_employee_department
WHERE rnk IN (1,2,3)
