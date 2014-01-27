import mysql.connector
rno=eval(input("Enter the regno:"))
name=input("Enter the student name:")
mark=eval(input("Enter the mark:"))
result=input("Enter the result:")
cn=mysql.connector.connect(user='root', database='student',password='rekha')
cr=cn.cursor()#cursor is the adapter
cr.execute("insert into mark(regno,sname,mark,result)values({0},'{1}',{2},'{3}')".format(rno,name,mark,result))
cn.commit()
print("record inserted")
cr.close()
cn.close()
cn=mysql.connector.connect(user='root', database='student',password='rekha')
cr=cn.cursor()
cr.execute("select * from mark")
for(r,n,m,rs) in cr:
 print("---------+------------+-----------+----------+")
 print("{0:<5}|{1:^20}|{2:<5}|{3:>10}|".format(r,n,m,rs))#width >right align ^center align
 print("---------+------------+-----------+----------+")
cr.close()
cn.close()
