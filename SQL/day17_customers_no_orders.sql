-- Day 17: Customers Who Never Order
-- ---------------------------------
-- Problem Statement:
-- Write a SQL query to find all customers who never ordered anything.

-- Tables:
-- Customers: Id, Name
-- Orders: Id, CustomerId

-- Solution 1: Using LEFT JOIN
SELECT c.Name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.Id = o.CustomerId
WHERE o.Id IS NULL;

-- Solution 2: Using NOT IN
SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (
    SELECT CustomerId FROM Orders
);
