CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name as name, s.size as size
  from dogs as d, sizes as s
  where d.height > s.min and d.height <= s.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT p.child
  from parents as p, dogs as d
  where d.name = p.parent
  order by d.height desc;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT s1.child as sib1, s2.child as sib2
  from parents as s1, parents as s2
  where s1.parent = s2.parent and s1.child < s2.child
  ;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sib.sib1 || " and " || sib.sib2 || " are " || s.size || " siblings"
  from siblings as sib, size_of_dogs as s, size_of_dogs as s2
  where sib.sib1 = s.name and sib.sib2 = s2.name and s.size = s2.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
-- Add your INSERT INTOs here

-- RECOMMENDED ANSWER (O(n^2))
-- INSERT INTO stacks_helper
--   SELECT name, height, height FROM dogs;

-- INSERT INTO stacks_helper
--   SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
--     FROM stacks_helper AS a, dogs AS b
--     WHERE a.last_height < b.height;

-- INSERT INTO stacks_helper
--   SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
--     FROM stacks_helper AS a, dogs AS b
--     WHERE a.last_height < b.height;

-- INSERT INTO stacks_helper
--   SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
--     FROM stacks_helper AS a, dogs AS b
--     WHERE a.last_height < b.height;

-- CREATE TABLE stacks AS
--   SELECT dogs, stack_height FROM stacks_helper
--     WHERE stack_height >= 170 ORDER BY stack_height;
  
-- MY ANSWER (O(n^4))
create table helper2 as
  select d1.name as n1,d2.name as n2,d3.name as n3,d4.name as n4, d1.height+d2.height+d3.height+d4.height as sum
  from dogs as d1,  dogs as d2,  dogs as d3,  dogs as d4
  where d1.height<d2.height and d2.height<d3.height and d3.height<d4.height and sum >= 170
  order by sum asc;

CREATE TABLE stacks AS
  SELECT n1||", "||n2||", "||n3||", "||n4, sum
  from helper2;
