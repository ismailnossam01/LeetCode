# Write your MySQL query statement below
SELECT MAX(num) as num
from MyNumbers

where num in 
(
    SELECT num
FROM MyNumbers
Group by num
having count(*) = 1
)