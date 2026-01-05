1. Calculate the running total of sales month by month.
->  select product, sale, month, sum(sale) over(ordered by month) as month_sale from sales;

2. Find the salary difference between an employee and the average salary of their department.
-> select *, salary - AVG(salary) over(partition by department) as difference from emp;

4. What is the difference between ROW_NUMBER() and RANK()?
->  ROW_NUMBER() is used to give unique number to each row, these numbers are not repeated where as the RANK() function is used to give rank over a attribute, rank can be same for multiple rows with same values and RANK() function skips the rank number after tie.
