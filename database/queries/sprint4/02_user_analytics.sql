-- Country Wise Users
SELECT country,
COUNT(*) AS total_users
FROM users
GROUP BY country
ORDER BY total_users DESC;

-- City Wise Users
SELECT city,
COUNT(*)
FROM users
GROUP BY city
ORDER BY COUNT(*) DESC;

-- Gender Distribution
SELECT gender,
COUNT(*)
FROM users
GROUP BY gender;

-- Subscription Distribution
SELECT s.plan_name,
COUNT(*) AS total_users
FROM users u
JOIN subscriptions s
ON u.subscription_id=s.subscription_id
GROUP BY s.plan_name
ORDER BY total_users DESC;

-- Average Age
SELECT
ROUND(AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE,date_of_birth))),2)
AS average_age
FROM users;

-- New Users Per Year
SELECT
EXTRACT(YEAR FROM signup_date) AS year,
COUNT(*)
FROM users
GROUP BY year
ORDER BY year;