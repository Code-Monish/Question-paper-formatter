CREATE TABLE employee (empid INTEGER NOT NULL PRIMARY KEY, empname TEXT NOT NULL, salary NOT NULL);
INSERT INTO employee(empid, empname, salary) VALUES(1, 'JAY', 12000);
INSERT INTO employee(empid, empname, salary) VALUES(2, 'KAVIN', 20000);

SELECT * FROM employee