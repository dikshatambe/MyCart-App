DROP DATABASE IF EXISTS MyCart;
CREATE DATABASE MyCart;
use MyCart;

DROP TABLE  IF EXISTS users;
DROP TABLE  IF EXISTS category;
DROP TABLE  IF EXISTS products;
DROP TABLE  IF EXISTS userCart;
DROP TABLE  IF EXISTS orders;
DROP TABLE  IF EXISTS discount;
DROP TABLE  IF EXISTS cartInfo;

CREATE TABLE users (
	user_id 	INT PRIMARY KEY,
	first_name	CHAR(25) 	NOT NULL,
	last_name	CHAR(25) 	NOT NULL,     
	email   	CHAR(50)	NOT NULL,
	contact_number CHAR(10)    	NOT NULL,
	address		VARCHAR(200)	NOT NULL,
	postal_code	VARCHAR(6),
	password 	VARBINARY(128)	NOT NULL,
	user_type	SMALLINT,
	creation_date	DATETIME	DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE category (
	category_id INT AUTO_INCREMENT PRIMARY KEY,
	cname VARCHAR(100),
	info VARCHAR(200) NOT NULL
);

CREATE TABLE products (
	product_id INT PRIMARY KEY,
	product_name VARCHAR(100),
	category_id INT,
	info CHAR(200) NOT NULL,
	color VARCHAR(20),
	product_size INT,
	price INT NOT NULL,
	FOREIGN KEY (category_id) REFERENCES category(category_id)
);


CREATE TABLE userCart (
	cart_id INT PRIMARY KEY,
	user_id INT,
	product_id INT,
	saved_for_later BOOLEAN,
	qty INT,	
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id),
	creation_date	DATETIME	DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cartInfo (
	cart_id INT,
	user_id INT,
	product_id INT,
	FOREIGN KEY (cart_id) REFERENCES userCart(cart_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id),
	CONSTRAINT UNIQUE(user_id, product_id)	
);

CREATE TABLE discount (
	discount_id 	INT 	AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20),
	amount 	INT,
	discount FLOAT(100,2),
	discount_type	BOOLEAN,
	quantity INT
);

CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT,
	address VARCHAR(200),
	discount_id INT,
	product_id INT,
	quantity INT NULL,
	STATUS VARCHAR(100),
	amount INT,
	creation_date	DATETIME	DEFAULT CURRENT_TIMESTAMP,
	modified DATETIME	DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (discount_id) REFERENCES discount(discount_id)
);