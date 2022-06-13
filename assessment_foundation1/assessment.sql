use democracy;

-- TASK 7 A

SELECT e.Candidate, sum(e.Votes) as TotalVotes FROM elections e GROUP BY e.Candidate;

-- TASK 7 B

SELECT e.Candidate, sum(e.Votes) as TotalVotes FROM elections e GROUP BY e.Candidate HAVING TotalVotes > 50;

-- TASK 7 C

-- either:
DELETE FROM elections e WHERE e.RecordID = 13;

-- or if we want to be EXTRA careful and don't trust the notion that RecordId is unique for each entry (as it's not a primary key):

DELETE FROM elections e WHERE e.Candidate = 'Mr Grumpy' and e.Votes = 9 and e.District = 'Pink Area';

-- TASK 7 D:
-- Depending on the type of the most common queries we will be running on this database, we could for example add primary key to RecordID,
-- so that we can quickly choose the exact record. We could also add single index to a column that gets the most queries (to District for example,
-- or to Candidate, if we want to access that data quicker). Or maybe Candidate and District are most often searched in combination? We could then
-- add composite index.

-- for primary key
ALTER TABLE elections ADD PRIMARY KEY (RecordID);

-- for single index on District:
CREATE INDEX district_area ON elections(District);

-- for composite index on Candidate and District:
CREATE INDEX candidate_district ON elections(Candidate, District);

-- TASK 8:

use corporation;

SELECT employees.Department_name FROM employees
JOIN salaries ON salaries.Employee_id = employees.Employee_id
GROUP BY employees.Department_name HAVING avg(salaries.Salary) < 500;

-- TASK 9
CREATE TABLE shopping (
Number INT,
Item VARCHAR(50),
Price FLOAT
);

INSERT INTO shopping 
(Number, Item, Price) 
VALUES 
(7, 'Coffee', 3.20),
(20, 'Extra large coffee', 6.00);