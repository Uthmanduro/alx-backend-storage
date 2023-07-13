-- Script that ranks country origins by brands
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin;
