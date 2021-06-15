SELECT *
FROM potential_customers;

BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

INSERT INTO potential_customers
	VALUES (11, 'email1@gmail.com', 'Svetlana2', 'Sumets2', 'Igorevna2', 'city 12');

SAVEPOINT point_1;

INSERT INTO potential_customers
	VALUES (12, 'email1@gmail.com', 'Svetlana3', 'Sumets3', 'Igorevna3', 'city 12');
INSERT INTO potential_customers
	VALUES (13, 'email1@gmail.com', 'Svetlana4', 'Sumets4', 'Igorevna4', 'city 12');

SAVEPOINT point_2;

UPDATE potential_customers
	SET name = 'Anna'
WHERE pot_cus_id = 13;

DELETE FROM potential_customers
WHERE pot_cus_id = 11;

RELEASE SAVEPOINT point_1;
RELEASE SAVEPOINT point_2;

ROLLBACK TO SAVEPOINT point_1;
ROLLBACK TO SAVEPOINT point_2;

COMMIT;
ROLLBACK;


SELECT *
FROM order_status;

BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

INSERT INTO order_status VALUES (6, 'Moved');

SAVEPOINT point_1;

DELETE FROM order_status
WHERE order_status_id = 6;

UPDATE order_status
	SET status_name = 'Restored'
WHERE order_status_id = 1;

SAVEPOINT point_2;

UPDATE order_status
	SET status_name = 'Accepted'
WHERE order_status_id = 1;

INSERT INTO order_status VALUES (7, 'Unpaid');

RELEASE SAVEPOINT point_1;
RELEASE SAVEPOINT point_2;

ROLLBACK TO SAVEPOINT point_1;
ROLLBACK TO SAVEPOINT point_2;

COMMIT;
ROLLBACK;


SELECT *
FROM categories;

BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

DELETE FROM categories
WHERE category_id = 6;

UPDATE categories
	SET category_description = 'My description'
WHERE category_id = 1;

SAVEPOINT point_1;

INSERT INTO categories VALUES (6, 'Category 6', 'Category 6 description');

UPDATE categories
	SET category_description = 'Category 1 description'
WHERE category_id = 1;

RELEASE SAVEPOINT point_1;

ROLLBACK TO SAVEPOINT point_1;

COMMIT;
ROLLBACK;
