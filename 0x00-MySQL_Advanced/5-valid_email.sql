-- creates a trigger
-- resets the attrinute valid_email when the email is changed
DELIMITER $$
CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = (OLD.email = NEW.email);
    END IF;
END$$
DELIMITER ;
