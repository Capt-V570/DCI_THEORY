-- create a database called novem

CREATE DATABASE IF NOT EXISTS november;

-- Linux users: sudo -i -u postgres
-- Mac users: psql -U postgres

-- connect to a database:
\c november


-- Now, create a table called users
-- - name (string)
-- - location (string)
-- - weight (floating)

CREATE TABLE IF NOT EXISTS users (
    name VARCHAR(255),
    location VARCHAR(255),
    weight FLOAT
);

-- forgot something? ('id' column!)

-- UPDATE -> updating data of the table
-- meanwhile:
-- for changing the structure of the table, we use ALTER


ALTER TABLE users ADD COLUMN id SERIAL PRIMARY KEY;


-- DROP a table (VERY RISKY TO DO!!! -in a business scenario- Company data could be loss if not copied beforehand):

DROP TABLE IF EXISTS users;


-- Re-Do the table, but with ID column in it already:

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    weight FLOAT
);

-- connection to november database
\c november
