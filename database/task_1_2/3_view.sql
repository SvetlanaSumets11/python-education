CREATE MATERIALIZED VIEW count_price_rent
AS
SELECT first_name, last_name,
		car_num, brand, model, price,
		rent_period, (price * rent_period) as price_rent
FROM customer
	JOIN rent USING(customer_id)
	JOIN car  USING(car_id)
ORDER BY price_rent DESC;

SELECT * FROM count_price_rent;
DROP MATERIALIZED VIEW count_price_rent;


CREATE VIEW customer_adress
AS
SELECT first_name, last_name, city, street, house
FROM customer JOIN adress USING(adress_id);

SELECT * FROM customer_adress;
DROP VIEW customer_adress;


CREATE VIEW cars_branches
AS
SELECT car_num, brand, model, price, branch_name
FROM car JOIN branch USING(branch_id);

SELECT * FROM cars_branches;
DROP VIEW cars_branches;