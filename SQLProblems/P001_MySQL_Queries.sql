--------------------------------------------------------------------------------------------
-- Table Details Here:
-- Url: https://www.edureka.co/blog/interview-questions/sql-query-interview-questions
--------------------------------------------------------------------------------------------

-- Q01: Query to retrieve the first four characters of  EmpLname from the EmployeeInfo table
SELECT SUBSTRING(EmpLname, 1, 4) 
FROM EmployeeInfo;

-- Q02: Query to fetch the EmpFname from the EmployeeInfo table in upper case and use the ALIAS name as EmpName
SELECT UPPER(EmpFname) AS EmpName 
FROM EmployeeInfo;

-- Q03: Query to fetch the number of employees working in the department ‘HR’.
SELECT COUNT(*) 
FROM EmployeeInfo 
WHERE Department = 'HR';

-- Q04: Query to get the current date.
SELECT GETDATE();

-- Q05: Query to fetch only the place name(string before brackets) from the Address column like - (DEL), from EmployeeInfo table.
--- Solution #1: using the mid() function;
SELECT MID(EmpLname, 1, Locate(')', EmpLname))
from Customers;

--- Solution #2: Using the substring() function;
SELECT SUBSTRING(Address, 1, CHARINDEX('(',Address)) 
FROM EmployeeInfo;

-- Q06: Query to create a new table which consists of data and structure copied from the other table.
--- Solution #1: Using INTO Command;
SELECT * INTO NewTable FROM EmployeeInfo WHERE 1 = 0;

--- Solution #2: Using Create Table Command;
CREATE TABLE NewTable AS SELECT * FROM EmployeeInfo;

-- Q07: Query to find all the employees whose salary is between 50000 to 100000.
SELECT * 
FROM EmployeePosition 
WHERE Salary BETWEEN '50000' AND '100000';

-- Q08: Query to find the names of employees that begin with ‘S’
SELECT * 
FROM EmployeeInfo 
WHERE EmpFname LIKE 'S%';

-- Q09: Query to fetch top N records.
SELECT * 
FROM EmpPosition 
ORDER BY Salary DESC LIMIT N;

-- Q10: Query to retrieve the EmpFname and EmpLname in a single column as “FullName”. The first name and the last name must be separated with space.
SELECT CONCAT(EmpFname, ' ', EmpLname) AS 'FullName' 
FROM EmployeeInfo

-- Q11: Query find number of employees whose DOB is between 02/05/1970 to 31/12/1975 and are grouped according to gender.
SELECT COUNT(*), Gender 
FROM EmployeeInfo 
WHERE DOB BETWEEN '02/05/1970 ' AND '31/12/1975' 
GROUP BY Gender;

-- Q12: Query to fetch all the records from the EmployeeInfo table ordered by EmpLname in descending order and Department in the ascending order.
SELECT * 
FROM EmployeeInfo 
ORDER BY EmpFname desc, Department asc;

