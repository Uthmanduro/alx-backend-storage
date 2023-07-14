-- creates a stored procedure
-- AddBonus that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT,
                          IN project_name VARCHAR(255),
                          IN score INT)
BEGIN
    DECLARE projectID INT DEFAULT 0;

    SELECT id INTO projectID
    FROM projects
    WHERE name = project_name;

    IF projectID = 0 THEN
        INSERT INTO projects (name)
        VALUES (project_name);

        SET projectID = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, projectID, score);
END$$
DELIMITER ;                        
