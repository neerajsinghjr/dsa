````
-------------------------------------------------------------------------------------
-  Title : Sql Notes
-  Author: @neeraj-singh-jr
-  Status : Ongoing...
-  Created : 26/05/2023
-  Updated : 20/01/2024
-  Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-  Q028 : Trigger in Sql;;
-  Q027 : VIEWS in Sql;;
-  Q026 : COPYING DATA TO TABLE in Sql;;
-  Q025 : DROP TABLE CONSTRAINTS in Sql;;
-  Q024 : ALTER TABLE CONSTRAINTS in Sql;;
-  Q023 : CRUD TABLE & SCHEMA CONSTRAINTS in Sql;;
-  Q022 : INSERT INTO Table in Sql;;
-  Q021 : CREATE TABLE in Sql;;
-  Q020 : Subqueries in Sql;;
-  Q019 : INTERSECT & EXCEPT in Sql;;
-  Q018 : UNION clause in Sql;;
-  Q017 : JOIN - CARTENSIAN PRODUCT in Sql;;
-  Q016 : JOIN Relationship in Sql;;
-  Q015 : GROUP_CONCAT in Sql;;
-  Q014 : COUNT(*) vs COUNT(1) in Sql;;
-  Q013 : COUNT & GROUP BY in Sql;;
-  Q012 : COALESCE vs IFNULL in Sql;;
-  Q011 : COALESCE Clause in Sql;;
-  Q010 : IFNULL Clause in Sql;;
-  Q009 : Concatenation in Sql;;
-  Q008 : Case Clause in Sql;;
-  Q007 : Modify Data from Rows in Sql;;
-  Q006 : Arithmetic Operation in Sql;;
-  Q005 : Modulus in Sql;;
-  Q004 : Strftime function in sql;;
-  Q003 : Date and Time function in sql;;
-  Q002 : Sql Length function in sql;;
-  Q001 : Sql Core Fundamentals Topics;;
------------------------------------------------------------------------------------
````

### SQL NOTES (SQLITE): BEGINNING 

-------------------------------------------------------------------------------------
### Q028 : Trigger in Sql;;


**(NOTE: To List Trigger)**

````
SELECT * 
FROM information_schema.triggers
WHERE trigger_schema = 'public';
````

#### Step1: Create trigger function defination: backup_current_record();;

````
CREATE OR REPLACE FUNCTION backup_current_record()
RETURNS TRIGGER 
LANGUAGE PLPGSQL
  AS
$$
BEGIN
   IF (TG_OP = 'UPDATE') THEN
   
      INSERT INTO table_name(
            "merchant_transaction_id","amount",
            "mobile_no","request_payload",
            "response_payload","user_id",
            "created_date","updated_date", 
            "reported_by", "reported_date"
       )
      VALUES(
          OLD.merchant_transaction_id,OLD.amount,
          OLD.mobile_no,OLD.request_payload,
          OLD.response_payload,OLD.user_id,
          OLD.created_date,OLD.updated_date, 
          current_user, now()
      );
      
   END IF;

   RETURN NEW;
END;
$$;
````

#### Step2: Bind function backup_current_record() to trigger my_trigger;;

for eg,
````
CREATE TRIGGER my_trigger
  BEFORE UPDATE
  ON table_name
  FOR EACH ROW
  EXECUTE PROCEDURE backup_current_record();
````


-------------------------------------------------------------------------------------
### Q027 : VIEWS in Sql;;

