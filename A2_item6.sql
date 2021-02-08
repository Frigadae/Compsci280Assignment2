/* Queries for operator table */

INSERT INTO operator_table(first_name, last_name, date_birth, license, endorsement, rescue_ops)
VALUES (
"Charlie",
"Brown",
'1999-9-12',
0,
FALSE,
0
);

INSERT INTO operator_table(first_name, last_name, date_birth, license, endorsement, rescue_ops)
VALUES (
"Bart",
"Simpson",
'2003-12-23',
1,
FALSE,
0
);

INSERT INTO operator_table(first_name, last_name, date_birth, license, endorsement, rescue_ops)
VALUES (
"Carl",
"Junior",
'1987-7-14',
2,
FALSE,
0
);

INSERT INTO operator_table(first_name, last_name, date_birth, license, endorsement, rescue_ops)
VALUES (
"Asriel",
"Dreemurr",
'1990-7-14',
2,
TRUE,
6
);

/* Queries for drone table */

INSERT INTO drone_table(name, class_type, rescue_type, operator_ID)
VALUES (
"Lunokhod",
"1",
FALSE,
NULL
);

INSERT INTO drone_table(name, class_type, rescue_type, operator_ID)
VALUES (
"Sojourner",
"2",
FALSE,
NULL
);

INSERT INTO drone_table(name, class_type, rescue_type, operator_ID)
VALUES (
"Curiosity",
"2",
TRUE,
NULL
);

INSERT INTO drone_table(name, class_type, rescue_type, operator_ID)
SELECT
"Mars 2020",
"1",
FALSE,
ID FROM operator_table WHERE first_name = "Bart" AND last_name = "Simpson"
;

INSERT INTO drone_table(name, class_type, rescue_type, operator_ID)
SELECT 
"ExoMars",
"2",
TRUE,
ID FROM operator_table WHERE first_name = "Asriel" AND last_name = "Dreemurr"
;
