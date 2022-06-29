import mysql.connector
from Show import methods
from tkinter import *
from PIL import Image,ImageTk
from sql_connect import ret_cursor
def Show(event,root,mycursor):
    children=root.winfo_children()
    print(len(children))
    for i in range(6,len(children)):
        children[i].destroy()
    def show(event1):
        obj=methods(account.get(),mycursor)
        label1=Label(root,text=obj.show(),font=('Helvetica bold',15))
        label1.place(x=500,y=400)
    account=StringVar()
    label=Label(root,text="Enter Account No",font=('Helvetica bold',15))
    label.place(x=100,y=400)
    input=Entry(root,textvariable=account)
    input.place(x=300,y=400)
    but=Button(root,text='Enter')
    but.place(x=300,y=450)
    but.bind('<Button-1>',show)
def Withdraw(event,root,mycursor):
    children = root.winfo_children()
    print(len(children))
    for i in range(6, len(children)):
        children[i].destroy()
    def withdraw(event1):
        obj=methods(account.get(),mycursor)
        ans=obj.withdraw(ammount.get())
        label1 = Label(root, text=ans, font=('Helvetica bold', 15))
        label1.place(x=500, y=400)
        pass
    account = StringVar()
    ammount=IntVar()
    label = Label(root, text="Enter Account No", font=('Helvetica bold', 15))
    label.place(x=100, y=400)
    label2=Label(root,text='Enter Ammount',font=('Helvetica bold', 15))
    label2.place(x=100,y=450)
    input = Entry(root, textvariable=account)
    input.place(x=300, y=400)
    input2=Entry(root,textvariable=ammount)
    input2.place(x=300,y=450)
    but = Button(root, text='Enter')
    but.place(x=300, y=500)
    but.bind('<Button-1>', withdraw)
def Payment(event,root,mycursor):
    children = root.winfo_children()
    print(len(children))
    for i in range(6, len(children)):
        children[i].destroy()
    def pay(event1):
        obj = methods("", mycursor)
        ans=obj.pay(Aadhar.get(),Loan.get(),date.get())
        label1 = Label(root, text=ans, font=('Helvetica bold', 15))
        label1.place(x=500,y=400)
    label = Label(root, text="Enter Aadhar No", font=('Helvetica bold', 15))
    label.place(x=100, y=400)

    label2 = Label(root, text="Enter Loan No", font=('Helvetica bold', 15))
    label2.place(x=100, y=450)

    label3 = Label(root, text="Enter Date", font=('Helvetica bold', 15))
    label3.place(x=100, y=500)

    Aadhar=StringVar()
    Loan=StringVar()
    date=StringVar()

    input = Entry(root, textvariable=Aadhar)
    input.place(x=300, y=400)

    input2 = Entry(root, textvariable=Loan)
    input2.place(x=300, y=450)

    input3 = Entry(root, textvariable=date)
    input3.place(x=300, y=500)

    but = Button(root, text='Enter')
    but.place(x=300, y=550)
    but.bind('<Button-1>', pay)
    pass
def Transfer(event,root,mycursor):
    children=root.winfo_children()
    for i in range(6,len(children)):
        children[i].destroy()
    def transfer(event1):
        obj=methods(Acc1.get(),mycursor)
        ans=obj.withdraw(amt.get())
        if ans=="Insufficient balance in the Account":
            label=Label(root,text=ans,font=('Helvetica bold',15))
            label.place(x=600,y=400)
            return
        else:
            obj2=methods(Acc2.get(),mycursor)
            ans2=obj2.withdraw(-amt.get())
            ans+='\n'
            ans+=ans2
            label=Label(root,text=ans,font=('Helvetica bold',15))
            label.place(x=600,y=400)
            return
    label1=Label(root,text="From(Account No)",font=('Helvetica bold',15))
    label1.place(x=100,y=400)
    label2=Label(root,text="To(Account No)",font=('Helvetica bold',15))
    label2.place(x=100,y=450)
    label3 = Label(root, text="Amount", font=('Helvetica bold', 15))
    label3.place(x=100,y=500)
    Acc1=StringVar()
    Acc2=StringVar()
    amt=IntVar()
    inp1=Entry(root,textvariable=Acc1)
    inp2=Entry(root,textvariable=Acc2)
    inp3=Entry(root,textvariable=amt)
    inp1.place(x=300,y=400)
    inp2.place(x=300,y=450)
    inp3.place(x=300,y=500)
    b1=Button(root,text='Enter')
    b1.place(x=300,y=550)
    b1.bind('<Button-1>',transfer)
