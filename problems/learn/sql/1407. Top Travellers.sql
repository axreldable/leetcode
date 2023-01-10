# Write your MySQL query statement below
select u.name, travelled_distance from Users u
join
(
    select u.id, name, COALESCE(sum(distance), 0) as travelled_distance from Users u
    left join Rides r on u.id = r.user_id
    group by 1, 2
) a on u.id = a.id
order by 2 desc, 1