create table accounts(
acc_id int,
acc_name varchar(50),
balance int 
);

insert into accounts values
(101,'harsh', 69000),
(102, 'Amit', 65000),
(103,'dev',55000),
(104, 'Darshan',48000);

--Start a transaction
BEGIN transaction;

--Insert record into accounts
BEGIN TRANSACTION;

INSERT INTO accounts
VALUES (105, 'lalu', 50000);
--Rollback changes
rollback;
--Commit valid transactions
BEGIN TRANSACTION;

INSERT INTO accounts
VALUES (105, 'LALU', 50000);

COMMIT;

select *from accounts;

--Demonstrate money transfer using transaction
BEGIN TRANSACTION;

-- Deduct from Amit
UPDATE accounts
SET balance = balance - 2000
WHERE acc_name = 'Amit';

-- Add to harsh
UPDATE accounts
SET balance = balance + 2000
WHERE acc_name = 'harsh';

-- Check balances
SELECT * FROM accounts;

-- If everything is OK
COMMIT;

-- If any error occurs
-- ROLLBACK;
