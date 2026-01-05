1. Write a query to find all customers who have never placed an order.
->   select customers from cust where order_id is NUll;

2. What is the difference between an INNER JOIN and a LEFT JOIN?
->  The inner join returns the value common in both the TABLES where as the left join returns all the values from the left table and the common values from the right table

3. Combine results from two tables with compatible columns, including duplicates. Which operator would you use?
->  UNION ALL is used to combine two tables with compatible columns, including duplicates.
