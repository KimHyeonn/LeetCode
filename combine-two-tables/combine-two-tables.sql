/* Write your PL/SQL query statement below */
select Person.FirstName, Person.LastName, Address.City, Address.State 
from Person Left join Address on Person.PersonId = Address.PersonId;