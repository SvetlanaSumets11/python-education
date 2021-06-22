CREATE OR REPLACE FUNCTION rent_info(arg_car_id int)
RETURNS TABLE (
	arg_car_num varchar,
	arg_first_name varchar,
	arg_last_name varchar
)
LANGUAGE plpgsql
AS $$
DECLARE
    var_r record;
BEGIN
	FOR var_r IN (
		SELECT car_num, first_name, last_name, rent_date
		FROM car JOIN rent     USING(car_id)
				 JOIN customer USING(customer_id)
		WHERE car_id > arg_car_id
        ) LOOP  arg_car_num    := LOWER(var_r.car_num);
				arg_first_name := UPPER(var_r.first_name);
				arg_last_name  := UPPER(var_r.last_name);
           RETURN NEXT;
	END LOOP;
END; $$;

SELECT * FROM rent_info (700);
DROP FUNCTION IF EXISTS rent_info;


CREATE OR REPLACE FUNCTION info_rent_car(arg_brand varchar)
RETURNS text
AS $$
DECLARE
	 results text DEFAULT '';
	 rec_car record;
	 car_info CURSOR(arg_brand varchar)
		 FOR SELECT car_num, brand, model
		 FROM car
		 WHERE brand = arg_brand;
BEGIN
   OPEN car_info(arg_brand);

   LOOP
      FETCH car_info into rec_car;
      EXIT WHEN NOT FOUND;

      IF rec_car.car_num LIKE '%6%'
	  THEN
         results := 'Number: '  || rec_car.car_num ||
		 			' Brand: '  || rec_car.brand   ||
					' Model: '  || rec_car.model;
      END IF;
   END LOOP;

   CLOSE car_info;
   RETURN results;
END; $$
LANGUAGE plpgsql;

SELECT info_rent_car('brand_2');
