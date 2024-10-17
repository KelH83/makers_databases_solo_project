## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORIES:

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.
Items > name, unit_price

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.
Items > qty

As a shop manager
So I can manage items
I want to be able to create a new item.
ADD NEW item

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.
Orders > customer_name

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.
Items_Orders

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 
Orders > date_placed

As a shop manager
So I can manage orders
I want to be able to create a new order.
ADD NEW order

```

```
Nouns:

Items, name, unit_price, qty, Orders, customer_name, date_placed
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| Items                 | name, unit_price, qty
| Orders                | customer_name, date_placed

1. Name of the first table (always plural): `items` 

    Column names: `name`, `unit_price`, `qty`

2. Name of the second table (always plural): `orders` 

    Column names: `customer_name`, `date_placed`

## 3. Decide the column types.

```
# EXAMPLE:

Table: items
id: SERIAL
name: VARCHAR(250)
unit_price: FLOAT
qty: INT

Table: orders
id: SERIAL
customer_name: VARCHAR(250)
date_placed: DATE
```

## 4. Design the Many-to-Many relationship

```

1. Can one item have many orders? YES
2. Can one order have many items? YES
```
## 5. Design the Join Table.

```

Join table for tables: items and orders
Join table name: items_orders
Columns: item_id, order_id
```

## 6. Write the SQL.

```sql
-- file: shop.sql

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(250),
  unit_price FLOAT,
  qty: INT
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name VARCHAR(250)
);

CREATE TABLE items_orders (
  item_id int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 database_solo_project < shop.sql
```