(refer table: https://academy.bigbinary.com/learn-sql/views/views)

-  Consider a Scenario, Let's say we want to display the number of unique
   authors that have written a book for each course.

#### ONE WAY DOING IT USING JOINS...

```
SELECT courses.name,
COUNT(DISTINCT authorId)

FROM courses 
JOIN books
ON books.courseId = courses.id

WHERE courseId IS NOT NULL
GROUP BY courseId
```

#### ANOTHER WAY OF DOINT IT USING SUBQUERIES...

```
SELECT courses.name, 
booksSummary.authorsCount
FROM  courses 
JOIN (
   SELECT courseId,
   COUNT(DISTINCT authorId) as authorsCount
   FROM books
   WHERE courseId IS NOT NULL
   GROUP BY courseId
) AS booksSummary
ON courses.id = booksSummary.courseId
```

#### ONE WAY OF DOING IT USING VIEWS ...

```
--- VIEW START
CREATE VIEW booksSummary AS
SELECT      courseId,
            COUNT(DISTINCT authorId) as authorsCount
FROM        books
WHERE       courseId IS NOT NULL
GROUP BY    courseId;  
--- VIEWS ENDS;;

--- SQL START
SELECT   courses.name, 
         booksSummary.authorsCount
FROM     courses 
JOIN     booksSummary
ON       courses.id = booksSummary.courseId
```

NOTE: Sometimes, when there is an expected use of results of a subquery, we
can create them separate using an SQL property called VIEWs. Notice the set
of statements below.

-  eg1: Create a VIEW basicStudentData that contains these four columns: name,
   age, grade, marks. The data should be the name, age, grade and marks for
   all the students.
   Display all data from the VIEW basicStudentData.

```
--- FIRST ANSWER;;
create view basicStudentData as
select name, age, grade, marks from students;

select *
from basicStudentData

-- SECOND ANSWER;;
create view basicStudentData as
select name, grade, ma from students;

select basicStudentData.name, 
basicStudentData.age, 
basicStudentData.grade, 
basicStudentData.marks
from basicStudentData
```

-  eg2: Write a set of SQL statements to:

(ref table : https://academy.bigbinary.com/learn-sql/views/exercise-views-2)

```
KEY POINT 1 : Create a VIEW booksVolumeSeries that contains these two columns:
name, nextVolumeId. The data should be the name and the nextVolumeId for all
the books where nextVolumeId is present.

KEY POINT 2 : Use the VIEW booksVolumeSeries in combination with books to get
the name of the book and the name of the next volume for all the books that
have a next volume. The headers should be set as bookName and nextVolumeName
respectively.

create view bookVolumeSeries as 
-- first book version in here;;
select name, nextVolumeId
from books;

-- second book version in here;;
select fv.name as bookName, 
sv.name as nextVolumeName
from bookVolumeSeries as fv
join books as sv
on fv.nextVolumeId = sv.id
```

-  eg3: Write a set of SQL statements to:

(ref table: https://academy.bigbinary.com/learn-sql/views/exercise-views-3)

```
KEY POINT 1 : Create a VIEW booksCourses that contains these three columns:
bookId, bookName, courseName. The data should be the id, name and the name of
the course the book belongs to for all the books. For the books that do not
have a course that they belong to, courseName should be NULL.

KEY POINT 2 : Use the VIEW booksCourses in combination with authors and books
to get the name of the book, name of the author it belongs to and name of the
course it belongs to for all the books. For books that don't have an author
or course, the relevant columns should be NULL. The headers should be set as
bookName, authorName and courseName respectively.

-- SOLUTION 

create view booksCourses as 
select books.id as bookId,
books.name as bookName,
courses.name as courseName, 
books.authorID as authorid
from books 
left join courses
on courses.id = books.courseID;

select booksCourses.bookName as bookName,
authors.name as authorName
from booksCourses
left join authors
on booksCourses.authorid = authors.id
```


-------------------------------------------------------------------------------------
### Q026 : COPYING DATA TO TABLE in Sql;;

-  Let's say we want to copy over all the data from the students table below
   to a new table, called studentsCopy.

-  `NAIVE APPORACH` : One way of doing it is copying over all the data manually
   after creating a new table with same schema.

-  `OPTIMIZE APPROACH` : The other is using a subquery that returns a list of
   rows instead of the VALUES list of an INSERT INTO statement.

for eg,

````
CREATE TABLE studentsCopy (
   id INTEGER NOT NULL PRIMARY KEY,
   name TEXT NOT NULL,
   age INTEGER,
   grade INTEGER,
   course TEXT,
   marks INTEGER NOT NULL
);

INSERT INTO studentsCopy
SELECT * FROM students;

-  eg2: There is a students table below with a few columns. The table
   studentsClone has the exact same number and type of columns as students.
   The table studentsMarks has only id, name and marks columns that are same
   as students, and a few extra columns. Neither studentsClone, nor
   studentsMarks have any records.


INSERT INTO studentsClone
SELECT * FROM students;

/*
* NOTE: You have to specify the column name when you are only sending specific
* values to columns.
*/

INSERT INTO studentsMarks(id, name, marks)
select id, name, marks from students
````

#### UPDATING DATA USING SUBQUERIES;;

-  We can also use subqueries to upgrade the data of a table also

-  Note the subquery in the SET clause in UPDATE statement below.

for eg,

````
UPDATE students
SET courseName = (
   SELECT name
   FROM   courses
   WHERE  id = students.courseId
   LIMIT  1
);
````


-------------------------------------------------------------------------------------
### Q025 : DROP TABLE CONSTRAINTS in Sql;;

-  SQL has a DROP TABLE statement to delete/drop tables from a database.

-  SYNTAX :

````
DROP TABLE teachers

eg1: Write an SQL statement to delete the table courses from the database
information given below.

drop table courses
````


-------------------------------------------------------------------------------------
### Q024 : ALTER TABLE CONSTRAINTS in Sql;;

-  `ALTER TABLE` is used for making updates to the structure of a table.

#### ALTER TABLE: ADD COLUMN TO TABLE

-  SYNTAX : 
````
ALTER TABLE students
ADD COLUMN NEW_COLUMN_NAME TEXT

-  eg1: There are two tables courses and teachers, given below. Write a set of
   SQL statements to add these new columns to specified tables.

----------------------------------------------------------------
| table    |  new column | data type   |  constraint           |
----------------------------------------------------------------
| courses  |  startedIn  | INTEGER     | DEFAULT 2015          |
| teachers |  courseId   | INTEGER     | NOT NULL, DEFAULT 1   |         
----------------------------------------------------------------

alter table courses
add column startedin integer default 2015;

alter table teachers 
add column courseId integer not null default 1;
````

#### ALTER TABLE: RENAME COLUMNS;;

-  SYNTAX :

````
ALTER TABLE students 
rename column name to first_name;
````

#### ALTER TABLE: RENAME TABLE;;

-  SQL provides a RENAME TO variant to the ALTER TABLE statement, to solve
   this problem.

-  SYNTAX :

````
ALTER TABLE students 
rename to students_records
````

-------------------------------------------------------------------------------------
### Q023 : CRUD TABLE & SCHEMA CONSTRAINTS in Sql;;

#### NOT NULL FOR TABLE;;

- SYNTAX :

````
CREATE TABLE teachers (
   id INTEGER,
   name TEXT NOT NULL,
   age INTEGER
);

INSERT INTO teachers values (1,'neeru', '24')
````

#### UNIQUE CONSTRAINTS FOR TABLE;;

-  Let's create a new table books, and insert a few rows of records in it.

- SYNTAX :
````
CREATE TABLE books (
    id INTEGER,
    name TEXT UNIQUE,
    price REAL
);
````

#### DEFAULT CONSTRAINTS FOR TABLE

-  DEFAULT constraints is used to set default value of a table.

- SYNTAX :
````
CREATE TABLE books (
   id INTEGER NOT NULL,
   name TEXT NOT NULL,
   price REAL DEFAULT 350
);
````

#### CHECK CONSTRAINTS FOR TABLE;;

-  CHECK constraints is used to check whether the input value for a column is
   authenticate value or not in the table.

- SYNTAX :
````
CREATE TABLE teachers (
   id INTEGER,
   name TEXT NOT NULL,
   age INTEGER CHECK (age > 21),
   contact TEXT
);


eg2: Create a new table courses with the following columns, data types and
constraints.

----------------------------------------------------------------------
|  column         |  data type  |            constraint              |
----------------------------------------------------------------------
|  id             |  INTEGER    |         UNIQUE, NOT NULL           |
|  name           |   TEXT      |         UNIQUE, NOT NULL           |
|  abbreviation   |   TEXT      |         Length <= 3 chars          |
|  type           |   TEXT      | must be 'Language' or 'Framework'  |
----------------------------------------------------------------------


CREATE TABLE courses (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE,
    abbreviation TEXT CHECK (LENGTH(abbreviation) <= 3),
    type TEXT CHECK (type IN ('Language', 'Framework'))
);

INSERT INTO
    courses
VALUES
    (1, 'Ruby', 'rb', 'Language'),
    (2, 'Rails', 'rls', 'Framework');
````

#### PRIMARY KEY CONSTRAINT IN TABLE;;

-  PRIMARY KEY is used to recognize a row uniquely in the database.

- SYNTAX:
````
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL DEFAULT 350
 );
````

#### PRIMARY KEY with multiple columns

-  Multiple columns are eligible for acting as a primary key in a table.
   Usually, any column which is unique in nature can act as a primary key.

- SYNTAX : 
````
CREATE TABLE books (
 id INTEGER NOT NULL,
 name TEXT NOT NULL,
 price REAL DEFAULT 350,
 isbn TEXT NOT NULL,
 PRIMARY KEY (id, isbn)
);

INSERT INTO books VALUES (1, 'Basics of SQL', 333.50, 'e42b-3637-119b-5a6f');
INSERT INTO books VALUES (2, 'Java for Beginners', 280.40, '2c1c-d89b-df66-c5d4');
INSERT INTO books VALUES (3, 'Basics of SQL', 333.50, 'e42b-3637-119b-5a6f');
INSERT INTO books VALUES (1, 'Basics of SQL', 333.50, 'e42b-3637-119b-5a6f');
````

#### PRIMARY KEY AUTOINCREMENT;;

-  SQL provides an attribute called AUTOINCREMENT as an addition to the
   PRIMARY KEY constraint on a column, which automatically generates the
   appropriate PRIMARY KEY values.

- SYNTAX :
````
CREATE TABLE courses (
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   abbreviation TEXT NOT NULL
);
INSERT INTO courses (name, abbreviation) VALUES
('Ruby', 'rb'),
('SQL', 'sql'),
('Python', 'py');
````

#### FOREIGN KEY :

-  The FOREIGN KEY constraint on a table can be defined as a new item in the
   CREATE TABLE columns list. 

-  It starts with FOREIGN KEY followed by the name of the column which is to
   be declared as FOREIGN KEY in parentheses (in this case, courseId).

-   This is followed by the keyword REFERENCES and the name of the table whose
    PRIMARY KEY is referred (in this case, courses), followed by the name of
    the PRIMARY KEY

- SYNTAX :
````
CREATE TABLE students (
   id INTEGER NOT NULL PRIMARY KEY,
   name TEXT NOT NULL,
   age INTEGER NOT NULL,
   courseId INTEGER NOT NULL,
   gradeId INTEGER NOT NULL,
   FOREIGN KEY (courseId) REFERENCES courses (id)
);   
````

#### FOREIGN KEY WITH MULTIPLE COLUMNS 

-  It is same as it was in Foreign Key in the previous hashtag. Just right now
   it is being using for more than 2 columns. 

- SYNTAX :
````
--- GRADE TABLE;;
CREATE TABLE grades   (
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL
);

-- COURSE TABLE;;
CREATE TABLE COURSE (
   id INTEGER NOT NULL PRIMARY AUTOINCREMENT,
   name text not null,
   abbr text check(length(name) <= 3)
)

--- STUDENT TABLE;;
CREATE TABLE STUDENTS (
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   age INTEGER NOT NULL,
   courseId INTEGER NOT NULL,
   gradeId INTEGER NOT NULL,
   FOREIGN KEY (courseId) REFERENCES courses (id),
   FOREIGN KEY (gradeId) REFERENCES grade (id)
)
````

#### UPDATING COLUMN IN TABLE;;

- SYNTAX :
````
/*
NOTE: WITHOUT THE WHERE CLAUSE THIS QUERY WILL RUN FOR ALL ROWS IN THE TABLE;;
*/

UPDATE students
SET marks = marks + 5, 
name = 'Neerj Singh Jr.'
WHERE id = 5;
````

#### DELETE SPECIFIC DATA FROM TABLE;;

- SYNTAX :
````
/*
NOTE: WITHOUT THE WHERE CLAUSE THIS QUERY WILL RUN FOR ALL ROWS IN THE TABLE;;
*/

DELETE FROM students
WHERE marks BETWEEN 30 AND 70
````


-------------------------------------------------------------------------------------
###  Q022 : INSERT INTO Table in Sql;;

#### INSERT INTO TABLE BASIC

````
--- Case 1: Simple Insert
INSERT INTO teachers (1,'Abhishek Mishra', 27, '2023-06-09')

--- Case 2: alternative syntax with values
INSERT INTO students VALUES (2, 'Henry Mishra', 24, NULL)
````

#### INSERT MULTIPLE RECORDS;; 
for eg,

````
INSERT INTO students VALUES 
(19, 'Henry', NULL, 7, 'Java', 56),
(20, 'Galahad', 13, 6, 'JavaScript', 64),
(21, 'Arthur', 10, 4, 'Scala', 23)
````

#### INSERTING RECORD IN SPECIFIC COLUMNS 

````
--- Case 1: Target Specific Column and rest null

INSERT INTO students VALUES (19, 'Jiaying', NULL, 9, NULL, NULL)

--- Case 2: Alternative syntax with values 

INSERT INTO students (id, name, grade) VALUES (19, 'Jiaying', 9)

--- and, with multiple records

INSERT INTO students (id, name, grade) VALUES 
(19, 'Jiaying', 9),
(20, 'Gordon', 8),
(21, 'Ramsay', 7)
````

-------------------------------------------------------------------------------------
###  Q021 : Create Table in Sql;;

-  Create table is used to create table in your database.

- SYNTAX :
````
 
   CREATE TABLE teachers (
      id INTEGER,
      name TEXT,
      age INTEGER,
      joiningDate TEXT
    )
````

-  EXPLANATORY :
- `CREATE TABLE` is how an SQL statement to create a new table starts,
  followed by the name of the table that needs to be created.

- Then, define list of columns inside parentheses(()), each of which is
  constituted by the name of the column, data type of it. 

-  DATA TYPE: Tables used to define column must be defined along side with their data type.

     1) INTEGER: Stores values that are integer in nature
     2) REAL : Stores floating point numbers/decimal numbers
     3) TEXT : Stores character data
     4) BLOB : Stores binary large objects like files
     5) NULL : When the data type is not defined or unclear.


