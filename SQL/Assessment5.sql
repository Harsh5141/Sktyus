  create table users(
  user_id int primary key,
  name varchar(50),
  email varchar(100) unique,
  password varchar(100) not null
  );

  insert into users (user_id, name, email, password) values
(1, 'dev',  'dev@gmail.com',  'dev@123'),
(2, 'Amit', 'amit@gmail.com', 'amit@123'),
(3, 'harsh',  'harsh@gmail.com', 'harsh@123'),
(4, 'mann',  'mann@gmail.com',  'mann@123');

select * from users

  CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(10,2),
    user_id INT
);

insert into orders (order_id, user_id,amount, order_date) values
(01, 1, 2500, '2025-01-11'),
(02, 2, 1800, '2005-08-13'),
(03, 4, 5000, '2015-06-20'),
(04, 1, 3200, '2012-03-25'),
(05, 3, 1500, '2019-04-28');
select * from orders





ALTER TABLE orders
ADD CONSTRAINT fk_user_order
FOREIGN KEY (user_id)
REFERENCES users(user_id);



--Create index on email column
CREATE INDEX idx_user_email
ON users(email);
    
  --Create view to display user order summary
  CREATE VIEW user_order_summary AS
SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;

--How to use the view
SELECT * FROM user_order_summary;

