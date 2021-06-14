-- Вывести всех юзеров
SELECT * FROM users;


-- Вывести все продукты
SELECT * FROM products;


-- Вывести все статусы заказов
SELECT * FROM order_status;


-- Вывести заказы, которые успешно доставлены и оплачены
SELECT order_id, status_name
FROM orders JOIN order_status ON order_status_order_status_id = order_status_id
WHERE status_name = 'Finished';


-- Вывести продукты, цена которых больше 80.00 и меньше или равно 150.00
SELECT product_id, product_title, price
FROM products
WHERE price > 80.00 and price <= 150.00
ORDER BY 3 DESC;

-- Вывести продукты, цена которых больше 80.00 и меньше или равно 150.00
SELECT product_id, product_title, price
FROM products
WHERE price BETWEEN 80.00 AND 150.00
ORDER BY 3 DESC;


-- Вывести заказы совершенные после 01.10.2020 (поле created_at)
SELECT order_id, created_at
FROM orders
WHERE created_at > to_timestamp('01 10 2020', 'DD MM YYYY')
ORDER BY 2;


-- Вывести заказы, полученные за первое полугодие 2020 года
SELECT order_id, created_at
FROM orders
WHERE created_at BETWEEN
	to_timestamp('01 01 2020', 'DD MM YYYY')
	AND to_timestamp('30 06 2020', 'DD MM YYYY')
ORDER BY 2;

-- Вывести заказы, полученные за первое полугодие 2020 года
SELECT order_id, created_at
FROM orders
WHERE EXTRACT(MONTH FROM created_at) < 7
	AND EXTRACT(YEAR FROM created_at) = 2020
ORDER BY 2 DESC;


-- Вывести подукты следующих категорий: Category 7, Category 11, Category 18
SELECT product_id, product_title, category_tittle
FROM products JOIN categories
	ON products.category_id = categories.category_id
WHERE category_tittle IN ('Category 7', 'Category 11', 'Category 18');

-- Вывести подукты следующих категорий: Category 7, Category 11, Category 18
SELECT product_id, product_title, category_tittle
FROM products JOIN categories
	ON products.category_id = categories.category_id
WHERE category_tittle = 'Category 7'
	OR category_tittle = 'Category 11'
	OR category_tittle = 'Category 18';

-- Вывести подукты следующих категорий: Category 7, Category 11, Category 18
SELECT product_id, product_title, category_tittle
FROM products JOIN categories
	ON products.category_id = categories.category_id
WHERE category_tittle LIKE '% 7'
	OR category_tittle LIKE '%11'
	OR category_tittle LIKE'%18';


-- Вывести незавершенные заказы по состоянию на 31.12.2020
SELECT order_id, status_name, created_at
FROM orders JOIN order_status
	ON order_status_order_status_id = order_status_id
WHERE status_name != 'Finished'
	AND created_at < to_timestamp('31 12 2020', 'DD MM YYYY')
ORDER BY 3 DESC;


-- Вывести все корзины, которые были созданы, но заказ так и не был оформлен
SELECT cart_id, order_id, carts_cart_id
FROM carts LEFT JOIN orders
	ON cart_id = carts_cart_id
WHERE carts_cart_id IS NULL;


-- Вывести среднюю сумму всех завершенных сделок
SELECT AVG(total) AS "Average_amount"
FROM orders JOIN order_status
	ON order_status_order_status_id = order_status_id
WHERE status_name = 'Finished';


-- Вывести максимальную сумму сделки за 3 квартал 2020
SELECT order_id, created_at, SUM(total) as total_sum
FROM orders
WHERE EXTRACT(QUARTER FROM created_at) = 3
	AND EXTRACT(YEAR FROM created_at) = 2020
GROUP BY order_id, created_at
ORDER BY 3 DESC LIMIT 1;

-- Вывести максимальную сумму сделки за 3 квартал 2020
SELECT MAX(total) as total_sum
FROM orders
WHERE EXTRACT(QUARTER FROM created_at) = 3
	AND EXTRACT(YEAR FROM created_at) = 2020;