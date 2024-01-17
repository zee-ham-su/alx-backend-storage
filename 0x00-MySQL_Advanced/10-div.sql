-- a SQL script that creates a function SafeDiv that divides (and returns) the first by the second
-- number or returns 0 if the second number is equal to 0.

DELIMITER $$;

CREATE FUNCTION SAFEDIV(A INT, B INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE
        RESULT FLOAT;
        IF     B = 0 THEN
            RETURN 0;
        END IF;
        SET    RESULT = (A * 1.0) / B;
        RETURN RESULT;
END; $$
DELIMITER;