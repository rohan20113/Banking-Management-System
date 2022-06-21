#CREATING BASIC TABLES STRUCTURES
create table ACCOUNT (
	AccountNumber VARCHAR(50),
	Balance VARCHAR(50),
	Type VARCHAR(13),
	Status VARCHAR(7),
	AadharNumber  VARCHAR(14),
	BranchNumber VARCHAR(3)
);
create table BANKBRANCH (
	BranchNumber INT,
	OfficeNumber VARCHAR(50),
	City VARCHAR(50)
);
create table CUSTOMER (
	AadharNumber VARCHAR(50),
	PhoneNumber VARCHAR(50),
	DateofBirth DATE,
	Name VARCHAR(50),
	HouseNumber VARCHAR(50),
	City VARCHAR(50)
);

create table Department (
	DepartmentNumber INT,
	DepartmentName VARCHAR(28),
	Branch_Number INT
);

create table EMPLOYEE (
	EmployeeID VARCHAR(50),
	EmployeeName VARCHAR(50),
	Salary VARCHAR(50),
	DateofJoining DATE,
	MobileNumber VARCHAR(50),
	HouseNo VARCHAR(50),
	City VARCHAR(50),
	BranchNumber INT,
	DepartmentNumber INT
);
create table MANAGES(
	BranchNumber INT,
    EmployeeID VARCHAR(50),
	DateOfAppointment date,
    PRIMARY KEY (EmployeeID)
);
create table LOAN (
	LoanNumber VARCHAR(50),
	Amount INT,
	Interest INT,
	Type VARCHAR(11),
	AadharNumber VARCHAR(14),
	BranchNumber INT,
	Status VARCHAR(17)
);
create table ACCOUNT (
	AccountNumber VARCHAR(50),
	Balance INT,
	Type VARCHAR(14),
	Status VARCHAR(7),
	AadharNumber VARCHAR(14),
	BranchNumber INT
);
create table PAYMENTS(
	AadharNumber VARCHAR(14),
    LoanNumber VARCHAR(50),
    Date DATE,
    Installment INT,
    Status VARCHAR(50)
);
SELECT * FROM PAYMENTS;