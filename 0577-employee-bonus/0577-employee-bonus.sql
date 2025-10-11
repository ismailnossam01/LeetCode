# Write your MySQL query statement below
select Employee.name, Bonus.bonus
from Employee 
Left join Bonus 
on Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;
