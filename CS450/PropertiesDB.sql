SELECT *
FROM (
    SELECT * FROM zillow_homes zh 
    UNION ALL
    SELECT * FROM realtor_homes rh 
) AS combined_tables
ORDER BY Price;