# Write your MySQL query statement below
SELECT id, count(*) as num

FROM(
    SELECT requester_id as id FROM RequestAccepted

    UNION ALL 

    SELECT accepter_id FROM RequestAccepted
) as f

GROUP BY id
ORDER BY num desc 
limit 1