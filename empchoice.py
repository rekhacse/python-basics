import os
os.system('cls')
import mysql.connector
cnx = mysql.connector.connect(user='root', database='student', password='rekha')
ch=""
while ch!="0":
    ch=input("\t\t+----------+\n\t\t| 0-exit   |\n\t\t| 1-display|\n\t\t| 2-clear  |\n\t\t| 3-insert |\n\t\t+----------+\nEnter your Option: ")
    if ch=="2":
        os.system('cls')
    elif ch=="1":
        cursor = cnx.cursor()
        query = ("SELECT * from employee")
        cursor.execute(query)
        print("+ {} + {} +".format("-"*10,"-"*20))
        print("| {:^10} | {:^20} |".format("empoyeeID", "empName"))
        print("+ {:<5} | {:>20} +".format("-"*10,"-"*20))
        for (e,n) in cursor:
            b=str(e)
            d=b.zfill(4)# zero fill
            print("| {:>10} | {:<20} |".format(d, n))
        print("+ {} + {} +".format("-"*10,"-"*20))
    elif ch=="3":
        eid=eval(input("Enter employee ID:"))
        name=input("Enter employee name:")
        cursor.execute("insert into employee(empoyeeID,empname)values({0},'{1}')".format(eid,name))
        cnx.commit()
cursor.close()
cnx.close()