-------------------------------------------------------------------------------------
###  Q020 : Subqueries in Sql;;

-  `Subqueries` are used to write nested queries inside the main queries to
   fetch record from multiple tables efficiently.

-  `Subqueries` are always written inside the parenthesis for the Main Queries.

-  `Subqueries` are alaway executes before executing the main query.

for eg1: Write a query to display name, price and author's name for all books
which are priced higher than the highest priced book written by the author
Steve Strange

````
SELECT book.name as book, 
book.price as price, 
author.name as author
FROM books as book
join authors as author
on author.id = book.authorID
WHERE book.price > (

  select max(price) 
  from authors as author 
  join books as book 
  on book.authorID = author.id
  where author.name = 'Steve Strange'

)
````

for eg2: Write a query to display name, grade and marks of all students who have
scored marks which lie between the lowest marks scored by a student in grade
7 and the highest marks scored by a student in grade 6.

````
SELECT student.name as name, 
student.grade as grade, 
student.marks as marks
FROM students as student 
WHERE student.marks between (select min(marks) from students where grade = 7) and 
(select max(marks) from students where grade = 6)
````

for eg3: Write a query to display name and publisherName of all such books which
are published by a publisher who have worked with at least 3 distinct
authors (i.e. the total number of distinct authors who have written a book
with that publisher are 3 or more).

````
select book.name as book,
book.publishername as publisherName 
from books as book
where book.publishername in (
  select book.publishername
  from authors as author 
  join books as book
  on book.authorID = author.id 
  group by book.publishername
  having count(distinct author.id) >= 3
)
````

#### CORRELATED SUBQUERIES IN FROM CLAUSE;;

-  Let's say, for each book, we want to display the name and prices of books
   which are costlier than the average price of books published by the same
   publisher.

-  We can narrow down the above problem into two steps 

   STEP 1: The subquery in this case would be to figure out the average price
   of books for each publisher, something similar to following:

    ````
   select publisherName, AVG(price) AS avgPrice
   from books
   group by publisherName
    ````
  
   STEP 2: Results of the subquery (average book price) will have to be
   individually compared with each of our main parameters (book price), based

    ````
   select books.name, 
   books.price, 
   books.publisherName,
   publisherSummary.avgPrice AS publisherAvgPrice
   
   from books 
   join (
      select publisherName, AVG(price) AS avgPrice
      from books
      group by publisherName
   ) AS publisherSummary
   on books.publisherName = publisherSummary.publisherName

   where books.price > publisherSummary.avgPrice
    ````
   
for eg3: Let's say students have to read all the books that exist for the course
they are enrolled in. Write a query to display student's name, name of the
course and the number of books they have to read, for each student
````
--- CONSTRAINTS :

1) Skip the students who don't have a course, or don't have a valid course
(Think JOIN vs LEFT JOIN)

2) Do not skip the students who are enrolled in courses which have no books
belonging to them. Make sure 0 is shown in numberOfBooks for such students.
(Again, think JOIN vs LEFT JOIN)


--- QUERY SOLUTION;;

select students.name AS student,
courseSummary.courseName AS course,
courseSummary.numberOfBooks AS numberOfBooks
from students
join (
   
   SELECT courses.id AS courseId,
   courses.name AS courseName,
   count(books.id) AS numberOfBooks
   FROM courses
   LEFT JOIN books ON books.courseId = courses.id
   GROUP BY courses.Id

) as courseSummary 
on students.courseId = courseSummary.courseId
````

for eg5: Write an SQL query to list all course names in alphabetical order, and
for each of them, display the number of books that belong to them, and the
number of students that belong to them

````
--- CONSTRAINTS:

1) Display 0 for count of students as well as count of books if there are no
matching records for a course.

select tb1.course_name as course,
tb1.book_count as numberOfBooks,
tb2.student_count as numberOfStudents
from (
  select course.id as course_id,
  course.name as course_name, 
  count(book.id) as book_count
  from courses as course 
  left join books as book 
  on course.id = book.courseid 
  group by course_id, course_name
) as tb1

left join(
  select course.id as course_id,
  course.name as course_name, 
  count(student.id) as student_count
  from courses as course 
  left join students as student
  on student.courseid = course.id
  group by course_id, course_name
) as tb2

on tb1.course_id = tb2.course_id
group by course
order by course asc
````

#### CORRELATED SUBQUERIES IN WHERE CLAUSE;;

-  Subqueries can be used in the where clause also. 

for eg6: Let's say we want to filter out courses for which the average price of
books belonging to that course is more than 500.

