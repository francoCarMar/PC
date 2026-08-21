SELECT name as Employee FROM employee e
WHERE salary > (
    SELECT salary as salary_manger
    FROM employee e_m
    WHERE e_m.id = e.managerid
)
