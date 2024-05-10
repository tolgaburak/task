/*

Code Implementation Task: If this list would be a database table, please provide SQL query to fill in the missing daily vaccination numbers with discrete median of country as similar to question a.  
Please  provide the link to your code as answer to this question. 
Note: This time SQL equivalent is requested, and imputation value is median of each country, not minimum. Please remember filling countries with zero if they do not have any valid daily_vaccination records like Kuwait.

*/


WITH MedianVaccinations AS (
    SELECT
        country,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS median_vaccinations
    FROM
        vaccination_data
    GROUP BY
        country
)
UPDATE
    vaccination_data AS vd
SET
    daily_vaccinations = COALESCE(vd.daily_vaccinations, mv.median_vaccinations, 0)
FROM
    MedianVaccinations AS mv
WHERE
    vd.country = mv.country;
