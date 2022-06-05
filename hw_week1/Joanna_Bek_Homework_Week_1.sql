
-- ------------------------------- TASK 1 ------------------------------------------

Use parts;

-- TASK 1.1
SELECT 
	p.pname, p.weight
FROM 
	part p
WHERE 
	p.weight > 14;

-- Comment: Nice! Very minor but the select was supposed to return only the name, not a problem here but could be in big queries.
-- 4/5

-- TASK 1.2
SELECT DISTINCT 
	sr.sname, sr.status
FROM 
	supplier sr
WHERE 
	sr.status = 20;

-- Comment: Nicely done! Same as above with status, but very minor (nit picking really).
-- 4/5

-- ------------------------------- TASK 2 ------------------------------------------

USE shop;

-- TASK 2.1
SELECT 
	s.Week, s.Day, s.SalesAmount
FROM 
	sales1 s
ORDER BY 
	s.Week;

-- Comment: You've got what you need but just consider what you'd
-- do if there were multiple rows for the same day/week, what would 
-- you change? (no need to reply by the way)
-- 4/5

-- TASK 2.2
UPDATE 
	sales1 s
SET 
	s.SalesPerson = 'Anette'
WHERE 
	s.SalesPerson = 'Inga' AND s.SalesAmount < 50;
    
SELECT s.SalesPerson, s.SalesAmount from sales1 s;

-- Comment: Nicely done! Perfect
-- 5/5

-- TASK 2.3
SELECT 
	count(s.store) as sales_logged_in_London
FROM 
	sales1 s
WHERE 
	s.Store = 'London';

-- Comment: Nice aliasing for the column name too!
-- 5/5

-- TASK 2.4
SELECT 
	s.SalesPerson, s.Day, sum(s.SalesAmount) as TotalSales
FROM 
	sales1 s 
GROUP BY 
	s.SalesPerson, s.Day
ORDER BY 
	s.SalesPerson;

-- Comment: Brilliant! Getting tougher now!
-- 5/5

-- -- TASK 2.5
SELECT 
	s.SalesPerson, sum(s.SalesAmount) as TotalSales
FROM 
	sales1 s 
WHERE 
	s.Week BETWEEN 1 AND 3
GROUP BY 
	s.SalesPerson;

-- Comment: Nicely done again! You're getting the knack of these now! :)
-- 5/5

-- TASK 2.6
SELECT 
	s.Store, sum(s.SalesAmount) as TotalSales, count(s.SalesAmount) as SalesLoggedInStore, 
    avg(s.SalesAmount) as AverageSales, min(s.SalesAmount) as LowestSales, max(s.SalesAmount) as HigestSales
FROM 
	sales1 s 
GROUP BY 
	s.Store;

-- Comment: Lovely complex query. Perfect.
-- 5/5

-- TASK 2.7
SELECT 
	s.Store, avg(s.SalesAmount) as AverageSales
FROM
	sales1 s 
GROUP BY
	s.Store;

-- Comment: Nice! Good use of a built in function there too.
-- 5/5

-- TASK 2.8
SELECT 
	s.SalesPerson, count(s.SalesPerson) as NumberOfSales
FROM
	sales1 s 
GROUP BY s.SalesPerson
HAVING NumberOfSales < 3;

-- Comment: Nice use of HAVING here. I don't often use it but this is a nice 
-- use case.
-- 5/5

-- TASK 2.9
USE shop;
SELECT
	s.SalesPerson, count(s.SalesPerson) as NumberOfSales, sum(s.SalesAmount) as TotalSales
FROM
	sales1 s
GROUP BY
	s.SalesPerson
HAVING sum(s.SalesAmount) <= 300;

-- Comment: Smashed it, again! Just be careful about selecting extranious columns.
-- It's definitely worth keeping during development of a query and it's good
-- practice to remove it when you're done.
-- 4/5

-- ------------------------------- TASK 3 ------------------------------------------

Use Parts;

-- Task 3.1
SELECT distinct
	part.P_ID, part.Colour, supplier.SNAME
FROM 
	part 
INNER JOIN supply ON supply.P_ID = part.P_ID
INNER JOIN supplier ON supplier.S_ID = supply.S_ID
WHERE supplier.SNAME LIKE '%s' and supplier.CITY != 'London';

-- Comment: That's a lovely bit of code! You got the right answer, selected
-- only the data you need AND kept it nice and clean.
-- 5/5

-- Task 3.2
SELECT 
	supplier.SNAME, part.PNAME, project.JNAME
FROM 
	part
INNER JOIN supply ON supply.P_ID = part.P_ID
INNER JOIN 	supplier ON supplier.S_ID = supply.S_ID
INNER JOIN project ON project.J_ID = supply.J_ID
WHERE part.CITY = supplier.CITY AND supplier.CITY = project.CITY;

-- Comment: Lovely looking query, perfect results.
-- 5/5

-- Overall: Awesome start, keep it up. Some awesome queries, there's also
-- a few extranious lines but mostly no harm in the output. Keep it up,
-- you've clearly but in the effort to understand these concepts.
-- 61/65 - 94%