-- Q13: Query to fetch details of employees with the address as “DELHI(DEL
SELECT * 
FROM EmployeeInfo 
WHERE Address LIKE 'DELHI(DEL)%';

-- Q14: Query to fetch all employees who also hold the managerial position.
SELECT E.EmpFname, E.EmpLname, P.EmpPosition 
FROM EmployeeInfo E INNER JOIN EmployeePosition P ON
E.EmpID = P.EmpID AND P.EmpPosition IN ('Manager');

-- Q15: Query to fetch the department-wise count of employees sorted by department’s count in ascending order.
SELECT Department, count(EmpID) AS EmpDeptCount 
FROM EmployeeInfo GROUP BY Department 
ORDER BY EmpDeptCount ASC;

-- Q16: Query to calculate the even and odd records from a table.
--- Solution #1:
SELECT EmpID 
FROM (SELECT rowno, EmpID from EmployeeInfo) 
WHERE MOD(rowno,2)=0;

--- Solution #2:
SELECT EmpID 
FROM (SELECT rowno, EmpID from EmployeeInfo) 
WHERE MOD(rowno,2)=1;

-- Q17: Query to retrieve employee details from EmployeeInfo table who have a date of joining in the EmployeePosition table.
SELECT * FROM EmployeeInfo E 
WHERE EXISTS 
(SELECT * FROM EmployeePosition P WHERE E.EmpId = P.EmpId);

-- Q18: Query to retrieve two minimum and maximum salaries from the EmployeePosition table.
--- Solution #1:
SELECT DISTINCT Salary FROM EmployeePosition E1 
 WHERE 2 >= (SELECTCOUNT(DISTINCT Salary)FROM EmployeePosition E2 
  WHERE E1.Salary >= E2.Salary) ORDER BY E1.Salary DESC;

--- Solution #2:
SELECT DISTINCT Salary FROM EmployeePosition E1 
 WHERE 2 >= (SELECTCOUNT(DISTINCT Salary) FROM EmployeePosition E2 
  WHERE E1.Salary <= E2.Salary) ORDER BY E1.Salary DESC;

-- Q19: Query to find the Nth highest salary from the table without using TOP/limit keyword.
SELECT Salary 
FROM EmployeePosition E1 
WHERE N-1 = ( 
      SELECT COUNT( DISTINCT ( E2.Salary ) ) 
      FROM EmployeePosition E2 
      WHERE E2.Salary >  E1.Salary );

-- Q20: Query to retrieve duplicate records from a table.
SELECT EmpID, EmpFname, Department COUNT(*) 
FROM EmployeeInfo GROUP BY EmpID, EmpFname, Department 
HAVING COUNT(*) > 1;

-- Q21: Query to retrieve the list of employees working in the same department.
Select DISTINCT E.EmpID, E.EmpFname, E.Department 
FROM EmployeeInfo E, Employee E1 
WHERE E.Department = E1.Department AND E.EmpID != E1.EmpID;

-- Q22: Query to retrieve the last 3 records from the EmployeeInfo table.
SELECT * 
FROM EmployeeInfo 
WHERE EmpID <=3 UNION SELECT * FROM
(SELECT * FROM EmployeeInfo E ORDER BY E.EmpID DESC) 
AS E1 WHERE E1.EmpID <=3;

-- Q23: Query to find the third-highest salary from the EmpPosition table
SELECT TOP 1 salary
FROM(
SELECT TOP 3 salary
FROM employee_table
ORDER BY salary DESC) AS emp
ORDER BY salary ASC;

-- Q24: Query to display the first and the last record from the EmployeeInfo table.
--- Solution #1:
SELECT * 
FROM EmployeeInfo 
WHERE EmpID = (SELECT MIN(EmpID) FROM EmployeeInfo);

--- Solution #2:
SELECT * 
FROM EmployeeInfo 
WHERE EmpID = (SELECT MAX(EmpID) FROM EmployeeInfo);

-- Q25: Query to add email validation to your database
SELECT Email 
FROM EmployeeInfo 
WHERE NOT REGEXP_LIKE(Email, ‘[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}’, ‘i’);

-- Q26: Query to retrieve Departments who have less than 2 employees working in it.
SELECT DEPARTMENT, COUNT(EmpID) as 'EmpNo' 
FROM EmployeeInfo 
GROUP BY DEPARTMENT HAVING COUNT(EmpD) < 2;

-- Q27: Query to retrieve EmpPostion along with total salaries paid for each of them.
SELECT EmpPosition, SUM(Salary) 
from EmployeePosition 
GROUP BY EmpPosition;

-- Q28: Query to fetch 50% records from the EmployeeInfo table.
SELECT * 
FROM EmployeeInfo WHERE
EmpID <= (SELECT COUNT(EmpID)/2 from EmployeeInfo);

-- Q29: Query to fetch all those employees who work on Project other than P1.
--- Solution #1:
SELECT EmpId
FROM EmployeeSalary
WHERE Project <> 'P1';

--- Solution #2:
SELECT EmpId
FROM EmployeeSalary
WHERE NOT Project='P1';

-- Q30: Query to display the total salary of each employee adding the Salary with Variable value.
SELECT EmpId,
Salary+Variable as TotalSalary 
FROM EmployeeSalary;

-- Q31: Query to fetch the employees whose name begins with any two characters, followed by a text “hn” and ending with any sequence of characters.
SELECT FullName
FROM EmployeeDetails
WHERE FullName LIKE ‘__hn%’;

-- Q32: Query to fetch all the EmpIds which are present in either of the tables – ‘EmployeeDetails’ and ‘EmployeeSalary’.
SELECT EmpId FROM EmployeeDetails
UNION 
SELECT EmpId FROM EmployeeSalary;

-- Q33: Query to fetch common records between two tables.
--- Solution #1:
SELECT * FROM EmployeeSalary
INTERSECT
SELECT * FROM ManagerSalary;

--- Solution #2:
SELECT *
FROM EmployeeSalary
WHERE EmpId IN 
(SELECT EmpId from ManagerSalary);

-- Q34: Query to display both the EmpId and ManagerId together.
SELECT CONCAT(EmpId, ManagerId) as NewId
FROM EmployeeDetails;

-- Q35: Query to upper case the name of the employee and lower case the city values.
SELECT UPPER(FullName), LOWER(City) 
FROM EmployeeDetails;