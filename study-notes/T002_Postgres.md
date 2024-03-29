````
-------------------------------------------------------------------------------------
-> Title: Postgres Diary
-> Author: @neeraj-singh-jr
-> Status: Ongoing...
-> Created: 15.10.2022
-> Updated: 15.10.2022
-> Summary: Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> P003 : Postgresql - Select
-> P002 : Connect to the PostgreSQL database server via psql
-> P001 : What is PostgreSQL
-------------------------------------------------------------------------------------
````

### PostgreSQL NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### P003 : Postgresql - Select

The SELECT statement is one of the most complex statements in PostgreSQL. It
has many clauses that you can use to form a flexible query.

The SELECT statement has the following clauses:

- Select distinct rows using DISTINCT operator.
- Sort rows using ORDER BY clause.
- Filter rows using WHERE clause.
- Select a subset of rows from a table using LIMIT or FETCH clause.
- Group rows into groups using GROUP BY clause.
- Filter groups using HAVING clause.
- Join with other tables using joins such as INNER JOIN, LEFT JOIN, 
FULL OUTER JOIN, CROSS JOIN clauses.
- Perform set operations using UNION, INTERSECT, and EXCEPT.

-------------------------------------------------------------------------------------
### P002 : Connect to the PostgreSQL database server via psql

Connect to PostgreSQL using the postgres role, you switch over to the
postgres account on your server by typing:

> $ sudo -i -u postgres

Then, you can access the PostgreSQL using the psql by typing the following
command:

> $ psql

You’ll access the postgres prompt like this:

> postgres=#

To quit the PostgreSQL prompt, you run the following command:

> postgres=# \q

This above command will bring you back to the postgres Linux command prompt.

> postgres@ubuntu-dev:~$

To return to your regular system user, you execute the exit command like
this:

> postgres@ubuntu-dev:~$ exit

#### Load the sample database

First, switch over the postgres account using the following command:

> $ sudo -i -u postgres

Second, download the sample database using the curl tool:

> $ curl -O https://sp.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip

Third, unzip the dvdrental.zip file to get the dvdrental.tar file:

> $ unzip dvdrental.zip

Fourth, access the PostgreSQL using the psql tool:

> $ psql

Fifth, create the dvdrental database using the CREATE DATABASE statement:

> postgres=# create database dvdrental;

Code language: Shell Session (shell)
Sixth, quit the psql by using the \q command:

> postgres=# \q

Code language: Shell Session (shell)
Seventh, use the pg_restore tool to restore the dvdrental database:

> $ pg_restore --dbname=dvdrental --verbose dvdrental.tar

Code language: Shell Session (shell)
Eighth, access PostgreSQL database server again using psql:

> $ psql

Code language: Shell Session (shell)
Ninth, switch to the dvdental database:

> postgres=# \c dvdrental

Code language: Shell Session (shell)
Now, you’re connected to the dvdrental database:

> dvdrental=#

Code language: Shell Session (shell)
Finally, enter the following command to get the number of films in the film table:

> dvdrental=# select count(*) from film;

````
Code language: Shell Session (shell)
Here is the output

count
-------
1000
(1 row)
Code language: Shell Session (shell)
Congratulations! you have successfully installed PostgreSQL on Ubuntu, connect 
to PostgreSQL database server using psql, and load the sample database.
````

-------------------------------------------------------------------------------------
### P001 : What is PostgreSQL;;

PostgreSQL is an advanced, enterprise-class, and open-source relational database 
system. PostgreSQL supports both SQL (relational) and JSON (non-relational) 
querying.

PostgreSQL is a highly stable database backed by more than 20 years of
development by the open-source community.

#### Common use case of PostgreSQL

1) A robust database in the LAPP stack : LAPP stands for Linux, Apache,
PostgreSQL, and PHP (or Python and Perl). PostgreSQL is primarily used as a
robust back-end database that powers many dynamic websites and web
applications.

2) General purpose transaction database : Large corporations and startups
alike use PostgreSQL as primary databases to support their applications and
products.

3) Geospatial database : PostgreSQL with the PostGIS extension supports
geospatial databases for geographic information systems (GIS).

#### Language supports

Python, Java, Php, C/C++, C#, Go, Perl.

#### PostgreSQL feature highlights

- Asynchronous replication
- Multi-version concurrency control (MVCC)
- Nested transactions (savepoints)
- Sophisticated locking mechanism

-------------------------------------------------------------------------------------
