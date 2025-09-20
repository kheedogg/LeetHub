with salary_rank as (
    select
        departmentId,
        salary,
        rank() over (partition by departmentId order by salary desc) as rnk
    from Employee
    group by 1, 2
)

select 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
from Employee e join Department d on e.departmentId = d.id
where (e.departmentId, e.salary) IN (select distinct departmentId, salary from salary_rank where rnk <= 3)