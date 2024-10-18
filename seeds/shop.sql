DROP TABLE IF EXISTS items_orders;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(250),
  unit_price FLOAT,
  qty INT
);

INSERT INTO items (name, unit_price, qty) VALUES ('Apples', 0.42, 40);
INSERT INTO items (name, unit_price, qty) VALUES ('Broccoli', 0.82, 20);
INSERT INTO items (name, unit_price, qty) VALUES ('Chicken', 5.00, 10);
INSERT INTO items (name, unit_price, qty) VALUES ('Dijon Mustard', 0.59, 15);
INSERT INTO items (name, unit_price, qty) VALUES ('Pasta', 1.29, 20);
INSERT INTO items (name, unit_price, qty) VALUES ('Baked beans', 0.42, 30);
INSERT INTO items (name, unit_price, qty) VALUES ('Chocolate bar', 0.49, 25);
INSERT INTO items (name, unit_price, qty) VALUES ('Toilet roll', 1.45, 10);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name VARCHAR(250),
  date_placed DATE
);

INSERT INTO orders (customer_name, date_placed) VALUES ('Kelly Howes', '2024-10-18');
INSERT INTO orders (customer_name, date_placed) VALUES ('Kimiko Dogue', '2024-10-12');
INSERT INTO orders (customer_name, date_placed) VALUES ('Twyla Kitty', '2024-10-9');

CREATE TABLE items_orders (
  item_id int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

INSERT INTO items_orders (item_id, order_id) VALUES (1, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (1, 2);
INSERT INTO items_orders (item_id, order_id) VALUES (1, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (2, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (2, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (3, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (3, 2);
INSERT INTO items_orders (item_id, order_id) VALUES (3, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (4, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (5, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (5, 2);
INSERT INTO items_orders (item_id, order_id) VALUES (6, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (6, 2);
INSERT INTO items_orders (item_id, order_id) VALUES (7, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (7, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (8, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (8, 2);