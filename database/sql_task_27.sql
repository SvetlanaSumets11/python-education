CREATE OR REPLACE FUNCTION find_shipping_total_with_city(arg_city varchar)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
	WITH my_table as
	(
	SELECT orders.shipping_total, users.city
  	FROM users
  		JOIN carts  ON user_id = users_user_id
		JOIN orders ON cart_id = carts_cart_id
	)
	UPDATE orders
	SET shipping_total = 0
  	FROM my_table
  	WHERE my_table.city = arg_city;

  	IF NOT FOUND THEN
     	RAISE 'The specified city % was not found', arg_city;
  	END IF;
END;$$;

DROP FUNCTION find_shipping_total_with_city;

SELECT find_shipping_total_with_city('city 16');

SELECT orders.shipping_total, users.city
FROM users
	JOIN carts  ON user_id = users_user_id
	JOIN orders ON cart_id = carts_cart_id
WHERE users.city = 'city 16';



DROP PROCEDURE my_procedure_1;

CREATE OR REPLACE PROCEDURE my_procedure_1(amount decimal)
LANGUAGE plpgsql
AS $$
DECLARE
    new_total int;
BEGIN
    UPDATE carts
    SET total = total - amount
    WHERE cart_id = 1
    RETURNING total
    INTO new_total;

    IF new_total >= 0 THEN
        COMMIT;
        UPDATE carts
    	SET total = total + amount
    	WHERE cart_id = 1;
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END;$$;

CALL my_procedure_1(11.2);



DROP PROCEDURE my_procedure_2;

CREATE OR REPLACE PROCEDURE my_procedure_2(arg_user_id int, amount decimal)
LANGUAGE plpgsql
AS $$
DECLARE
    res record;
BEGIN
	FOR res IN (
		SELECT user_id, last_name, sum(orders.total) as summ
		FROM users
			LEFT JOIN carts  ON user_id = users_user_id
			LEFT JOIN orders ON cart_id = carts_cart_id
		WHERE orders.total > amount AND user_id < arg_user_id
		GROUP BY user_id, last_name, first_name
        ) LOOP
				UPDATE carts
    			SET total = res.summ
				WHERE res.last_name LIKE '%1%';
			IF res.summ >= 0 THEN
				COMMIT;
			ELSE
        		ROLLBACK;
    		END IF;
		END LOOP;
END;$$;

CALL my_procedure_2(1000, 11.2);



SELECT category_tittle, product_title, price, AVG(price)
	OVER ( PARTITION BY category_tittle)
FROM products JOIN categories
	ON products.category_id = categories.category_id;



CREATE FUNCTION check_entered_user()
RETURNS TRIGGER
AS $$
BEGIN
    IF length(NEW.last_name) < 11
		OR NEW.last_name IS NULL
		OR length(NEW.first_name) < 12
		OR NEW.first_name IS NULL
		OR length(NEW.middle_name) < 13
		OR NEW.middle_name IS NULL
	THEN
        RAISE EXCEPTION 'The entered username does not match';
    END IF;
    IF NEW.last_name IS NULL
		OR NEW.first_name IS NULL
		OR NEW.middle_name IS NULL
	THEN
        RAISE EXCEPTION 'Username cannot be NULL';
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER username_check
    BEFORE UPDATE
	ON users
	FOR EACH ROW
    EXECUTE PROCEDURE check_entered_user();

DROP TRIGGER username_check ON users;

SELECT * FROM users;

UPDATE users
SET last_name = 'my_last_name_22'
WHERE user_id = 22;

UPDATE users
SET last_name = ''
WHERE user_id = 22;

UPDATE users
SET last_name = 'last_name'
WHERE user_id = 22;



CREATE OR REPLACE FUNCTION check_total()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
	IF NEW.total < 0 THEN
		RAISE 'The total amount cannot be less then 0';
	END IF;
	RETURN NEW;
END;
$$;

CREATE TRIGGER check_total_in_orders
  BEFORE INSERT OR UPDATE
  ON orders
  FOR EACH ROW
  EXECUTE PROCEDURE check_total();

DROP TRIGGER check_total_in_orders ON orders;

SELECT * FROM orders;

UPDATE orders
SET total = 10
WHERE order_id = 1;

UPDATE orders
SET total = -1
WHERE order_id = 1;
