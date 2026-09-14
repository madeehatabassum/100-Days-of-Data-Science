-- Day 8: SQL Window Functions
-- ---------------------------
-- Problem Statement:
-- Write a SQL query to find the top 3 salaries in each department.
-- Use window functions (DENSE_RANK).

SELECT Department, Employee, Salary
FROM (
    SELECT 
        d.Name AS Department,
        e.Name AS Employee,
        e.Salary,
        DENSE_RANK() OVER (PARTITION BY d.Id ORDER BY e.Salary DESC) as rnk
    FROM Employee e
    JOIN Department d ON e.DepartmentId = d.Id
) ranked_salaries
WHERE rnk <= 3;
