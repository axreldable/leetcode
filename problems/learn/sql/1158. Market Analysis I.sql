# Write your MySQL query statement below
select buyer_id, join_date, sum(is_2019_order) as orders_in_2019 from
(
    select 
        user_id as buyer_id, join_date, 
        case
            when year(order_date) = 2019 then 1
            else 0
        end as is_2019_order
    from Users u
    left join Orders o on u.user_id = o.buyer_id
) a
group by 1, 2
order by 1;

--

select
    user_id as buyer_id,
    join_date,
    count(order_date) as orders_in_2019
from Users u
left join Orders o on u.user_id = o.buyer_id and year(order_date) = 2019
group by 1, 2
order by 1;
