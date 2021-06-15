SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'products';

--1. Выбрать пользователей, что живут в городе 17
EXPLAIN SELECT user_id, last_name, first_name, email, city
FROM users
WHERE city = 'city 17';

-- DROP INDEX idx_users_city_17;

CREATE INDEX idx_users_city_17 ON users(city)
WHERE city = 'city 17';

EXPLAIN SELECT user_id, last_name, first_name, email, city
FROM users
WHERE city = 'city 17';

--2. Продукты, цена которых между 60.00 и 100.00
EXPLAIN SELECT product_id, product_title, price
FROM products
WHERE price BETWEEN 60.00 AND 100.00
ORDER BY 3 DESC;

-- DROP INDEX idx_products_between;

CREATE INDEX idx_products_between ON products(price)
WHERE price BETWEEN 60.00 AND 100.00;

EXPLAIN SELECT product_id, product_title, price
FROM products
WHERE price BETWEEN 60.00 AND 100.00
ORDER BY 3 DESC;

-- 3. Заказы, полученные за второе полугодие 2020 года
EXPLAIN SELECT order_id, created_at
FROM orders
WHERE EXTRACT(MONTH FROM created_at) > 7
	AND EXTRACT(YEAR FROM created_at) = 2020;

-- DROP INDEX idx_orders_second_half_year;

CREATE INDEX idx_orders_second_half_year ON orders(order_id, created_at)
WHERE EXTRACT(MONTH FROM created_at) > 7
	AND EXTRACT(YEAR FROM created_at) = 2020;

EXPLAIN SELECT order_id, created_at
FROM orders
WHERE EXTRACT(MONTH FROM created_at) > 7
	AND EXTRACT(YEAR FROM created_at) = 2020;



EXPLAIN SELECT user_id, last_name, first_name, count(cart_id) as amount, status_name
FROM users
	JOIN carts        ON user_id = users_user_id
	JOIN orders       ON cart_id = carts_cart_id
	JOIN order_status ON order_status_order_status_id = order_status_id
WHERE last_name ILIKE '%2%' AND first_name ILIKE '%1%'
GROUP BY user_id, last_name, first_name, status_name
ORDER BY amount DESC;

-- DROP INDEX idx_last_first_name;

CREATE INDEX idx_last_first_name ON users(last_name, first_name)
WHERE last_name ILIKE '%2%' AND first_name ILIKE '%1%';