def q1():
    #Original query
    """SELECT D.DepartmentNumber,avg(E.Salary) as average_salary from Employee as E, " \
           "Department as D where(E.DepartmentNumber=D.DepartmentNumber) " \
           "Group by DepartmentNumber Order by DepartmentNumber"""
    #Optimized query
    return "SELECT DepartmentNumber,avg(Salary) OVER (PARTITION BY " \
           "DepartmentNumber) AS AVG_Salary FROM EMPLOYEE;"
def q2():
    return "SELECT E.Employeename from Employee as E,Manages as M WHERE(E.EmployeeID=M.EmployeeID)"
def q3():
    ''' Original query
    SELECT EmployeeName,Salary From EMPLOYEE as e1 " \
           "where 4 = (SELECT COUNT(DISTINCT salary) " \
           "FROM Employee as e2 where(e2.Salary>e1.Salary));'''
    #Optimized query
    return "SELECT EmployeeName,Salary From " \
           "(SELECT EmployeeName,Salary, DENSE_RANK() over " \
           "(ORDER by Salary desc) as rk FROM EMPLOYEE) as a where rk=4"
def q4():
    return "SELECT C.Name,L.AadharNumber,L.Amount,L.Interest,L.Status,L.Type  " \
           "FROM LOAN AS L,CUSTOMER AS C WHERE " \
           "C.AadharNumber=L.AadharNumber AND  " \
           "L.Status!=\"Fully Paid\" AND L.Status!=\"Grace\" " \
           "ORDER BY Amount,Interest DESC"
def q5():
    return "SELECT A.AadharNumber,A.AccountNumber,L.amount " \
           "from ACCOUNT as A,LOAN as L where (A.AadharNumber=L.AadharNumber AND " \
           "A.Balance<=100000000 AND L.amount>=10000000);"
def q6():
    return "SELECT * FROM all_accounts"
def q7():
    return "SELECT C.Name, C.AadharNumber,Count(C.AadharNumber) FROM customer as C INNER JOIN " \
           "Account as A ON C.AadharNumber = A.AadharNumber GROUP BY " \
           "C.AadharNumber HAVING COUNT(*) > 1 ORDER BY Count(C.AadharNumber) " \
           "DESC;"
def q8():
    return "SELECT C.Name,C.AadharNumber,L.LoanNumber,L.Amount,P.Installment," \
           "P.DATE FROM CUSTOMER AS C,LOAN AS L, PAYMENTS AS P " \
           "WHERE C.AadharNumber=P.AadharNumber AND P.LoanNumber=L.LoanNumber " \
           "AND L.LoanNumber=P.LoanNumber ORDER BY P.DATE,P.Installment ASC; "
def q9():
    return "UPDATE ACCOUNT SET Status='Closed' WHERE AadharNumber='2788-4810-0143'"
def q10():
    return "SELECT BranchNumber,MAX(Type) FROM LOAN GROUP BY BranchNumber"
