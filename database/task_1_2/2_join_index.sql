EXPLAIN SELECT car_id, car_num, brand, model, price
FROM rent
	LEFT JOIN car    USING(car_id)
	LEFT JOIN branch USING(branch_id)
WHERE car_num LIKE '%5%' AND brand LIKE '%6';

-- DROP INDEX idx_car_num_with_5;

CREATE INDEX idx_car_num_with_5 ON car(car_num)
WHERE car_num LIKE '%5%' AND brand LIKE '%6';


EXPLAIN SELECT adress_id, city, street, house
FROM customer RIGHT JOIN adress USING(adress_id)
WHERE customer.adress_id IS NULL;


EXPLAIN SELECT first_name, last_name,
		car_num, brand, model, price,
		rent_period, rent_date
FROM car
	JOIN rent USING(car_id)
	JOIN customer USING(customer_id)
WHERE first_name LIKE '%1%' AND last_name LIKE '%5';

-- DROP INDEX idx_first_name_like_1;

CREATE INDEX idx_first_name_like_1 ON customer(first_name)
WHERE first_name LIKE '%1%' AND last_name LIKE '%5';
