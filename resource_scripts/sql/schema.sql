DROP DATABASE IF EXISTS MyCart;
CREATE DATABASE MyCart;
use MyCart;

DROP TABLE  IF EXISTS users;
DROP TABLE  IF EXISTS category;
DROP TABLE  IF EXISTS products;
DROP TABLE  IF EXISTS productDetails;
DROP TABLE  IF EXISTS address;
DROP TABLE  IF EXISTS userCart;
DROP TABLE  IF EXISTS orders;
DROP TABLE  IF EXISTS orderItem;
DROP TABLE  IF EXISTS discount;

CREATE TABLE users (
	user_id 	INT AUTO_INCREMENT	PRIMARY KEY,
	first_name	CHAR(25) 	NOT NULL,
	last_name	CHAR(25) 	NOT NULL,     
	email   	CHAR(50)	NOT NULL,
	contact_number CHAR(10)    	NOT NULL,
	password 	VARBINARY(128)	NOT NULL,
	user_type	SMALLINT,
	creation_date	DATETIME	DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE category (
	category_id INT AUTO_INCREMENT PRIMARY KEY,
	cname CHAR(100),
	info CHAR(200) NOT NULL
);

CREATE TABLE products (
	product_id INT AUTO_INCREMENT PRIMARY KEY,
	category_id INT,
	product_name VARCHAR(100),
	info CHAR(200) NOT NULL,
	price INT NOT NULL,
	FOREIGN KEY (category_id) REFERENCES category(category_id)
);


CREATE TABLE productDetails (
	product_detail_id INT AUTO_INCREMENT PRIMARY KEY,
	product_id INT,
	color VARCHAR(20),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE userCart (
	cart_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT,
	product_id INT,
	saved_for_later BOOLEAN,
	qty INT,	
	creation_date	DATETIME	DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE address (
	address_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
	address_1 VARCHAR(100),
	address_2 VARCHAR(100),
	postal_code VARCHAR(6),
	city VARCHAR(20),
	FOREIGN KEY (user_id) REFERENCES users(user_id)	
);

CREATE TABLE discount (
	discount_id 	INT 	AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20),
	amount 	INT,
	discount FLOAT(100,2),
	type	BOOLEAN,
	quantity INT
);

CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT,
	address_id INT,
	discount_id INT,
	creation_date	DATETIME	DEFAULT CURRENT_TIMESTAMP,
	STATUS VARCHAR(100),
	amount INT,
	modified DATETIME	DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (address_id) REFERENCES address(address_id),
	FOREIGN KEY (discount_id) REFERENCES discount(discount_id)
);

CREATE TABLE orderItem (
	order_item_id INT AUTO_INCREMENT PRIMARY KEY,
	order_id INT,
	product_id INT,
	quantity INT NULL,
	FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);


