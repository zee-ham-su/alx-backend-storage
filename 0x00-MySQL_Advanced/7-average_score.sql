-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and
-- store the average score for a student. Note: An average score can be a decimal

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN userId INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = userId)
    WHERE id = userId;
END$$
DELIMITER ;
