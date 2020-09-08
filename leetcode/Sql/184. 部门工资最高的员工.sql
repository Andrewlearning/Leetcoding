--Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。
--
--+----+-------+--------+--------------+
--| Id | Name  | Salary | DepartmentId |
--+----+-------+--------+--------------+
--| 1  | Joe   | 70000  | 1            |
--| 2  | Jim   | 90000  | 1            |
--| 3  | Henry | 80000  | 2            |
--| 4  | Sam   | 60000  | 2            |
--| 5  | Max   | 90000  | 1            |
--+----+-------+--------+--------------+
--Department 表包含公司所有部门的信息。
--
--+----+----------+
--| Id | Name     |
--+----+----------+
--| 1  | IT       |
--| 2  | Sales    |
--+----+----------+
--编写一个 SQL 查询，找出每个部门工资最高的员工。对于上述表，您的 SQL 查询应返回以下行（行的顺序无关紧要）。
--
--+------------+----------+--------+
--| Department | Employee | Salary |
--+------------+----------+--------+
--| IT         | Max      | 90000  |
--| IT         | Jim      | 90000  |
--| Sales      | Henry    | 80000  |
--+------------+----------+--------+

select B.Name as Department, A.Name as Employee, A.Salary
from
Employee as A join Department as B on A.DepartmentId = B.Id
where (A.DepartmentId, A.Salary) in

-- 因为 Employee 表里已经有工资了，所以我们可以先把每个部门的最高工资给找出来
-- 然后我们把表join在一起后，再把筛选出来的信息找出来
(
select DepartmentId, max(Salary)
from Employee
group by DepartmentId
);