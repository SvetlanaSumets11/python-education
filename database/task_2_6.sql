CREATE VIEW all_from_products
AS
SELECT *
FROM products;

SELECT * FROM all_from_products;
DROP VIEW all_from_products;


CREATE VIEW products_join_categories
AS
SELECT product_id, product_title, product_description,
	price, products.category_id, category_tittle, category_description
FROM products JOIN categories
	ON products.category_id = categories.category_id;

SELECT * FROM products_join_categories;
DROP VIEW products_join_categories;


CREATE VIEW order_join_order_status
AS
SELECT order_id, shipping_total, total, created_at,
	updated_at, order_status_id, status_name
FROM orders JOIN order_status
	ON order_status_order_status_id = order_status_id;

SELECT * FROM order_join_order_status;
DROP VIEW order_join_order_status;


CREATE MATERIALIZED VIEW count_users_with_carts
AS
 SELECT user_id, last_name, first_name, count(cart_id) as amount, status_name
FROM users
	JOIN carts        ON user_id = users_user_id
	JOIN orders       ON cart_id = carts_cart_id
	JOIN order_status ON order_status_order_status_id = order_status_id
GROUP BY user_id, last_name, first_name, status_name
ORDER BY amount DESC;

SELECT * FROM count_users_with_carts;
DROP MATERIALIZED VIEW count_users_with_carts;