````
select course.name as course_name
from courses as coure
join books as book
on course.id = book.courseID
group by course_name
having avg(book.price) < 500

--- Alternatively, approach using subqueries,

select course.name as course_name 
from courses as course 
where 500 < (
   select avg(book.price)
   from books as book
   where book.courseID = course.id 
)
````

for eg1: Write a query to display name and marks of all students, who have
scored the minimum marks out of all the students enrolled in the same
course as them.

````
select a.name as name, 
a.marks as marks
from students as a
where marks = (
  select min(marks)
  from students as b
  where a.courseId = b.courseId
)
````

#### CORRELATED SUBQUERY IN SELECT CLAUSE;;

-  We can also used the subqueries in the select clause

for eg7: Let's say we want to display the year of publishing of the oldest
   published book that belongs to each course, with the name of the course
   itself.

````
select courses.name as name,
min(books.publishedIn) as oldestBookPublishedIn
from course join books 
on course.id = books.courseId
group by courses.name

--- Alternatively, approach using subqueries,

select courses.name,
(
   SELECT MIN(publishedIn)
   FROM books
   WHERE books.courseId = courses.id
) AS oldestBookPublishedIn

FROM courses
````

#### CORRELATED SUBQUERIES WITH EXISTS

-  When you want to select data row from a table on the basis that whether
   there is at least one record existing with a certain condition related to
   the original table.

for eg8: Let's say we want to show names of students who are enrolled in
   courses that have at least 1 book that belong to them.
````
select name
from students
where 
course exists(
   select id
   from books as book
   where courseID = students.courseId
)
````

for eg9: Write a query to list the names of authors who have written at least
one book which was published either in 2010 or earlier. Set the header for the 
single column of results, to be name.

Note: Try doing it with EXISTS operator.

````
SELECT name 
FROM authors 
where exists(
  select id 
  from books
  where publishedIn <= 2010 and 
  authors.id = authorid
)
````

for eg10: Write a query to list the names of books for which the next volume was
   published within 1 year of their publishing year

````
SELECT a.name as name
FROM books as a
WHERE exists(
  select b.id as id
  from books as b
  where b.id = a.nextVolumeId and 
  b.publishedIn - a.publishedIn <= 1
)
````

####--- CORRELATED SUBQUERIES WITH NOT EXISTS;;

-  `NOT EXIST` case work opposite with respect to EXIST clause. 

-  It returns those 0 no of rows from the database on the basis of the
   constraints given.

for eg11: Write a query to list the names of courses that do not have a book
   published in 2014.

````
select course.name as name 
from courses as course 
where not exists(
  select id 
  from books
  where publishedin = 2014 and 
  courseid = course.id
)
````


-------------------------------------------------------------------------------------
###  Q019 : INTERSECT & EXCEPT in Sql;;

#### INTERSECT 

-  INTERSECT clause is used to fetch the common the data from the tables,
   which helps display common data of different types together, from results
   of two or more queries.

````
-  eg1: Write a query to display names which are common in the names of all
students and codeNames of all authors, under a single column.

SELECT name as name FROM students
INTERSECT
SELECT codename as name FROM authors
````

#### EXCEPT 

-  EXCEPT display all those records which are present in the first table
   records but not present in the second table records.

````
-  eg2: Write a query to display all the ids belonging to books, which are not
ids of any of the students

SELECT id
FROM books
EXCEPT
SELECT id
FROM students

-  eg3: Write a query to display names which are codeNames for authors, but not
names of any of the students. Set Header as uniqueCodeNames.

SELECT codeName as uniqueCodeNames
FROM authors 
EXCEPT
SELECT name as uniqueCodeNames
FROM students 
````


-------------------------------------------------------------------------------------
###  Q018 : UNION clause in Sql;;

#### UNION 

-  `UNION` is used to club the different data together in a single column.

````
eg1: UNION is used to merge queries data together.

SELECT name AS people
FROM students
UNION
SELECT name AS people
FROM authors
````

-  `UNION` must have the same number of columns from each query.

````
eg2: Column mismatch error in UNION

SELECT name, id FROM students
UNION
SELECT name FROM authors

-- output: 
SELECTs to the left and right of UNION do not have the same number 
of result columns
````

````
eg3: Write a query to display all the book names and all the course 
names, under a single column.

select name as academicData
from books
union
select name as academicData
from courses
````

````
eg4: Write a query to display the following under a single column:
 - Names of all students enrolled in the Java course
 - Names of all the books that belong to the Java course
 - Names of all authors who have written at least one book that belongs to Java

OUTPUT FORMAT :
-----------------------------------
|     type     |     javaData     |
-----------------------------------
|  Student     |     Joaquin      |
|  Books       |   Basic of Java  |
|  Student     |     Helen        |
|  Author      |    Mat Reeves    |
-----------------------------------

select 'Student' as type, 
student.name as 'javaData'
from students as student, courses as course
where student.courseid = course.id and 
course.name = 'Java'

UNION 
select 'Book' as type,
book.name as 'javaData'
from books as book, courses as course
where course.id = book.courseid and
course.name = 'Java'

UNION 
select 'Author' as type, 
author.name as 'javaData'
from books as book, authors as author, courses as course
where book.authorid = author.id and 
course.id = book.courseid and 
course.name = 'Java'
group by author.name 
having count(author.name) > 0
````

#### UNION ALL 

-  UNION is fetched all the unique rows or column from one or more tables.

for eg, 
````
# STUDENT TABLE COUNT: 25;;
AUTHORS TABLE COUNT: 25;;

select id from students 
union 
select id from authors
-- output : 25

NOTE: To overcom such scenario, we need all records from UNION;;

select id from students 
UNION ALL 
select id from authors 
-- output: 50
````

-------------------------------------------------------------------------------------
### Q017 : JOIN - CARTESIAN PRODUCT in Sql;;

#### CARTESIAN PROJECT WITH SIMPLE JOIN

-  Let's see what happens if we skip the ON clause from a simple JOIN query.

````
-- STUDENTS ROW: 25, COURES: 15
-- OUTPUT: 25*13 ~ 325 ROWS (~all possible combinations of table rows)

select student.name, course.name
from students as student
join courses as course
````

-  Let's rearrange the above possible combination and rendered a new
   columned, 'enrolled' if particular student is enrolled in that course.

````
SELECT students.name AS student,
courses.name AS course,
students.courseId = courses.id AS enrolled
FROM students 
JOIN courses

-  eg1: Write a query to display all the combinations of book names and author
names, and for each combination, display a boolean value (0/1) that shows
whether the book is written by the author.

select book.name as book,
author.name as author,
book.authorID = author.id as 'authored'
from books as book
join authors as author
````

#### CATESIAN PROJECT WITH SELF JOIN & FILTER

-  Let's say we want to select a panel of 2 authors, author1 and author2, out
   of all available authors and a1.id != a2.id 

````
/*
OBSERVATIONS:
author table rows : 10 
self join : 100 rows in total 
but adding filter a1.id <> a2.id 
reduces 10 rows.
TOTAL ROW NOW = 90
*/

SELECT a1.name AS author1,
a2.name AS author2
FROM authors a1 JOIN authors a2
WHERE a1.id <> a2.id

-  eg2: Let's say we want to select a panel of 2 authors, author1 and author2,
out of all available authors. There's one condition though, author1 must be a
female (gender 'F') and author2 must be a male (gender 'M'). Write a query to
get all combinations of names of author1 and author2.

SELECT a1.name as author1, 
a2.name as author2
FROM authors as a1
join authors as a2
WHERE a1.id <> a2.id and 
a1.gender == 'F' and
a2.gender == 'M'
````

