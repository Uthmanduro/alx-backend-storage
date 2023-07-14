-- creates a stored procedure
-- ComputeAverageScoreForUser that computes & store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id FLOAT)
BEGIN
    DECLARE scores FLOAT DEFAULT 0;

    SELECT AVG(score) INTO scores
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = scores
    WHERE id = user_id;
END$$
DELIMITER ;
