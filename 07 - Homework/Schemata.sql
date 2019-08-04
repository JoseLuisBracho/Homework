CREATE TABLE "departments" (
  "dept_no" VarChar(4),
  "dept_name" VarChar(30),
  PRIMARY KEY ("dept_no")
);

CREATE TABLE "titles" (
  "emp_no" bigint,
  "title" VarChar(30),
  "from_date" date,
  "to_date" date
);

CREATE INDEX "FK" ON  "titles" ("emp_no");

CREATE TABLE "salaries" (
  "emp_no" bigint,
  "salary" decimal,
  "from_date" date,
  "to_date" date
);

CREATE INDEX "FK" ON  "salaries" ("emp_no");

CREATE TABLE "dept_emp" (
  "emp_no" bigint,
  "dept_no" VarChar(4),
  "from_date" date,
  "to_date" date
);

CREATE INDEX "FK" ON  "dept_emp" ("emp_no", "dept_no");

CREATE TABLE "employees" (
  "emp_no" bigint,
  "birth_date" date,
  "first_name" VarChar(30),
  "last_name" VarChar(30),
  "genre" VarChar(2),
  "hire_date" date,
  PRIMARY KEY ("emp_no")
);

CREATE TABLE "dept_manager" (
  "dept_no" VarChar(4),
  "emp_no" bigint,
  "from_date" date,
  "to_date" date
);

CREATE INDEX "FK" ON  "dept_manager" ("dept_no", "emp_no");