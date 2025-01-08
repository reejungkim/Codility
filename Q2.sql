
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