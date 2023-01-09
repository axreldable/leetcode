# Write your MySQL query statement below
select actor_id, director_id from
(
    select actor_id, director_id, count(*) as c from ActorDirector
    group by 1, 2
    having c > 2
) as a;
