-- Day 41: Managers with at Least 5 Direct Reports
-- ------------------------------------------------
-- Problem Statement: Find managers who have at least 5 direct reports.

SELECT m.name
FROM Employee e
JOIN Employee m ON e.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;