-------------------------------------------------------------------------------------
### Q016 : JOIN Relationship in Sql;;

-  `JOIN` is used when you have two or more tables bind to each other using
   foreign key relationship.

-  `JOIN` Terminology,(https://www.w3schools.com/sql/sql_join.asp)
   1) JOIN == INNER JOIN
   2) LEFT JOIN == LEFT OUTER JOIN 
   3) RIGHT JOIN == RIGHT OUTER JOIN 
   4) FULL OUTER JOIN


#### INNER JOIN 

-  Examine below INNER Query,

````
SELECT students.name, courses.name 
FROM students 
JOIN courses ON
students.courseId = courses.id
````

- SELECT Keyword: Specifies the list of columns
- FROM Keyword: Consists of the list of tables the columns are being picked
  from, separated by the word JOIN
- ON Keyword: It is used to express the columns from each table which should
  be matched together to connect the data amongst them
- CONSTRAINT Keyword: The column courseId in students stores the reference to
  the courses students are enrolled in. Hence, the clause, ON
  students.courseId = courses.id 

````
-  eg1: Write a query to display the name and age of all students who are
enrolled in a course, along with the name and the abbreviated name of the
courses.

SELECT a.name as studentName, 
a.age as age, 
b.name as courseName, 
b.abbreviatedname as courseAbbreviatedName
FROM students as a
INNER JOIN courses as b
ON a.courseId = b.id 
````


#### LEFT OUTER JOIN 

-  `OUTER JOIN` is a `JOIN` that also returns records that are unmatched from the
   criteria in ON clause, along with the ones that match.

-  `LEFT OUTER JOIN` or a `LEFT JOIN` returns records from the table at left in
   the JOIN, that are unmatched from the connecting query in ON, along with
   the matched records.

````
-  eg2: Write a query to display the id and name of all students, along with the
name of the course they are enrolled in, if its a valid course.

select stud.id as studentId,
stud.name as studentName,
course.name as courseName
FROM students as stud
left outer join courses as course
ON stud.courseId = course.id
````

#### SELF JOIN 

-  `SELF JOIN` is used to crawl the data from the same table.

````
-  eg3: The table books contains a column nextVolumeId. It stores the id of
another book which is the next volume of the book in that row.

Write a query to display the name of all the books which have a next volume,
along with the name of the book which is the next volume for each of them

select a.name as book, 
b.name as nextVolume
from books as a
join books as b
on a.nextvolumeid = b.id


-  eg4: Write a query to display the name of all the students, along with the
name of the student who is their student mentor. For students who don't have
a student mentor, leave that column in the result blank.

select a.name as studentName, 
b.name as mentorName
from students a
left join students b
on a.studentmentorid = b.id
````


####- JOINING MORE THAN 2 TABLES

-  We can join two or more tables using JOINS.

````
-  eg5: 
 
select publisherName, 
books.name as book,
courses.name AS course,
authors.name AS author
from books 
join courses, authors
ON books.courseId = courses.id AND
books.authorId = authors.id
````

#### JOIN WITH FILTER 

-  WHERE claue can be used to add inside the JOIN query like an ordinary sql
   query to render multiple table data.

for eg,
````
SELECT students.name AS studentName,
courses.name AS courseName, marks
FROM students 
JOIN courses
ON students.courseId = courses.id
WHERE courses.name IN ('JavaScript', 'Python') AND
marks BETWEEN 15 AND 85;
````

#### JOIN WITH ORDER

-  ORDER claue can be also used to order data final table in ascending or
   descending order.

for eg,

````
SELECT students.name AS studentName,
courses.name AS courseName, marks
FROM students 
JOIN courses
ON students.courseId = courses.id
ORDER BY courses.name, marks
````

#### JOIN WITH GROUP BY

-  GROUP BY clause can be used simply like ordinary query.

````
eg1: Write a query to display the names of all authors and the number of books
authored by them.

/*
-- A LEFT JOIN B: Here A: AUTHOR, B: BOOK 
-- Query will return all the author who have or have not 
-- published any book. 
*/

select author.name as author, 
count(book.name) as books
from authors as author 
left join books as book
on book.authorID = author.id 
group by author

-  eg2: Write a query to display the names of all courses followed by these 4
data items:
   - maximum marks scored by students in the course
   - minimum marks scored by students in the course
   - sum of all marks scored by students in the course
   - average of marks scored by students in the course

/*
LEFT JOIN is used because we want those course too, in which marks is not 
scored or those course whose exam not conducted till now.
*/
select course.name as courseName, 
max(marks) as maximumMarks, 
min(marks) as minimumMarks, 
sum(marks) as sumOfMarks, 
avg(marks) as averageMarks
from courses as course
left join students as student
on student.courseid = course.id 
group by course.name


-  eg3: Write SQL query to get the count of students in each unique combination
of a course and a grade.

Note: Skip combinations which have 0 results. So if there is no student in
grade 5 who is enrolled in Java, don't include this combination in the final
results.

select course.name as name, 
student.grade grade, 
count(student.name) as studentsCount
from students as student
join courses as course 
on student.courseid = course.id
group by course.name, student.grade
order by course.name, student.grade desc


-  eg4: Write an SQL query to display the name of all unique male authors
(gender equals M) who have written 3 or more books, with the number of books
authored for each of them.

select author.name author, 
count(1) as booksAuthored
from authors as author
join books as book
on book.authorID = author.id 
where author.gender = 'M'
group by author.name
having count(1) >= 3


-  eg 5: Write an SQL query to display the name of all unique courses, and 
count of books that belong to that course. The names of courses should be in
alphabetical order.

select course.name as course, 
count(1) as books
from courses as course
join books as book
on book.courseID = course.id 
group by course.name
order by course.name
````

#### GROUP BY MULITPLE JOINED TABLES 

````
-  eg6: Write a query to display the names of all students who are enrolled in a
valid course that has at least one book that belongs to it, and the year of
publishing of the oldest book that belongs to the course the student is
enrolled in, for each student

At the end, make sure that the results are sorted in

   - the ascending order of oldestPublishingYear, and
   - the alphabetical order of students' name.

select student.name as student, book.publishedIn as oldestPublishingYear
from students as student
join courses as course
on student.courseid = course.id 
join books as book
on book.courseID = course.id
group by student.name
order by book.publishedIn, student.name  
````


-------------------------------------------------------------------------------------
### Q015 : GROUP_CONCAT in Sql;;

**(NOTE: GROUP_CONCAT applicable for MySql, Sqllite3)**

-  Let's say we want to display the names of all unique not-null courses. For
   each of these courses names display names of all students enrolled in the
   course. Separate the names of students using a comma.
