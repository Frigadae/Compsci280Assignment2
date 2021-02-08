CREATE TABLE operator_table(
ID INTEGER NOT NULL AUTO_INCREMENT,
first_name TEXT,
last_name TEXT,
date_birth DATE,
license INTEGER,
endorsement BOOLEAN,
rescue_ops INTEGER,
PRIMARY KEY (ID)
);

CREATE TABLE drone_table( 
ID INTEGER NOT NULL AUTO_INCREMENT, 
name VARCHAR(50), 
class_type INTEGER, 
rescue_type BOOLEAN, 
operator_ID INTEGER,
PRIMARY KEY (ID),
FOREIGN KEY (operator_ID) REFERENCES operator_table (ID)
);