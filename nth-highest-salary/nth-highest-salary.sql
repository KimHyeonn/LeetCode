CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select distinct Salary into result
    from (select dense_rank() over (order by Salary desc) as Ranks, Salary
          from Employee) A
    where A.Ranks = N;
    RETURN result;
END;