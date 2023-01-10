# Write your MySQL query statement below
select coalesce(e_id, s_id) as employee_id from (
    SELECT e.employee_id as e_id, s.employee_id as s_id FROM Employees e
        LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    UNION
    SELECT e.employee_id as e_id, s.employee_id as s_id FROM Employees e
        RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
) a
where e_id is null or s_id is null
order by 1