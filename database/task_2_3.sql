 CREATE TABLE public.potential_customers (
 	pot_cus_id int NOT NULL,
 	email varchar(255),
 	name varchar(255),
 	surname varchar(255),
 	second_name varchar(255),
 	city varchar(255)
 );


 INSERT INTO potential_customers VALUES (1, 'email1@gmail.com', 'Svetlana', 'Sumets', 'Igorevna', 'city 12');
 INSERT INTO potential_customers VALUES (2, 'email2@gmail.com', 'Anna', 'Svitskaya', 'Sergeevna', 'city 17');
 INSERT INTO potential_customers VALUES (3, 'email3@gmail.com', 'Igor', 'Marchenko', 'Evgenevich', 'city 11');
 INSERT INTO potential_customers VALUES (4, 'email4@gmail.com', 'Svetlana', 'Kosikova', 'Pavlovna', 'city 17');
 INSERT INTO potential_customers VALUES (5, 'email5@gmail.com', 'Pavel', 'Antonenko', 'Vitalevich', 'city 17');
 INSERT INTO potential_customers VALUES (6, 'email6@gmail.com', 'Dana', 'Nurova', 'Denisovna', 'city 1');
 INSERT INTO potential_customers VALUES (7, 'email7@gmail.com', 'Sergey', 'Novickov', 'Anatolevich', 'city 22');
 INSERT INTO potential_customers VALUES (8, 'email8@gmail.com', 'Anna', 'Krymskaya', 'Sergeevna', 'city 16');
 INSERT INTO potential_customers VALUES (9, 'email9@gmail.com', 'Ekaterina', 'Fomina', 'Sergeevna', 'city 17');
 INSERT INTO potential_customers VALUES (10, 'email10@gmail.com', 'Kirill', 'Kotelevec', 'Andreevich', 'city 22');


--Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17
SELECT pot_cus_id, name, surname, email, city
FROM potential_customers
WHERE city = 'city 17'
	UNION
SELECT user_id, last_name, first_name, email, city
FROM users
WHERE city = 'city 17';


--Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)
SELECT user_id, last_name, first_name, email, city
FROM users
ORDER BY city, last_name;


--Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества
SELECT category_tittle, count(product_id) AS amount
FROM products JOIN categories
	ON products.category_id = categories.category_id
GROUP BY category_tittle
ORDER BY amount DESC;


--Вывести продукты, которые ни разу не попадали в корзину.
SELECT product_id, products_product_id
FROM products LEFT JOIN cart_product
	ON product_id = products_product_id
WHERE products_product_id IS NULL;


--Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
SELECT product_title
FROM products
	LEFT JOIN cart_product ON product_id = products_product_id
	LEFT JOIN carts        ON cart_product.carts_cart_id = cart_id
	LEFT JOIN orders       ON cart_id = orders.carts_cart_id
WHERE orders.carts_cart_id IS NULL
ORDER BY product_title;


--Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
SELECT product_id, product_title, count(products_product_id) as amount
FROM products JOIN cart_product
	ON product_id = products_product_id
GROUP BY product_id
ORDER BY amount DESC LIMIT 10;


--Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT product_title, count(orders.carts_cart_id) AS amount
FROM products
	JOIN cart_product ON product_id = products_product_id
	JOIN carts        ON cart_product.carts_cart_id = cart_id
	JOIN orders       ON cart_id = orders.carts_cart_id
GROUP BY product_title
ORDER BY amount DESC LIMIT 10;


--Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT user_id, last_name, first_name, orders.total
FROM users
	JOIN carts  ON user_id = users_user_id
	JOIN orders ON cart_id = carts_cart_id
ORDER BY orders.total DESC LIMIT 5;


--Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
SELECT user_id, last_name, first_name, count(order_id) as amount
FROM users
	JOIN carts  ON user_id = users_user_id
	JOIN orders ON cart_id = carts_cart_id
GROUP BY user_id, last_name, first_name
ORDER BY amount DESC LIMIT 5;


--Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
SELECT user_id, last_name, first_name, count(cart_id) as amount
FROM users
	JOIN carts       ON user_id = users_user_id
	LEFT JOIN orders ON cart_id = carts_cart_id
WHERE carts_cart_id IS NULL
GROUP BY user_id, last_name, first_name
ORDER BY amount DESC LIMIT 5;