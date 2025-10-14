# Write your MySQL query statement below
select *,
    IF(x+y>z AND y+z>x AND x+z>y, "Yes", "No") as triangle
FROM
    Triangle