-  SQL provides GROUP_CONCAT, a combination clause over GROUP BY.
-  Delmiter can be anything in the GROUP CONCAT function default is comma and
   other like pipe(|), Dash(-), Underscore(_), Hashtag(#) etc.
-  GROUP_CONCAT(column_name, 'delimiter')
-  for an instance,

````
# Data with Group By Only 

select course, name, count(*)
from students 
where course is not null 
group by course, name

-- RESULT DATA 
 _________________________________________
|  python | (first student)  | 1 (~count) |
|  python | (second student) | 1 (~count) |
|  Java   | (third student)  | 1 (~count) |
 -----------------------------------------

# WITH GROUP CONCAT (SQL Applicable Only) 

select course, group_concat(name), count(*)
from students 
where course is not null
group by course

-- RESULT DATA
 ________________________________________________________
| python  | (first student, second student) | 2 (~count) |
| Java 	  | (third student) 				| 1 (~count) |
---------------------------------------------------------	

-  eg1: Write a query to list all the unique not-null grades. For each of these
grades, display all the courses, students of that grade are enrolled in.
Separate the list of courses using a single space ( ). Set the headers for
grades and list of courses as grade and courses respectively.

SELECT grade, group_concat(course, ' ') as courses
FROM students
WHERE grade is not null and course is not null
GROUP BY grade
````
**(NOTE: Postgres use another function named array_agg())** 
````
Note: string_agg() is also other alternative but not working for postgres.

Suppose you have data like this,

 ----------------------------------------------
| id  | user_name |    mobile_no  | is_active  |
|  1  |  neeraj   |   1234512340  |   true     |
|  2  |   ram     |   1234512341  |   true     |
|  3  |   siya    |   1234512342  |   false    |
 ----------------------------------------------
 
Now, the requirement is to fetch  mobile_no and name
of all the active use in a single row.

SELECT 
is_active, 
array_agg(mobile_no, '|'),
array_agg(user_name, '|'), 
count(1)
FROM users
GROUP BY is_active

-- RESULT DATA
 ______________________________________________________________________
| true  | ["1234512340", "1234512341"] | ["neeraj", "ram", "sita"] | 3 |
 ----------------------------------------------------------------------	
````


-------------------------------------------------------------------------------------
### Q014 : COUNT(*) vs COUNT(1) in Sql;;

(~ Future : https://learnsql.com/blog/difference-between-count-distinct)

#### COUNT(*)
-  The COUNT(*) returns the total number of rows in a table, including the
   NULLs. 

#### COUNT(1) 
-  The COUNT(1) function map all records from the query result set with
   value 1. If you have NULL values, it is also map by 1. Therefore,
   COUNT(1) also returns the total number of records (including NULLs) in the
   table.

-  Similarly, If you used count(2), count(3), count(1000), count(-100) all will
   have the same result No different.

-  Even if you use the string in the count() function the final result will be
   the same as for count(*).

#### COUNT(COLUMN_NAME)
-  If we specify a column name in the SQL COUNT function argument, it counts
   the total number of rows in the table and excludes the NULL in the
   specified column. 

#### COUNT(DISTINCT COLUMN_NAME)
-  It will count the normal distinct value count only. As what the distinct
   keyword do.

#### FALSE MISCONCEPTION 
-  There’s a popular misconception that “1” in COUNT(1) means “count the
   values in the first column and return the number of rows.” From that
   misconception follows a second: that COUNT(1) is faster because it will
   count only the first column, while COUNT(*)

#### CONCLUSION
````
-  COUNT(*) returns counts of all the rows, including NULLs
-  COUNT(1) returns counts of all the rows, including NULLs
-  COUNT(column_name) counts of all the rows, excluding NULLs.
````


-------------------------------------------------------------------------------------
### Q013 : COUNT & GROUP BY in Sql;;

-  `COUNT`: It is used to count the number of rows in table.
-  `GROUP BY`: When we count rows then we have to group the rows with respects
   to the column for which you want the count.

````
-  eg1: Count the number of students enrolled in all course and course is not null.

select course, count(*) NoOfStudents
from students
where course is not null
group by course

-  eg2: Find all grades and the maximum age of students in each grade. The column
header for "maximum age" should be maxAge.

SELECT grade, max(age) as maxAge
FROM students
where grade is not null
group by grade

-  eg3 : Find all the distinct courses and the minimum marks students have scored
in each course. The column header for "minimum marks" should be minMarks.

SELECT course, min(marks) as minMarks
FROM students
where course is not null
group by course

-  eg4 : Find all distinct courses and the total sum of all marks students have
scored in each course. The column header for "sum of marks" should be
sumOfMarks.

SELECT course, sum(marks) as sumOfMarks
FROM students
where course is not null 
group by course

-  eg5: Find all distinct grades and the average of all marks students have
scored in each grade. The column header for "average of all marks" should be
avgOfMarks.

select grade, avg(marks)
from students
where grade is not null
group by grade
````

#### GROUP BY Modified Column Data 
-  We can apply group by on non-exisiting table column or one which is
   rendered by the sql query builder.

````
-  eg6: We want to count the number of students for unique length of names.

SELECT LENGTH(name) AS nameLength, 
COUNT(*) AS countOfStudents
FROM students
GROUP BY LENGTH(name)

-  eg7: Write a query which shows the number of students who have got marks in
single digits (0-9) and the number of students who got marks in double
digits (10-99).

select length(marks) as digitsInMarks, 
count(*) as noOfStudents
from students
group by length(marks)
````

#### GROUP BY with ORDERING (ORDER BY);;

````
-  eg8: Write Query to fetch no. of students in each grade and sort the no. of
students in descending order.

select grade, count(*) as studentsCount
from students
where grade is not null
group by grade
order by count(*) desc

-  eg9: Write a query to list all unique not-null courses and the maximum marks
obtained in each of them as "maxMarks" by the students in ascending order

select course, max(marks) as maxMarks
from students
where course is not null 
group by course
order by marks asc
````

#### GROUP BY with FILTER (HAVING)

-  `HAVING clause` is used with the group by clause when there is a need to add
   filteration among the grouped data.

```
-  eg10: Write a SQL query to list only unique not-null courses having average
marks obtained in each them between 30 and 69, along with the average marks
obtained in each of them as avgMarks, sorted in the descending order of the
avgMarks scored in them.

select course, avg(marks) as avgMarks
from students
where course is not null
group by course
having avg(marks) between 30 and 69
order by avg(marks) desc

-  eg11: List all no. of students in every course having student count geater
than 2.

select grade, count(*) as noOfStudents
from students
where grade is not null
group by grade
having count(1) > 2
```

####--- GROUP BY with MULTIPLE COLUMNS

-  When you are fetching only one column (excluding dynamically rendered
   column) then everything works fine. But things gets messy as soon as you
   include more than two columns in single group by. To overcome such things,
   you 've to include multiple columns in the single group by clause.

**(NOTE: GROUP BY Clause you can also group an alias column or a column 
that you have been rendered dynamically on the basis of a logic)**

````
-  eg12: List of all the PASSED & FAILED students in every grade. Students
having marks greater than 33 will be considered as PASSED or else FAILED.

select grade, count(*) as CountOfStudents,
case when marks > 33 then 'PASSED' else 'FAILED' end as status
from students
where grade is not null
group by grade, status
````


-------------------------------------------------------------------------------------
### Q012 : COALESCE vs IFNULL in Sql;;

-  COALESCE is useful when you have unknown number of values that you want to
   check and IFNULL is useful when you select columns and know that it can be
   null but you want to represent it with a different value.
-  COALESCE function can take two or more parameters and returns the first
   non-NULL parameter, or NULL and IFNULL function takes two arguments and
   returns the first one if it's not NULL or the second if the first one is
   NULL.

````
-  eg1, Difference of COALESCE Vs IFNULL

SELECT IFNULL('some value', 'some other value');
-- returns 'some value'

SELECT IFNULL(NULL,'some other value');
-- returns 'some other value'

SELECT COALESCE(NULL, 'some other value');
-- returns 'some other value' - equivalent of the IFNULL function

SELECT COALESCE(NULL, 'some value', 'some other value');
-- returns 'some value'

SELECT COALESCE(NULL, NULL, NULL, NULL, 'first non-null value');
-- returns 'first non-null value'
````


-------------------------------------------------------------------------------------
### Q011 : COALESCE Clause in Sql;;

- `COALESCE` function is used to select first not-null value in the list of inputs.

````
for eg, Let's say we want to display the name of all students with one additional
data point. If age is available, then print it. If age is not available, then
we print the grade value. If the grade is also NULL, then we print the course
value. If the course value is NULL as well, we return NULL

SELECT name, 
coalesce(age, grade, course) AS "age or grade or course"
FROM students
````


-------------------------------------------------------------------------------------
### Q010 : IFNULL Clause in Sql;;

-  `IFNULL` is simply to implement a check of a value being NULL 
-  `IFNULL` accepts 2 arguments. 
	1) The first argument is the column that needs to be picked
	2) Fallback value if the first column is set to null.

