-- lists the number of records w/ same score in second_table of hbtn_0c_0
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
