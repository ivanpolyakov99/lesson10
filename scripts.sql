CREATE TABLE users (
  first_name VARCHAR(100),
  last_name VARCHAR(100)
  age INT
);
CREATE TABLE orders (
  text VARCHAR(100),
  user_id INT
)

SELECT * FROM users;

SELECT first_name, age FROM users;

SELECT * FROM users LIMIT 3;

SELECT * FROM users WHERE age > 25 AND first_name = 'Mark';

SELECT * FROM users, orders
WHERE orders.user_id = users.id
      AND users.first_name = 'Hello';


SELECT * FROM users
JOIN orders
ON users.id = orders.user_id


INSERT INTO users (first_name, last_name, age) VALUES
  ('Nicolle', 'Travers', 20),
  ('Rumaysa', 'Stacey', 21),
  ('Kelise', 'Schwartz', 22),
  ('Skyla', 'Parsons', 23),
  ('Fenton', 'Harrell', 24),
  ('Habibah', 'East', 25),
  ('Amman', 'Slater', 26),
  ('Henrietta', 'England', 27),
  ('Chay', 'Hackett', 28),
  ('Ahmad', 'Hughes', 29)


UPDATE users
SET first_name = 'Hello',
    last_name = 'World', age = 99
WHERE id = 1;

DELETE FROM users WHERE id = 1