# Write your MySQL query statement below
select a.ID from weather a, weather b
where datediff(a.recorddate, b.recorddate) = 1 
and a.Temperature > b.Temperature;