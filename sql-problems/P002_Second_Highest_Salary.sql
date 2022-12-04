/*
----------------------------------------------------------------------------------------------------
-> Problem Title: 176. Second Highest Salary
-> Problem Status: Completed
-> Problem Attempted: 21/10/2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
SQL Schema
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+

id is the primary key column for this table.

Each row of this table contains information about the salary of an employee.

Write an SQL query to report the second highest salary from the Employee
table. If there is no second highest salary, the query should report null.

The query result format is in the following example.
 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

----------------------------------------------------------------------------------------------------
*/


-- Problems Solutions;;


/*
Status: Accepted
Summary:
By with the help of nested query. We are selecting the salary as a 
whole column from the Employee table database. Then using nested query
we only fetch the highest salary from the salary column table.
Then we finally return the salary < HighestSalary, by ordering and 
limiting rowws.
*/

select
	ifnull (
		(
			select salary 
			from Employee
			where salary < (select max(salary) from Employee limit 1)
			order by salary desc
			limit 1
		),
		null
	) as SecondHighestSalary


/*
Status: Accepted
Summary ~V3:
- dense_rank() is used with the over() function and order by clause
to list out any column data as rank.
on the basis of increasing or deceasing flow.
- If both values have same rank then dense_rank() will allocate the same rank
to both rows.
*/

select
    ifnull(
        (
            select salary from 
            (
                select *,dense_rank() over(order by salary desc) as "Ranking"
                from employee
            ) as temp
            where ranking = 2 limit 1            
        ), NULL
    ) as SecondHighestSalary


/*
Status: Rejected
Summary ~V2:
Simple query with the usage of limit and offset,
- Limit limits the quantity of the result, where
- Offset allows to skip the specified number of rows from start;
- Select ifnull($query, 'No Result Found'): If $query is None,
  Then the 'No Result Found' is returned.
 
Query: $Query retrieves all the salary in desc order, Limit 1 and Offset 1

BottleNeck: If 2 employees have same salaries,then result should be NULL

#Note: Limit 1 Offset 1 ~ Limit 1,1 i.e [0]:Offset & [1]:Limit;;
*/

Select 
    ifnull(
        (
            Select salary
            from employee
            Order by salary desc
            Limit 1 Offset 1
        ),NULL
    ) as SecondHighestSalary


/* 
Status: Accepted
Summary ~V1:
Simply select the first highest salary then again
run the same query to get the another highest salary
which is lesser than the first highest salary;;
*/

select max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee);