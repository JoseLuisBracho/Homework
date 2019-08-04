SELECT * FROM departments

SELECT * FROM dept_emp

SELECT * FROM dept_manager

SELECT * FROM employees

SELECT * FROM salaries

SELECT * FROM titles

-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT e.emp_no, e.last_name, e.first_name, e.genre, s.salary
FROM employees e, salaries s
WHERE e.emp_no = s.emp_no;

-- 2. List employees who were hired in 1986.

SELECT emp_no, last_name, first_name, hire_date
FROM employees
WHERE hire_date > '1985-12-31' AND
      hire_date < '1987-01-01';

-- 3. List the manager of each department with the following information: department number, department name, 
--    the manager's employee number, last name, first name, and start and end employment dates.

SELECT d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
FROM departments d, employees e, dept_manager dm
WHERE d.dept_no = dm.dept_no AND
      e.emp_no = dm.emp_no;


-- 4. List the department of each employee with the following information: employee number, last name, 
--    first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e, dept_emp de, departments d
WHERE e.emp_no = de.emp_no AND
      d.dept_no = de.dept_no;

--- 5. List all employees whose first name is "Hercules" and last names begin with "B."

SELECT emp_no, last_name, first_name
FROM employees
WHERE first_name = 'Hercules' AND
      last_name like 'B%';

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e, dept_emp de, departments d
WHERE e.emp_no = de.emp_no AND
      d.dept_no = de.dept_no
GROUP BY e.emp_no, d.dept_name
HAVING d.dept_name = 'Sales';


-- 7. List all employees in the Sales and Development departments, including their employee number, 
--    last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e, dept_emp de, departments d
WHERE e.emp_no = de.emp_no AND
      d.dept_no = de.dept_no
GROUP BY e.emp_no, d.dept_name
HAVING d.dept_name = 'Sales'
UNION
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e, dept_emp de, departments d
WHERE e.emp_no = de.emp_no AND
      d.dept_no = de.dept_no
GROUP BY e.emp_no, d.dept_name
HAVING d.dept_name = 'Development';

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT last_name, count(last_name) as same_lastName
FROM employees
GROUP BY last_name
ORDER BY same_lastName DESC;

-- Employee number 

SELECT emp_no, last_name, first_name
FROM employees
WHERE emp_no = 499942
