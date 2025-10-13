# Write your MySQL query statement below
SELECT ROUND(COUNT(player_id) / (SELECT COUNT(DISTINCT player_id) from Activity),2)as fraction


FROM
    Activity
WHERE(player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN (SELECT player_id, MIN(event_date) as first_date
FROM
    Activity 
GROUP BY
    player_id)