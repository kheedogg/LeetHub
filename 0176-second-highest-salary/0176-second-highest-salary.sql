# Write your MySQL query statement below

## 1)
-- SELECT
--     (
--         SELECT DISTINCT salary 
--         FROM Employee 
--         ORDER BY salary DESC
--         LIMIT 1
--         OFFSET 1
--     ) AS SecondHighestSalary


## 2)
select max(salary) as SecondHighestSalary 
from employee 
where salary < (select max(salary) from employee)
