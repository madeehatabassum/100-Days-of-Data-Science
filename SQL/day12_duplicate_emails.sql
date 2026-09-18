-- Day 12: Find Duplicate Emails
-- -----------------------------
-- Problem Statement:
-- Write a SQL query to find all duplicate emails in a table named Person.

-- Table Schema:
-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+

-- Solution 1: Using GROUP BY and HAVING
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;

-- Solution 2: Using Self Join
SELECT DISTINCT p1.Email
FROM Person p1
JOIN Person p2
ON p1.Email = p2.Email AND p1.Id <> p2.Id;