def execute(event,root,mycursor):
    children=root.winfo_children()
    for i in range(1,len(children)):
        children[i].destroy()
    lbl=Label(root,text='Enter which no',font=('Helvetica bold',15))
    lbl.place(x=100,y=50)
    inp=IntVar()
    en=Entry(root,textvariable=inp)
    en.place(x=300,y=50)
    def ex(event):
        children=root.winfo_children()
        for i in range(4,len(children)):
            children[i].destroy()
        x=inp.get()
        soln = ""
        q = ""
        if (x == 1):
            l2=Label(root,text='Average salary for all departments',
                     font=('Helvetica bold',12))
            l2.place(x=100,y=80)
            q = q1()
        elif x == 2:
            l2 = Label(root, text='list of employees that are also managers.',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q2()
        elif x == 3:
            l2 = Label(root, text=' details of the employee with the nth highest salary.',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q3()
        elif x == 4:
            l2 = Label(root, text='all Active Loans by Price and Interest',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q4()
        elif x == 5:
            l2 = Label(root, text='Account Numbers,Aadhar Number and Loan amount of people who have taken a '
                                  'loan of amount 1cr and '
                                  'more and have 10cr or less in their accounts.',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q5()
        elif x == 6:
            l2 = Label(root, text='Account view for all active accounts in bank',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q6()
        elif x == 7:
            l2 = Label(root, text='all persons having more than 1 account ',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q7()
        elif x == 8:
            l2 = Label(root, text='names for persons by which they pay the installment earliest',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q8()
        elif x == 9:
            q = q9()
        else:
            l2 = Label(root, text='branch ids with their most dominant loan types',
                       font=('Helvetica bold', 12))
            l2.place(x=100, y=80)
            q = q10()
        mycursor.execute(q)
        result = mycursor.fetchall()
        vert=Scrollbar(root,orient='vertical')
        t=Text(root,width=100,height=50,
               yscrollcommand=vert.set)
        t.place(x=10,y=120)
        for i in range(0,len(result)):
            t.insert(END,str(result[i])+'\n')
    b1=Button(root,text='Enter')
    b1.place(x=450,y=50)
    b1.bind('<Button-1>',ex)
    pass
def aggregate(event,root,mycursor):
    children=root.winfo_children()
    for i in range(1,len(children)):
        children[i].destroy()
    query="SELECT EmployeeID,Salary, dense_rank() " \
          "over(order by Salary desc) as 'rank' " \
          "from EMPLOYEE order by 'rank'"
    mycursor.execute(query)
    result=mycursor.fetchall()
    ans="EmployeeId, Salary, rank\n"
    vert = Scrollbar(root, orient='vertical')
    t = Text(root, width=100, height=50,
             yscrollcommand=vert.set)
    t.place(x=10, y=120)
    t.insert(END,ans)
    for i in range(0, len(result)):
        ans=str(result[i])+'\n'
        t.insert(END, ans)
mydb = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='d3v@n$h123',
                                   auth_plugin='mysql_native_password',
                                   database='Bank')
mycursor = mydb.cursor()
root=Tk()
root.geometry('1000x1000')
photo=PhotoImage(file='back.png')
back=Label(root,image=photo)
back.place(x=0,y=0)
button1=Button(root,text='Show details',width=10,height=5)
button1.place(x=100,y=120)
button2=Button(root,text='Withdraw Money',width=12,height=5)
button2.place(x=300,y=120)
button3=Button(root,text='Pay Loan',width=10,height=5)
button3.place(x=700,y=120)
button6=Button(root,text='Transfer Money',width=12,height=5)
label1=Label(root,text='Welcome to General bank',font=('Helvetica bold',40))
label1.place(x=260,y=10)
button1.bind('<Button-1>',lambda event:Show(event,root,mycursor))
button2.bind('<Button-1>',lambda event:Withdraw(event,root,mycursor))
button3.bind('<Button-1>',lambda event:Payment(event,root,mycursor))
button6.bind('<Button-1>',lambda event:Transfer(event,root,mycursor))
button6.place(x=500,y=120)
button4=Button(root,text='Aggregate function',width=15,height=5)
button4.place(x=225,y=220)
button5=Button(root,text='SQL queries',width=12,height=5)
button5.place(x=625,y=220)
button4.bind('<Button-1>',lambda event:aggregate(event,root,mycursor))
button5.bind('<Button-1>',lambda event:execute(event,root,mycursor))
root.resizable(False,False)
root.mainloop()