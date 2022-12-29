/* 6. Теперь пришла пора анализировать наши данные – напишите запросы для получения следующей информации:

-- 6.1 Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании */

SELECT id, FullName, StartDay
FROM employees;

-- 6.2 Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников

SELECT id, FullName, StartDay
FROM employees
LIMIT 3;

-- 6.3 Уникальный номер сотрудников - водителей

SELECT id
FROM employees
WHERE DriverLicense IS TRUE;

-- 6.4 Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E

SELECT id
FROM estimates
WHERE Еstimate ='D' OR Еstimate = 'E';

-- 6.5 Выведите самую высокую зарплату в компании

SELECT MAX(Salary) AS "Max salary"
FROM employees;