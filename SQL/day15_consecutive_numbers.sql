-- Day 15: Consecutive Numbers
-- ---------------------------
-- Problem Statement:
-- Write a SQL query to find all numbers that appear at least three times consecutively.

-- Table Schema:
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+

-- Solution using LAG and LEAD window functions
SELECT DISTINCT Num AS ConsecutiveNums
FROM (
    SELECT 
        Num,
        LAG(Num) OVER (ORDER BY Id) AS prev_num,
        LEAD(Num) OVER (ORDER BY Id) AS next_num
    FROM Logs
) t
WHERE Num = prev_num AND Num = next_num;
