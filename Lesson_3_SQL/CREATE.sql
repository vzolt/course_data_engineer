/* 1. Создать таблицу с основной информацией о сотрудниках: 
ФИО, дата рождения, дата начала работы, должность, 
уровень сотрудника (jun, middle, senior, lead), уровень зарплаты, 
идентификатор отдела, наличие/отсутствие прав(True/False). 
При этом в таблице обязательно должен быть уникальный номер для каждого сотрудника.*/

CREATE TABLE employees
(
    Id SERIAL PRIMARY KEY,
	FullName VARCHAR(100) NOT NULL,
	BirthDay DATE NOT NULL,
	StartDay DATE NOT NULL,
	JobTitle VARCHAR(50) NOT NULL,
	JobLevel VARCHAR(6),
	Salary NUMERIC (12,2),
	DepartmentId VARCHAR(10) NOT NULL,
	DriverLicense BOOLEAN
);

/* 2. Для будущих отчетов аналитики попросили вас создать еще одну таблицу 
с информацией по отделам – в таблице должен быть идентификатор для каждого отдела, 
название отдела (например. Бухгалтерский или IT отдел), 
ФИО руководителя и количество сотрудников. */

CREATE TABLE departments
(
    DepartmentId VARCHAR(10) NOT NULL UNIQUE,
	DepartmentName VARCHAR(80) NOT NULL,
	FullNameHead VARCHAR(100) NOT NULL,
	EmployeesNumber INT	
);

/* 3. На кону конец года и необходимо выплачивать сотрудникам премию. 
Премия будет выплачиваться по совокупным оценкам, которые сотрудники получают в каждом квартале года. 
Создайте таблицу, в которой для каждого сотрудника будут его оценки за каждый квартал. 
Диапазон оценок от A – самая высокая, до E – самая низкая. */

CREATE TABLE estimates
(
    Id INT NOT NULL UNIQUE,
	Year INT2 NOT NULL,
	Quarter INT2 NOT NULL,
	Еstimate CHAR(1) NOT NULL	
);