````
-  eg1: Select all grade and print no grade if grade is null

select name, ifnull(grade, 'no other')
from students

or, we can also do it with the case statement. Like

select name, 
case 
	when grade is not null then grade
else
	'no grade'
from students
````


-------------------------------------------------------------------------------------
### Q009 : Concatenation in Sql;;

-  We use `||` operator to concatenate data from different columns 

````
-  eg1: Display name and email in a single column

select name||','||email as contacts
from students
````


-------------------------------------------------------------------------------------
### Q008 : Case Clause in Sql;;

- Case in sql is used for the implementation of the if-else block in
  programming language.

- Syntax:  
````
  case 
    when something = True 
    then 'this happens' 
  else 'This one' 
  end 
````

Note that the way conditional expressions in SQL are written, differs from
database to database. 

> Sqlite3 used the conditional operator CASE and Portgres also used the same 
> But MySql have different syntax. Like,

#### MYSQL SYNTAX : 

````
select name, 
if(course in ('Python', 'Ruby'), 
	'Then This will Execute', 
	'Otherwise this will work')
from students

-  eg1 : Display students result and the value of "result" should be be "passed"
if marks is greater than 33. Otherwise "failed".

SELECT name, marks, 
case when marks > 33 then 'passed' else 'failed' end as result
FROM students
````

-------------------------------------------------------------------------------------
### Q007 : Modify Data from Rows in Sql;;

-  You can add boolean clauses in select statements

````
-  eg1: Display name and age of students along with the information whether they
are a teenager or not.

SELECT name, age, (age BETWEEN 13 AND 19) AS isTeenager
FROM students

-  eg2 : Let's say that a student is considered underage if the difference
between the age and the grade is 5 or less.

SELECT name, age, grade, (age-grade <= 5) as isUnderage
FROM students
````

-------------------------------------------------------------------------------------
### Q006 : Arithmetic Operation in Sql;;

Arithmetic operations like addition, subtraction, multiplication, division
and modulo can be applied on an individual column.

````
-  eg1: Show arithmetic operatoin

SELECT age / 2, age * 2
FROM students

-  eg2: Display the length of name of students incremented by 1 and marks of
students rounded to nearest multiple of 10 less than or equal to marks

SELECT 
length(name) + 1 as incremented_length, 
marks-marks%10 as rounded_marks
FROM students

-  eg3: List the names, ages and marks of students where the sum of age and marks
is between 30 and 70.

select name, age, marks
from students
where (age + marks) between 30 and 70

-  eg4: Display the name, age and marks of students whose age is an even number
and marks are an odd number.

SELECT name, age , marks
FROM students
where age % 2 = 0 and marks % 2 <> 0

-  eg5: Display the name, age and grade of students in the ascending order of
difference of their age and grade for students who have both age data and
grade data.
````


-------------------------------------------------------------------------------------
### Q005 : Modulus in Sql;;

-  SQL can perform arithmetic operations like addition, subtraction, division
   or modulus.
-  Modulus is the remainder of a division between two numbers. It is
   represented by the symbol %.

````
-  eg1: show modulo between 10 and 3

select 10 % 3;
-- output : 1

-  eg2: Find all students having ids even

select * from students where id % 2 = 0;
````


-------------------------------------------------------------------------------------
### Q004 : Strftime function in sql;;

-  `STRFTIME` is a SQL function that can be used over DATETIME to extract
   specific information.
-  Here are a few basic parameters used for date extractions. Like,
	- %d ~ day of month: 00
	- %m ~ month: 01-12
	- %Y ~ year: 2023
	- %H ~ hour: 00-24
	- %M ~ minutes: 00-60
	- %S ~ seconds: 00-60
	- %f ~ fractional seconds: SS.SSS ~ 59.001
	- %j ~ day of the year: 001- 366
	- %J ~ julian day number
	- %s ~ seconds since 1970-01-01
	- %w ~ day of week :0 to 6 with 0 -  Sunday
	- %W ~ week of year: 00-53

```
-  eg1, Print month of the current date

SELECT STRFTIME('%m', DATETIME('Now'))

-  eg2, Format the whole date

select strftime('%Y-%m-%d %H:%M:%S', datetime('now'))

-  eg 3, Write a query to display the datetime timestamps
1) for time exactly 4 days after the current time in UTC
2) time at the b-  eginning of the current day in UTC 

SELECT 
strftime('%d/%m/%Y %H:%M', datetime('now', '+4 days')) as time4DaysLater,
strftime('%d/%m/%Y %H:%M', datetime('now', 'start of day')) 
as timeCurrentDayStart

-- time4dayslater : 04/06/2023 15:42
-- timecurrentdaystart : 31/05/2023 00:00
```


-------------------------------------------------------------------------------------
### Q003 : Date and Time function in sql;;

#### Date 
- `Date` function is used to display the date of today.

````
-  eg 1 : Let's use the DATE function to display today's date along 
with the name and course of all students.

SELECT DATE('Now')
-- output: 2023-05-31
````

#### Time 
-  `Time()` function is used to display the time in current instances;

````
-  eg2 : Dispaly time in sql query
select time('now')
````

#### DateTime() function
-  The DATETIME function combines the features of both DATE and TIME
   functions. It displays both date and time together.
-  The time shown by DATETIME is UTC time by default. If we want to display
   the local time, we can add a parameter 'localtime' to the DATETIME
   function .
-  There are modifiers like 
     1) 'start of day'
     2) 'start of month'
     3) 'start of year'
     4) '+2 days'
     5) '-2 days'
     6) '+2 months'
     7) '+2 months'
 
````
eg3: Display localtime

SELECT DATETIME('NOW', 'localtime')
````

#### DateTime() Modifiers 
We can also add or subtract date time from current date time.

```
-  eg4: For adding 2 days in current datetime

select datetime('now', '+2 days')
-- 2023-06-02 14:57:21

and, this modifier also work with date() function

-  eg4.1: For adding two days with date() function 

select date('now', '+2 days')
-- 2023-06-02

-  eg 4.2: for subtracting 2 months from the current date

select datetime('now', '-2 days')

and with date() function

select date('now', '-2 days ')

-  eg 4.3: for subtracting 2 months from the current date

select datetime('now', '-2 months')
-- 2023-03-31 15:02:28

and, similarly with date() function 

select date('now', '-2 months')
-- 2023-03-31

-  eg 4.4: for datetime timestamp of +3 years to the current localtime

select datetime('now', 'localtime', '3 years')
-- UTC TIME + 3year

and, if you want 

-  eg 4.5: some other modifiers are

SELECT DATETIME('now', 'localtime', 'Start of Day');

SELECT DATETIME('now', 'localtime', 'Start of Month');

SELECT DATETIME('now', 'localtime', 'Start of Year');
```


-------------------------------------------------------------------------------------
### Q002 : Sql Length function;;

- SQL has a LENGTH function which can be used for counting the length of
  string, number etc.
- LENGTH can also be used on number or integer columns in addition to string
  columns.
- We can use LENGTH in ORDER BY clause to get this result.

````
-  eg 1 : Let's say we want to select the length of the names of students along
with their names.
 
SELECT name, LENGTH(name)
FROM students

-  eg 2 : Find unique course names which are of length 4.

SELECT DISTINCT course
FROM students
WHERE LENGTH(course) = 4

-  eg 3 : List the names of students in the ascending order of length of their
names.

select name 
from students 
order by length(name) asc
````

