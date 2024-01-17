-- a SQL script that creates a trigger that resets the attribute valid_email only
-- when the email has been changed.


DELIMITER $$;

CREATE TRIGGER VALIDATE BEFORE
    UPDATE ON users FOR EACH ROW
BEGIN
    IF NEW.EMAIL != OLD.EMAIL THEN
        SET NEW.VALID_EMAIL = 0;
    END IF;
END;

$$ DELIMITER;