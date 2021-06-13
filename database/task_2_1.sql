CREATE TABLE public.users (
    user_id serial NOT NULL,
    email varchar(255),
    password varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    middle_name varchar(255),
    is_staff smallint,
    country varchar(255),
    city varchar(255),
    address text
);

CREATE TABLE public.carts (
    cart_id serial NOT NULL,
    users_user_id int,
    subtotal decimal,
    total decimal,
    time_stamp timestamp(2)
);

CREATE TABLE public.cart_product (
    carts_cart_id int NOT NULL,
    products_product_id int NOT NULL
);

CREATE TABLE public.products (
    product_id serial NOT NULL,
    product_title varchar(255),
    product_description text,
    in_stock int,
    price float,
    slug varchar (45),
    category_id int
);

CREATE TABLE public.categories (
    category_id serial NOT NULL,
    category_tittle varchar(255),
    category_description text
);

CREATE TABLE public.orders (
    order_id serial NOT NULL,
    carts_cart_id int,
    order_status_order_status_id int,
    shipping_total decimal,
    total decimal,
    created_at timestamp(2),
    updated_at timestamp(2)
);

CREATE TABLE public.order_status (
    order_status_id serial NOT NULL,
    status_name varchar(255)
);

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);

ALTER TABLE ONLY public.carts
    ADD CONSTRAINT carts_pkey PRIMARY KEY (cart_id);

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);

ALTER TABLE ONLY public.order_status
    ADD CONSTRAINT order_status_pkey PRIMARY KEY (order_status_id);

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


ALTER TABLE ONLY public.carts
    ADD CONSTRAINT users_user_id_fkey FOREIGN KEY (users_user_id) REFERENCES public.users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT carts_cart_id2_fkey FOREIGN KEY (carts_cart_id) REFERENCES public.carts(cart_id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE ONLY public.orders
    ADD CONSTRAINT order_status_order_status_id_fkey FOREIGN KEY (order_status_order_status_id) REFERENCES public.order_status(order_status_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY public.cart_product
    ADD CONSTRAINT carts_cart_id_fkey FOREIGN KEY (carts_cart_id) REFERENCES public.carts(cart_id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE ONLY public.cart_product
    ADD CONSTRAINT products_product_id_fkey FOREIGN KEY (products_product_id) REFERENCES public.products(product_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY public.products
    ADD CONSTRAINT category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id) ON UPDATE CASCADE ON DELETE RESTRICT;


COPY public.users (user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
FROM '/usr/src/users.csv' DELIMITER ',' CSV;

COPY public.categories (category_id, category_tittle, category_description)
FROM '/usr/src/categories.csv' DELIMITER ',' CSV;

COPY public.order_status (order_status_id, status_name)
FROM '/usr/src/order_statuses.csv' DELIMITER ',' CSV;

COPY public.products (product_id, product_title, product_description, in_stock, price, slug, category_id)
FROM '/usr/src/products.csv' DELIMITER ',' CSV;

COPY public.carts (cart_id, users_user_id, subtotal, total, time_stamp)
FROM '/usr/src/carts.csv' DELIMITER ',' CSV;

COPY public.orders (order_id, carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at)
FROM '/usr/src/orders.csv' DELIMITER ',' CSV;

COPY public.cart_product (carts_cart_id, products_product_id)
FROM '/usr/src/cart_products.csv' DELIMITER ',' CSV;

ALTER TABLE users
ADD COLUMN phone_number int;

ALTER TABLE users
ALTER COLUMN phone_number TYPE varchar(20);

UPDATE products SET price = price * 2;