-------------------------------------------------------------------------------------
### Q001 : Sql Core  Fundamentals Topics;;

####  Select 
SELECT to select all the columns and all the data from the table.

for eg,
```` 
select * 
from students;
````

#### Where
WHERE is used to filterout data from the table.

for eg,
````
select * 
from student 
where couse = 'English'
````

####  Not
We can use not equal to operator != to get the job done.

for eg,
````
SELECT * 
FROM students 
WHERE age != 12
````

#### Less Than
We can use < to perform a less than operation.

for eg,
````
SELECT * 
FROM students 
WHERE grade < 8
````

#### Greater Than
We can use > to perform a greater than operation.

for eg,
````
SELECT * 
FROM students 
WHERE age > 13
````

#### Less Than Equals to 
We can use <= to perform a less than or equal to operation.

for eg,
````
SELECT * 
FROM students 
WHERE age <= 7
````

#### Greater Than Equals to 
We can use >= to perform a greater than or equal to operation.

for eg,
````
SELECT *
FROM students
WHERE grade >= 9
````

#### Sql Comments
We can use comments in SQL too to mark part of code not to be run.

for eg,
````
SELECT *
FROM students
-- WHERE grade < 8
````

#### Multiple Line Comments
Let's say we have a query to get all students whose grade is less than 8.

for eg,
````
/* 
Multi-Line Comment in Sql Language !!!
*/

SELECT *
FROM students
WHERE age < 13
````

#### AND Operation
We can use AND operator to combine the two conditions.

for eg,
````
SELECT *
FROM students
WHERE age > 10
AND course = 'JavaScript'
````

#### OR Operation
We can use OR operator to combine the three conditions. If one of the
conditions is true then that record will be selected since we are using OR
operator.

for eg,
````
SELECT *
FROM students
WHERE age > 15
OR course = 'Java'
OR grade = 7
````

#### Both AND & OR
We need to use both AND as well as OR to solve this problem.

for eg, 
````
Find all students who are of age 15 or of age 13 or of age 12 and belong
to a grade lesser than 9.

SELECT *
FROM students 
where (grade < 9) and
(age = 15 or age = 13 or age = 12)
````

#### Between 
One way of doing this would be using OR.

for eg, 
````
Find all students who are of age between 12 and 15.

SELECT *
FROM students
WHERE age BETWEEN 12 and 15
````

#### Between and Other Condition
We can use BETWEEN & AND condition to solve this.

for eg, 
````
Find all students who belong to grades between 8 and 12 and they are
enrolled in course C#.

SELECT *
FROM students
WHERE (course = 'C#') and 
(grade BETWEEN 8 and 12)
````

#### Not Between 
One way of doing this would be using WHERE in combination with less than and
greater than operators.

for eg, 
````
Find all students who don't have marks between 30 and 70.

select *
from students
where marks NOT BETWEEN 30 AND 70;

alternatively , 

select * 
from students
where not marks between 30 and 70;
````

#### IN 
In operator is used to find values from a list of collections

for eg, 
````
Find all student having grades 6,9,12

SELECT *
FROM students
WHERE grade IN (6, 9, 12)
````

#### NOT IN 
NOT In is just used to find the opposite of IN collections.

for eg,
````
Find those grade not in (2, 3, 5, 7, 11)

SELECT *
FROM students
WHERE grade  NOT IN (2, 3, 5, 7, 11)

alternative,

SELECT *
FROM students
WHERE NOT grade IN (2, 3, 5, 7, 11)
````

#### Null 
In database we represent missing information as NULL.

for eg, 
````
Find all students whose age information is not available.

SELECT *
FROM students
WHERE age IS NULL

Find those student age is missing or course is missing

select *
from students 
where age is null or course is null 
````

#### NOT Null
Find all information who row is not missing.

for eg, 
````
Find all students whose grade information is available.

SELECT *
FROM students
WHERE grade IS NOT NULL
````

#### Like 
We can use % with LIKE to solve this find any string pattern

for eg, 
````
Find all students who are enrolled in a course that starts with P.

SELECT  *
FROM students 
where course like 'P%';
````

#### NOT Like
We can use % with NOT LIKE to solve this.

for eg, 
````
Find all students who are enrolled in a course that does not start with  Ja.

SELECT *
FROM students
WHERE course NOT LIKE 'Ja%'
````

#### DISTINCT
Distinct is used to fetch the unique record from a row.

for eg, Find all the unique age of all the students.
````
SELECT distinct age
FROM students;
````

#### COUNT
The count function is used to count the number of rows.

An aggregate function is used to perform some calculations on data. Count, 
average, sum, maximum and minimum are examples of aggr-  egate function.

for eg, 
````
Let's find the total number of students.

select count(*) from students

alternatively, both query are same 

select count(all name) from students
````

#### AS
`AS` is used to change the header of the column.

for eg, 
````
Let's display only the id, grade and course of students. The column 
name for ids should be studentId and the column name for grades should be
studentGrade.

SELECT
id as studentId,
grade as studentGrade,
course
FROM students;
````

#### COUNT with DISTINCT
count distinct give distinct count of all the rows of the database.

for eg, 
````
find all distinct courses.

SELECT DISTINCT(course)
FROM students
````

#### SUM and AVG
- `Sum` : `Sum` aggr-  egate sums up all the values from the result

for eg, 
````
Find the sum of all distinct marks under 50 and name it
sumOfDistinctMarks.

SELECT sum(distinct marks) as sumOfDistinctMarks
FROM students
where marks < 50;
````

- `Avg` : `Avg` aggregate average of all the marks. 

for eg, 
````
Find the average of all the marks. AVG can be used to solve this.

SELECT AVG(marks)
FROM students
````

#### MAX and MIN
-  Max : Max returns the maximum of all the not-null values in the column
   mentioned next to it.

for eg, 
````
Calculate the maximum marks among all the students who are enrolled in the
Python course.

select max(marks)
from students
where course = 'Python'
````

-  Min : Min returns the Minimum of all the not-null values in the column
   mentioned next to it.

for eg, 
````
calculate the minimum age.

SELECT min(age)
FROM students
````

#### Select Multiple Data
We can select multiple columns and perform some mathematical operation on
these columns. Suppose, we want to get the total age of all the students and
the maximum marks in the same query.

for eg, 
````
Let's calculate the minimum marks, the maximum marks and the count of
distinct courses and name them as minMarks, maxMarks and countOfCourses
respectively.

SELECT min(marks) as minMarks,
max(marks) as maxMarks,
count(distinct course) as countOfCourses
FROM students
````

#### ORDER BY
order by is used to order the result row in ascending or descending pattern.

````
-  eg1,
Find name, grade, and age of all students, sorted in increasing order of their age.

SELECT name, grade, age
FROM students 
order by age asc

-  eg2,
Find name, grade, age, and marks of students, in the increasing order of grade
first, then age and then marks.

SELECT name, grade, age, marks
FROM students
order by grade, age, marks

-  eg3, Find name, marks and age of all students, and order them by age in
ascending order first and then sort them in descending order of marks.

SELECT name, marks, age
FROM students
ORDER BY age ASC, marks DESC
````

#### LIMIT
Limit is used to select specific number of rows from the results 

````
-  eg4,
Select 6 students above age 9

SELECT  *
FROM students
where age > 9
limit 6;
````

#### OFFSET
SQL provides OFFSET which sets the starting position. When we use LIMIT then
we take a number of records from the top. It means starting position is 0.

for eg,
````
Let's say that we want to find students who are at position 6, position 7,
position 8, position 9 and position 10. You have to skip the first 5 position
of the customer

select *
from students 
limit 5
offset 5
````

-------------------------------------------------------------------------------------