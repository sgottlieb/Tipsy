
create table Users (
    id INTEGER PRIMARY KEY,
    email VARCHAR(64),
    password VARCHAR(64),
    name VARCHAR(64)
);
create table Tasks (
    id INTEGER PRIMARY KEY,
    title VARCHAR(64),
    created_at Current_Timestamp,
    completed_at Current_Timestamp,
    user_id INTEGER
);