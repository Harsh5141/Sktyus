use ECommerceDB
--Add index to improve search on orders.customer_id
  create index idx_orders_customer_id
  on orders(customer_id);

  --Use EXPLAIN to analyze query

  select * from orders
  where customer_id = 101;

  --Optimize a slow join query
  SELECT *
FROM orders
WHERE customer_id = 101;

--Explain when index should not be used"
select * from customers
WHERE name LIKE 'Amit%'

select * from customers;
