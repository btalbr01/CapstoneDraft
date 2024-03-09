SELECT *
FROM (
    SELECT * FROM zillow_homes zh 
    UNION ALL
    SELECT * FROM realtor_homes rh 
) AS combined_tables
ORDER BY Price;

SELECT * FROM realtor_land;

SELECT *
FROM (
    SELECT * FROM zillow_land 
    UNION ALL
    SELECT * FROM realtor_land
) AS combined_tables
ORDER BY Price;

SELECT Address, Price, Area, Measurement
FROM zillow_homes
UNION ALL
SELECT Address, Price, Area, Measurement
FROM zillow_land;