-- Active: 1684832160404@@127.0.0.1@5432@default
Active: 1684832160404@@127.0.0.1@5432@default;
CREATE TABLE studentlist(
    id bigserial,
    name text,
    address text,
    date text,
    email text,
    active bool DEFAULT true,
    constraint pkey_student PRIMARY KEY (id)   
);
SELECT * FROM studentlist;
INSERT INTO studentlist (name, address, date, email, active) VALUES ('Mai Tiến Đạt', 'Nam Định', '28022000', 'dat.mt@sis.hust.edu.vn', 'true');
DELETE FROM studentlist WHERE id = 61;
UPDATE studentlist SET active = true ;
SELECT * FROM studentlist ORDER BY name ASC;
CREATE TABLE transcripts(
    id bigserial,
    Course TEXT,
    a FLOAT,
    b FLOAT,
    c FLOAT,
    d FLOAT,
    e FLOAT,
    GPA FLOAT,
    status bool DEFAULT true, 
    constraint pkey_transcripts PRIMARY KEY (id)   
);
SELECT * FROM transcripts;
INSERT INTO transcripts (Course, a, b, c, d, e, GPA) VALUES ('Javascript', 8, 8, 7, 9, 9, 10);
CREATE OR REPLACE FUNCTION calculate_gpa(a FLOAT, b FLOAT, c FLOAT, d FLOAT, e FLOAT)
  RETURNS FLOAT AS $$
BEGIN
  RETURN (a + b + c + d + e) / 5.0;
END;
$$ LANGUAGE plpgsql;
UPDATE transcripts
SET gpa = calculate_gpa(a , b, c, d, e);
UPDATE transcripts
SET status = true;