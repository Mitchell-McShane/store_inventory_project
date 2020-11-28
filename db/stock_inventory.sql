DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS workers;
DROP TABLE IF EXISTS studios;


CREATE TABLE workers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    dob INT
);

CREATE TABLE studios (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    worker_id INT REFERENCES workers(id) ON DELETE CASCADE,
    genre VARCHAR(255),
    price FLOAT,
    buying_cost FLOAT,
    studio_id INT REFERENCES studios(id) ON DELETE CASCADE,
    stock INT NOT NULL DEFAULT 0
);