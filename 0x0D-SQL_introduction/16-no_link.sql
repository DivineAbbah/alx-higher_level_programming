-- script to lists all records of the tbl 


SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
