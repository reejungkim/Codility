-- Implement your solution here

with x as (
        (
        select host_team as team_id,
        sum(case 
        when host_goals > guest_goals then 3
        when host_goals = guest_goals then 1
        else 0 end ) as num_points
        from matches
        group by host_team
        ) 
        UNION ALL
        (
        select guest_team as team_id,
        sum(case
        when guest_goals > host_goals then 3
        when guest_goals = host_goals then 1
        else 0 end) as num_points
        from matches
        group by guest_team 
        )
    )
select t.team_id, t.team_name, sum(coalesce(num_points,0)) as num_points 
from x
right join teams t on t.team_id = x.team_id 
group by t.team_id , team_name
order by sum(coalesce(num_points,0)) desc , t.team_id asc 



