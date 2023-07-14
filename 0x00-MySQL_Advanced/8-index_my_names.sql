-- creates an index
-- idx_name_first on table names 
CREATE INDEX idx_name_first ON names(SUBSTRING(name, 1, 1));
