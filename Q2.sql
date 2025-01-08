
with x as (
select  
event_type,
value as value1,
lead(value) over(partition by event_type order by time desc) as value2,
row_number() over(partition by event_type order by time desc) as row
from events 
) 
select 
event_type, 
value1 - value2 as value
from x 
where row = 1 
and value2 is not null


'''
with rank_events as(
    select event_type, value, time, rank() over(partition by event_type order by time desc) as rank
    from events
)
select A.event_type, A.value - B.value as value
from (select * from rank_events where rank=1) A
join (select * from rank_events where rank=1) B 
on A.event_type = B.event_type
order by A.event type 
'''