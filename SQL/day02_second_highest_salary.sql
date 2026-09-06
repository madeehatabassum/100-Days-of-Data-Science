-- Day 2: Second Highest Salary
-- ----------------------------
-- Problem Statement:
-- Write a SQL query to get the second highest salary from the Employee table.
-- If there is no second highest salary, then the query should return null.

-- Table Schema:
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- Solution 1: Using OFFSET (Standard SQL)
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary;

-- Solution 2: Using MAX() (More compatible across older databases)
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
