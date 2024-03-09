SELECT * FROM zillow_output
UNION DISTINCT
SELECT * FROM realtor_output;