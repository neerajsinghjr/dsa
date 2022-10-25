--------------------------------------------------------------------------------------------
-- SQL Schema:
--------------------------------------------------------------------------------------------

--- Q01: Create Table
This statement is used to create a new table from an existing table. So, this table gets the same column definitions as that of the existing table.

for eg,

Syntax:
CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....;

for eg,
CREATE TABLE ExampleTable AS
SELECT Studentname, Parentname
FROM Students;

-- Q02: Alter Table
The ALTER command is used to add, modify or delete constraints or columns.

Syntax:
ALTER TABLE table_name
ADD column_name datatype;

-- Q03: Drop Table
The DROP command is used to delete the database, tables or columns.

Syntax:
DROP SCHEMA schema_name;

for eg,
DROP SCHEMA StudentsInfo;

-- Q04: TRUNCATE Table
This statement is used to delete the data which is present inside a table, but the table doesn’t get deleted.

for eg,
Syntax:
TRUNCATE TABLE table_name;

-- Q05: RENAME table 
This statement is used to rename one or more tables.

for eg,
Syntax:
RENAME TABLE 
    tbl_name TO new_tbl_name
    [, tbl_name2 TO new_tbl_name2] ...

-- Q06: Different Types Of Keys In Database
There are mainly 5 types of Keys, that can be mentioned in the database...
1) Candidate Key : The minimal set of attributes which can uniquely identify a tuple is known as a candidate key. A relation can hold more than a single candidate key, where the key is either a simple or composite key.
2) Super Key : The set of attributes which can uniquely identify a tuple is known as Super Key. So, a candidate key is a superkey, but vice-versa isn’t true.
3) Primary Key : A set of attributes that can be used to uniquely identify every tuple is also a primary key. So, if there are 3-4 candidate keys present in a relationship, then out those, one can be chosen as a primary key.
4) Alternate Key : The candidate key other than the primary key is called as an alternate key.
5) Foreign Key : An attribute that can only take the values present as the values of some other attribute, is the foreign key to the attribute to which it refers