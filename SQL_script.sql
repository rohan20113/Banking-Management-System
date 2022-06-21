use Bank;
#1)List the average salary of all the departments.
SELECT DepartmentNumber,
avg(Salary) OVER (PARTITION BY DepartmentNumber) AS AVG_Salary
FROM EMPLOYEE;
#2)Write an SQL query to list the employees that are also managers.
SELECT E.Employeename from Employee as E,Manages as M WHERE(E.EmployeeID=M.EmployeeID) ;  
#3)Return details of the employee with the nth highest salary.
#you can put N as any number while writing the query(For example-4,5,6,etc)
SELECT EmployeeName,Salary 
From (SELECT EmployeeName,Salary,DENSE_RANK() over (ORDER by Salary desc) as rk FROM EMPLOYEE) as a where rk=n;
#4)List all Active Loans by Price and Interest
SELECT C.Name,L.AadharNumber,L.Amount,L.Interest,L.Status,L.Type 
FROM LOAN AS L,CUSTOMER AS C WHERE C.AadharNumber=L.AadharNumber AND 
L.Status!="Fully Paid" AND L.Status!="Grace" 
ORDER BY Amount,Interest DESC;
#5)List Account Numbers,Aadhar Number and Loan amount of people who have taken a loan of amount 1cr and more and have 10cr or less in their accounts.
SELECT A.AadharNumber,A.AccountNumber,L.amount 
from ACCOUNT as A,LOAN as L where (A.AadharNumber=L.AadharNumber 
AND A.Balance<=100000000 AND L.amount>=10000000);
#6)Create an Account view for all active accounts in bank
CREATE VIEW all_accounts AS (SELECT * FROM ACCOUNT WHERE Status!="Closed");
SELECT * FROM all_accounts;
#7)List all persons having more than 1 account 
SELECT C.Name, C.AadharNumber,Count(C.AadharNumber) FROM customer as C
INNER JOIN Account as A ON C.AadharNumber = A.AadharNumber GROUP BY C.AadharNumber HAVING COUNT(*) > 1 ORDER BY Count(C.AadharNumber) DESC;
#8)List names for persons by which they pay the installment earliest
SELECT C.Name,C.AadharNumber,L.LoanNumber,L.Amount,P.Installment,P.DATE FROM 
CUSTOMER AS C,LOAN AS L, PAYMENTS AS P WHERE 
C.AadharNumber=P.AadharNumber AND P.LoanNumber=L.LoanNumber AND L.LoanNumber=P.LoanNumber
ORDER BY P.DATE,P.Installment ASC;
#9)Close all accounts owned by 2788-4810-0143
UPDATE ACCOUNT SET Status='Closed' WHERE AadharNumber='2788-4810-0143';
#10)List the branch ids with their most dominant loan types
SELECT BranchNumber,MAX(Type) FROM LOAN GROUP BY BranchNumber;

