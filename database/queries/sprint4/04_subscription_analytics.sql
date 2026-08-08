-- Total Revenue
SELECT
SUM(amount)
FROM payments
WHERE payment_status='SUCCESS';

-- Revenue By Plan
SELECT
s.plan_name,
SUM(p.amount)
FROM payments p
JOIN subscriptions s
ON p.subscription_id=s.subscription_id
WHERE payment_status='SUCCESS'
GROUP BY s.plan_name
ORDER BY SUM(p.amount) DESC;

-- Payment Method Usage
SELECT
payment_method,
COUNT(*)
FROM payments
GROUP BY payment_method
ORDER BY COUNT(*) DESC;

-- Payment Status
SELECT
payment_status,
COUNT(*)
FROM payments
GROUP BY payment_status;

-- Monthly Revenue
SELECT
DATE_TRUNC('month',payment_date) AS month,
SUM(amount)
FROM payments
WHERE payment_status='SUCCESS'
GROUP BY month
ORDER BY month;