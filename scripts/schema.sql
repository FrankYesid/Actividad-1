CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL UNIQUE,
    area VARCHAR(80) NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_courses_name ON courses (name);
CREATE INDEX IF NOT EXISTS ix_courses_area ON courses (area);

CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(180) NOT NULL UNIQUE,
    course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS ix_students_name ON students (name);
CREATE INDEX IF NOT EXISTS ix_students_email ON students (email);

INSERT INTO courses (name, area)
VALUES ('Minería de datos', 'Analítica')
ON CONFLICT (name) DO NOTHING;