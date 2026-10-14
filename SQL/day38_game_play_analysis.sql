-- Day 38: Game Play Analysis I
-- ----------------------------
-- Problem Statement: Report the first login date for each player.

SELECT player_id,
       MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
