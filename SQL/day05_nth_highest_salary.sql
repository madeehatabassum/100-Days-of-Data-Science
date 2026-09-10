-- Day 5: Nth Highest Salary
-- -------------------------
-- Problem Statement:
-- Write a SQL query to get the nth highest salary from the Employee table.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT Salary 
      FROM Employee 
      ORDER BY Salary DESC 
      LIMIT 1 OFFSET N
  );
END
