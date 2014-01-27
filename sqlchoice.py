import os
os.system('cls')
import mysql.connector
cnx = mysql.connector.connect(user='root', database='student', password='rekha')
ch=""
while ch!="0":
    ch=input("Enter Option 1 to display 0 to stop 2 to clear: ")
    if ch=="2":
        os.system('cls')
    elif ch=="1":
        cursor = cnx.cursor()
        query = ("SELECT * from employee")
        cursor.execute(query)
        print("+ {} + {} +".format("-"*10,"-"*20))
        print("| {:^10} | {:^20} |".format("employeeID", "EmployeeName"))
        print("+ {:<5} | {:>20} +".format("-"*10,"-"*20))
        for (e,n) in cursor:
            b=str(e)
            d=b.zfill(4)
            print("| {:>10} | {:<20} |".format(d, n))
        print("+ {} + {} +".format("-"*10,"-"*20))
cursor.close()
cnx.close()
#print("{2:d10}".format(10))
