-- a SQL script that creates a trigger that resets the attribute valid_email only
-- when the email has been changed.


DELIMITER //

CREATE TRIGGER before_update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = NULL;
    END IF;
END;

//