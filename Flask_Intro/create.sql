CREATE DATABASE flask_intro;
-- Command to connect to the flask_intro database
\c flask_intro

-- Create a table called reminders

CREATE TABLE reminders (
    title VARCHAR(255),
    description TEXT
);

-- To run this file
