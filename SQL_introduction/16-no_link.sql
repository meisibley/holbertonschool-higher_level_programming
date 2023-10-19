-- lists all records of second_table of hbtn_0c_0 in MySQL
-- Don't list rows without a name value, results: score, name and score DESC
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
