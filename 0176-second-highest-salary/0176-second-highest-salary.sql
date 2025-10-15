# Write your MySQL query statement below
select MAX(e1.salary) as SecondHighestSalary
FROM Employee e1 INNER JOIN Employee e2 
ON e1.salary < e2.salary


-- | id | salary  | id | salary |
-- | -- | ------  | -- | ------ |
-- | 1  | 100     | 1  | 100    |
-- | 2  | 200     | 2  | 200    |
-- | 3  | 300     | 3  | 300    |