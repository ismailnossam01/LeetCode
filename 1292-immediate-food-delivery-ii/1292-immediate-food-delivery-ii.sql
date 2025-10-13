# Write your MySQL query statement below
SELECT 
    ROUND(SUM(IF(order_date = customer_pref_delivery_date,1,0))*100 / COUNT(distinct customer_id),2) as        immediate_percentage
FROM 
    Delivery


WHERE(customer_id, order_date) IN (SELECT customer_id, MIN(order_date) as first_order 
FROM Delivery
GROUP BY 
    customer_id)