import mysql.connector
def ret_cursor():

    return mycursor
'''
mydb = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='d3v@n$h123',
                                   auth_plugin='mysql_native_password',
                                   database='Bank')
mycursor = mydb.cursor()
mycursor.execute('select * from bankbranch')
result=mycursor.fetchall()
for i in result:
    print(i)
'''