/* Returns a user by their first and last name */

SELECT * FROM operator_table
WHERE first_name = "Asriel" AND last_name = "Dreemurr";

/* Returns operator_table in ascending order by last, first names */

SELECT * FROM operator_table
ORDER BY last_name, first_name ASC;

/* Returns entries showing drones with an operator */

SELECT * FROM drone_table
WHERE operator_ID IS NOT NULL;

/* Returns entries showing drones without an operator */

SELECT * FROM drone_table
WHERE operator_ID IS NULL;

/* Returns all drones in drone_table including with and without operators */

SELECT drone_table.*, CONCAT(operator_table.first_name, ' ', operator_table.last_name) As name
FROM drone_table LEFT JOIN operator_table ON drone_table.operator_ID = operator_table.ID