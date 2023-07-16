-- creates a stored procedure
-- ComputeAverageWeightedScoreForUser computes and stores the average weighted scores
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id  INT)
BEGIN
    DECLARE weighted_average INT;
    SELECT SUM(score * weight) / SUM(weight) INTO weighted_average 
    FROM corrections 
    RIGHT JOIN projects ON corrections.project_id = projects.id 
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = weighted_average
    WHERE id = user_id;
END$$
DELIMITER ;
