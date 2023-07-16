-- creates a view
-- need_meeting lists all students with score under 80 and no last meeting
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND
(last_meeting IS NULL OR DATEDIFF(CURDATE(), last_meeting) > 30);
