class methods:
    def __init__(self,Acct_details,cursor):
        self.cursor=cursor
        self.Acct=f"{Acct_details}"
    def show(self):
        query='SELECT * FROM ACCOUNT WHERE ACCOUNTNUMBER=\'' \
              f'{self.Acct}\''
        try:
            self.cursor.execute(query)
        except:
            return "No record found"
        result = self.cursor.fetchall()
        if(len(result)==0):
            return "No data found"
        i=result[0]
        ans="Account Number is {}\n" \
            "Balance {}\n Type {}\n" \
            "Status {}\n Aadhar Number {}\n" \
            "Branch Number {}".format(i[0],i[1],i[2],i[3],i[4],i[5])
        return ans
        pass
    def withdraw(self,Ammount):
        query = 'SELECT * FROM ACCOUNT WHERE ACCOUNTNUMBER=\'' \
                f'{self.Acct}\''
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        amt=result[0][1]
        if(Ammount>amt):
            return "Insufficient balance in the Account"
        else:
            query = 'UPDATE ACCOUNT ' \
                    f'SET BALANCE={amt-Ammount} WHERE ACCOUNTNUMBER=\'' \
                    f'{self.Acct}\''
            print(query)
            self.cursor.execute(query)
            return self.show()
        pass
    def pay(self,Aadhar,Loan_no,date):
        query='UPDATE PAYMENTS SET STATUS=\'Fully Paid\' WHERE AADHARNUMBER' \
              f'=\'{Aadhar}\' AND LOANNUMBER=\'{Loan_no}\' AND DATE=' \
              f'\'{date}\''
        print(query)
        self.cursor.execute(query)
        query = 'SELECT * FROM PAYMENTS WHERE AADHARNUMBER' \
                f'=\'{Aadhar}\' AND LOANNUMBER=\'{Loan_no}\' AND DATE=' \
                f'\'{date}\''
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        i=result[0]
        soln='Aadhar Number ={}\n' \
             'Loan Number ={}\n' \
             'Installment={}\n' \
             'Status={}\n' \
             ''.format(i[0],i[1],i[2],i[4])
        return soln
        pass
