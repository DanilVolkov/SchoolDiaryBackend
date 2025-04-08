CREATE TABLE IF NOT EXISTS role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "group" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    role_id INTEGER NOT NULL REFERENCES role(id),
    group_id INTEGER REFERENCES "group"(id)
);

CREATE TABLE IF NOT EXISTS subject (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS classroom (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS schedule (
    id SERIAL PRIMARY KEY,
    group_id INTEGER NOT NULL REFERENCES "group"(id),
    subject_id INTEGER NOT NULL REFERENCES subject(id),
    teacher_id INTEGER NOT NULL REFERENCES "user"(id),
    classroom_id INTEGER NOT NULL REFERENCES classroom(id),
    day_of_week INTEGER NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
    lesson_order INTEGER NOT NULL CHECK (lesson_order BETWEEN 1 AND 8)
);

CREATE TABLE IF NOT EXISTS markvalue (
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS lesson (
    id SERIAL PRIMARY KEY,
    schedule_id INTEGER NOT NULL REFERENCES schedule(id),
    group_id INTEGER NOT NULL REFERENCES "group"(id),
    subject_id INTEGER NOT NULL REFERENCES subject(id),
    teacher_id INTEGER NOT NULL REFERENCES "user"(id),
    classroom_id INTEGER NOT NULL REFERENCES classroom(id),
    date DATE NOT NULL,
    time_start TIME NOT NULL,
    time_end TIME NOT NULL,
    CONSTRAINT time_check CHECK (time_end > time_start)
);

CREATE TABLE IF NOT EXISTS mark (
    id SERIAL PRIMARY KEY,
    lesson_id INTEGER NOT NULL REFERENCES lesson(id),
    student_id INTEGER NOT NULL REFERENCES "user"(id),
    value_id INTEGER NOT NULL REFERENCES markvalue(id),
    date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS homework (
    id SERIAL PRIMARY KEY,
    lesson_id INTEGER NOT NULL REFERENCES lesson(id),
    teacher_id INTEGER NOT NULL REFERENCES "user"(id),
    description TEXT NOT NULL,
    date DATE NOT NULL
);

