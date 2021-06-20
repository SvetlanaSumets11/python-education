CREATE FUNCTION check_entered_customer()
RETURNS TRIGGER
AS $$
BEGIN
    IF length(NEW.last_name) < 11
		OR NEW.last_name IS NULL
		OR length(NEW.first_name) < 12
		OR NEW.first_name IS NULL
	THEN
        RAISE EXCEPTION 'The entered customer name does not match';
    END IF;
    IF NEW.last_name IS NULL
		OR NEW.first_name IS NULL
	THEN
        RAISE EXCEPTION 'Customer name cannot be NULL';
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER customer_name_check
    BEFORE UPDATE
	ON customer
	FOR EACH ROW
    EXECUTE PROCEDURE check_entered_customer();

DROP TRIGGER customer_name_check ON customer;

SELECT * FROM customer;

UPDATE customer
SET last_name = 'customer_last_name'
WHERE customer_id = 1;

UPDATE customer
SET last_name = ''
WHERE customer_id = 1;

UPDATE customer
SET last_name = 'last_name'
WHERE customer_id = 1;


CREATE OR REPLACE FUNCTION check_car_price()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
	IF NEW.price < 0 THEN
		RAISE 'The price of the car cannot be less then 0';
	END IF;
	RETURN NEW;
END;
$$;

CREATE TRIGGER validation_car_price
	AFTER INSERT OR UPDATE
	ON car
	FOR EACH ROW
	EXECUTE PROCEDURE check_car_price();

DROP TRIGGER validation_car_price ON car;

SELECT * FROM car;

UPDATE car
SET price = 10000
WHERE car_id = 1;

UPDATE car
SET price = -10000
WHERE car_id = 1;
