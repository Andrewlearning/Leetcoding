--
--O_Id	OrderDate	OrderPrice	Customer
--1	2008/12/29	    1000	       Bush
--2	2008/11/23	    1600	     Carter
--3	2008/10/05	    700	           Bush
--4	2008/09/28	    300	           Bush
--5	2008/08/06	    2000	      Adams
--6	2008/07/21	    100	         Carter

SELECT
    customer, sum(OrderPrice)
FROM
    Orders
GROUP BY
    Customer

--Customer	SUM(OrderPrice)
--Bush	    2000
--Carter	1700
--Adams	    2000