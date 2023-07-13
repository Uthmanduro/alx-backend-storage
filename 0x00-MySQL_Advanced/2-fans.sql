-- Script that ranks country origins by brands
-- imports an sql dump
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
