with x as (
select submission_date, 
    s.hacker_id , 
    h.name, 
    -- count(*) as count,
    rank() over(partition by submission_date order by count(*) desc, s.hacker_id asc) as rank 
from Submissions s
    join Hackers h on s.hacker_id= h.hacker_id
group by submission_date, s.hacker_id , h.name
    ) select x.submission_date, x.hacker_id, x.name from x 
    where rank =1;