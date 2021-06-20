CREATE OR REPLACE PROCEDURE my_procedure_1(amount decimal)
LANGUAGE plpgsql
AS $$
DECLARE
    new_price int;
BEGIN
    UPDATE car
    SET price = price - amount
    WHERE car_id = 1
    RETURNING price
    INTO new_price;

    IF new_price >= 0 THEN
        COMMIT;
        UPDATE car
    	SET price = price + amount
    	WHERE car_id = 1;
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END;$$;

CALL my_procedure_1(1123);
SELECT * FROM car;
DROP PROCEDURE my_procedure_1;


CREATE OR REPLACE PROCEDURE my_procedure_2(arg_id int)
LANGUAGE plpgsql
AS $$
DECLARE
    new_id int;
BEGIN
    UPDATE adress
    SET adress_id = 500
    WHERE adress_id = arg_id
	RETURNING adress_id
    INTO new_id;

	INSERT INTO adress
	VALUES (302, 'my_city', 'my_street', 302, '2222222222');

    IF arg_id >= 300 THEN
		COMMIT;
        DELETE FROM adress
		WHERE adress_id = 302;
		COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END;$$;

CALL my_procedure_2(301);
SELECT * FROM adress;
DROP PROCEDURE my_procedure_2;