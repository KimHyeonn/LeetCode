/* Write your PL/SQL query statement below */
select Email from (select distinct Email, count(Email) as cnt from Person
group by Email)
where cnt > 1;