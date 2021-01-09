.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT first.date, first.color, first.pet, first.number, second.number
  from students as first, fa17students as second
  where first.pet = second.pet and first.date = second.date and first.color = second.color
  ;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven
  from students as a, checkboxes as b 
  where a.number = 7 and b."7" = "True" and a.time = b.time
  ;

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, count(*) as count
  from fa17students
  group by number
  order by count desc 
  limit 1 
  ;


CREATE TABLE fa17favpets AS
  SELECT pet, count(*) as count
  from fa17students
  group by pet
  order by count desc, pet asc
  limit 10
  ;


CREATE TABLE sp18favpets AS
  SELECT pet, count(*) as count
  from students
  group by pet
  order by count desc, pet asc
  limit 10
  ;


CREATE TABLE sp18dog AS
  SELECT pet, count(*) as count
  from students
  where pet = "dog"
  group by pet;


CREATE TABLE sp18alldogs AS
  SELECT pet, count(*) as count
  from students
  where pet like "%dog%"
  group by "dog";


CREATE TABLE obedienceimages AS
  SELECT seven, denero, count(*) as count
  from students
  where seven = '7'
  group by denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*) as count
  from students
  group by smallest
  order by smallest asc 
  ;
