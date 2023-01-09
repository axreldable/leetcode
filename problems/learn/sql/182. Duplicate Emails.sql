# Write your MySQL query statement below
select email from
(select email, count(*) as c_e from Person group by 1 having c_e > 1) as e
