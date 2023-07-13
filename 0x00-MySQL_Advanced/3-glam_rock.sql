-- scripts that list all bands
-- with glam rock as their main style
SELECT band_name, (ifnull(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan DESC;
