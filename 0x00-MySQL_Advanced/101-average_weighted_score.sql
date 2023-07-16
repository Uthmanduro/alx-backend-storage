-- creates a stored procedure
-- computes and stores the average weighted score for all students 
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM corrections
        RIGHT JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id);
END$$
DELIMITER ;
