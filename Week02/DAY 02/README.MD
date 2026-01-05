1. Find the departments where the average salary is higher than the company-wide average salary.
->  SELECT department, AVG(salary) AS dept_avg_salary FROM employees GROUP BY department HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);

2. Using a CTE, find the top 3 products sold in each region.
->  WITH sorted as 
(SELECT region,product, quantity, dense_rank() over(partition by region order by quantity desc)as rnk from sales)
select region, product from sorted where rnk<4;

3. When is a correlated subquery inefficient?
->  A correlated subquery becomes inefficient when it is executed repeatedly for each row over a large dataset which result in poor query performance
