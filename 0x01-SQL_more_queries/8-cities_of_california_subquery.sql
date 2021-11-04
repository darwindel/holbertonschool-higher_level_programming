-- list cities in cali
SELECT id, name FROM cities WHERE state_id IS (
    SELECT id FROM states WHERE name LIKE 'California'
    )
ORDER BY id ASC;
