-- 2. Выполните следующие запросы: 

-- a. Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.
SELECT fullname
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- b. Попробуйте вывести фамилии сотрудников в алфавитном порядке

SELECT fullname
FROM employees
ORDER BY fullname;

-- c. Рассчитайте средний стаж для каждого уровня сотрудников

SELECT jobLevel,    
       AVG((DATE_PART('year', CURRENT_DATE::date) - DATE_PART('year', startday::date))*12 
	        + DATE_PART('month', CURRENT_DATE::date) - DATE_PART('month', startday::date)) AS average -- средний стаж в месяцах
FROM employees
GROUP BY joblevel;

-- d. Выведите фамилию сотрудника и название отдела, в котором он работает

SELECT e.fullname, d.departmentname
FROM employees AS e
JOIN departments AS d ON e.departmentid = d.departmentid;

-- e. Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.

WITH
i AS (SELECT d.departmentname, MAX(e.salary) AS maxsalary
FROM employees AS e
JOIN departments AS d ON e.departmentid = d.departmentid
GROUP BY d.departmentname),
e AS (SELECT e.fullname, d.departmentname, e.salary
FROM employees AS e
JOIN departments AS d ON e.departmentid = d.departmentid)

SELECT i.departmentname, e.fullname, i.maxsalary
FROM i LEFT OUTER JOIN e ON i.departmentname = e.departmentname
WHERE e.salary = i.maxsalary

