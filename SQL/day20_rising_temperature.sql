-- Day 20: Rising Temperature
-- --------------------------
-- Problem Statement:
-- Write a SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

-- Table Schema: Weather (Id, RecordDate, Temperature)

-- Solution using JOIN and DATEDIFF (MySQL/SQL Server syntax)
SELECT w1.Id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature;
