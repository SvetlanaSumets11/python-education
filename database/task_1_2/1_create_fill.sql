DROP TABLE IF EXISTS rent;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS car;
DROP TABLE IF EXISTS branch;
DROP TABLE IF EXISTS adress;

CREATE TABLE adress (
    adress_id serial   NOT NULL,
    city varchar(30)   NOT NULL,
    street varchar(50),
    house int             CHECK(house > 0),
	telephone varchar(10) UNIQUE CHECK(telephone NOT LIKE '%[^0-9]%'),

	PRIMARY KEY(adress_id)
);

CREATE TABLE branch (
    branch_id serial        NOT NULL,
    adress_id int           NOT NULL,
    branch_name VARCHAR(20) NOT NULL,

	PRIMARY KEY(branch_id),
	FOREIGN KEY(adress_id) REFERENCES adress(adress_id)
);

CREATE TABLE car (
    car_id serial      NOT NULL,
    car_num varchar(8) NOT NULL,
	brand varchar(50)  NOT NULL,
	model varchar(50)  NOT NULL,
	price int          NOT NULL,
	branch_id int      NOT NULL,

	PRIMARY KEY(car_id),
	FOREIGN KEY(branch_id) REFERENCES branch(branch_id)
);

CREATE TABLE customer (
    customer_id serial     NOT NULL,
    first_name varchar(25) NOT NULL,
    last_name varchar(25)  NOT NULL,
    adress_id int,

	PRIMARY KEY(customer_id),
	FOREIGN KEY(adress_id) REFERENCES adress(adress_id)
);

CREATE TABLE rent (
    rent_id serial  NOT NULL,
    car_id int      NOT NULL,
	customer_id int,
	rent_period int NOT NULL,
	rent_date timestamp NOT NULL,

	PRIMARY KEY(rent_id),
	FOREIGN KEY(car_id) REFERENCES car(car_id),
	FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);


CREATE SEQUENCE seq_num
    INCREMENT 1
    START 1;

-- SELECT nextval('seq_num');
-- DROP SEQUENCE seq_num;

CREATE OR REPLACE FUNCTION random_telephone()
RETURNS varchar
LANGUAGE plpgsql
AS $$
DECLARE
   tel_num varchar;
BEGIN
	SELECT format('%s%s%s%s%s%s%s%s%s%s',
				  tel[1], tel[2], tel[3], tel[4], tel[5],
				  tel[6], tel[7], tel[8], tel[9], tel[10])
	INTO tel_num
	FROM(
	   SELECT ARRAY(
		  SELECT trunc(random() * 10)::int
		  FROM generate_series(1, 10)
		  )AS tel
	   )sub;

	RETURN tel_num;
END;$$;

-- DROP FUNCTION random_telephone;

CREATE OR REPLACE PROCEDURE fill_adress()
LANGUAGE plpgsql
AS $$
DECLARE
    i_current int = 1;
	i_end int = 300;
BEGIN
	WHILE i_current <= i_end
	LOOP
		i_current = i_current + 1;
		INSERT INTO adress
			VALUES (nextval('seq_num'),
					'city_'   || currval('seq_num'),
					'street_' || currval('seq_num'),
					trunc(random() * 300) + 1::int,
					random_telephone());
	END LOOP;
END;$$;

CALL fill_adress();
SELECT * FROM adress;

-- DELETE FROM adress;


DROP SEQUENCE seq_num;
CREATE SEQUENCE seq_num
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE fill_branch()
LANGUAGE plpgsql
AS $$
DECLARE
    i_current int = 1;
	i_end int = 300;
BEGIN
	WHILE i_current <= i_end
	LOOP
		i_current = i_current + 1;
		INSERT INTO branch
			VALUES (nextval('seq_num'),
					currval('seq_num'),
					'branch_' || currval('seq_num'));
	END LOOP;
END;$$;

CALL fill_branch();
SELECT * FROM branch;

-- DELETE FROM branch;


DROP SEQUENCE seq_num;
CREATE SEQUENCE seq_num
    INCREMENT 1
    START 1;

CREATE OR REPLACE FUNCTION random_car_num()
RETURNS varchar
LANGUAGE plpgsql
AS $$
DECLARE
   car_num varchar;
BEGIN
	SELECT format('AX%s%s%s%s%s%s',
				  cars[1], cars[2], cars[3], cars[4], cars[5], cars[6])
	INTO car_num
	FROM(
	   SELECT ARRAY(
		  SELECT trunc(random() * 10)::int
		  FROM generate_series(1, 10)
		  )AS cars
	   )sub;

	RETURN car_num;
END;$$;

CREATE OR REPLACE PROCEDURE fill_car()
LANGUAGE plpgsql
AS $$
DECLARE
    i_current int = 1;
	i_end int = 7894;
BEGIN
	WHILE i_current <= i_end
	LOOP
		i_current = i_current + 1;
		INSERT INTO car
			VALUES (nextval('seq_num'),
					random_car_num(),
					'brand_' || currval('seq_num'),
					'model_' || currval('seq_num'),
					trunc(random() * 10000) + 1::int,
					trunc(random() * 200) + 1::int);
	END LOOP;
END;$$;

CALL fill_car();
SELECT * FROM car;

-- DELETE FROM car;


DROP SEQUENCE seq_num;
CREATE SEQUENCE seq_num
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE fill_customer()
LANGUAGE plpgsql
AS $$
DECLARE
    i_current int = 1;
	i_end int = 12344;
BEGIN
	WHILE i_current <= i_end
	LOOP
		i_current = i_current + 1;
		INSERT INTO customer
			VALUES (nextval('seq_num'),
					'first_name_' || currval('seq_num'),
					'last_name_' || currval('seq_num'),
					trunc(random() * 200) + 1::int);
	END LOOP;
END;$$;

CALL fill_customer();
SELECT * FROM customer;

-- DELETE FROM customer;


DROP SEQUENCE seq_num;
CREATE SEQUENCE seq_num
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE fill_rent()
LANGUAGE plpgsql
AS $$
DECLARE
    i_current int = 1;
	i_end int = 15000;
BEGIN
	WHILE i_current <= i_end
	LOOP
		i_current = i_current + 1;
		INSERT INTO rent
			VALUES (nextval('seq_num'),
					trunc(random() * 7000) + 1::int,
					trunc(random() * 12000) + 1::int,
					trunc(random() * 30) + 1::int,
					timestamp '2021-01-10 20:00:00' +
						random() * (timestamp '2001-01-01 07:00:00' -
								timestamp '2021-07-01 10:00:00'));
	END LOOP;
END;$$;

CALL fill_rent();
SELECT * FROM rent;

-- DELETE FROM rent;
