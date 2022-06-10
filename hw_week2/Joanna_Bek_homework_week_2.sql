-- TASK 1 SQL

-- Single column index & task 1
use bakery;

CREATE INDEX alphabetical_sweets
ON sweet(item_name);

select * from sweet where item_name like 'c%';

-- Single indexes on many columns
use bakery;

CREATE INDEX alphabetical_sweets
ON sweet(item_name);

CREATE INDEX price_index
ON sweet(price);

select * from sweet where item_name LIKE "c%";
select * from sweet where price > 0.5;

-- Multi-column index & task 2
use bank;

select * from accounts;

CREATE INDEX name_idx on accounts(account_holder_name, account_holder_surname);

select * from accounts where account_holder_name = 'Julie' AND account_holder_surname = 'Smith';

-- Clustered index

DROP INDEX name_idx on accounts;

ALTER TABLE accounts
ADD PRIMARY KEY (account_number);

select * from accounts;

insert into accounts(account_number, account_holder_name, account_holder_surname, balance)
values ('111111', 'Lily', 'Marks', '400');

select * from accounts;