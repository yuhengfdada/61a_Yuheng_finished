.read fa17data.sql
.read sp18data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT seven, denero from students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT time, smallest from students
  where smallest > 15
  order by smallest
  limit 20;

-- Q4
CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color
  from students as first, students as second
  where first.time < second.time and first.pet = second.pet and first.song = second.song
  ;
