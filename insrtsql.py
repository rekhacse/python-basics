import mysql.connector
cn=mysql.connector.connect(user='root', database='student',password='rekha')
cr=cn.cursor()#cursor is the adapter
cr.execute("insert into mark(regno,sname,mark,result)values({0},'{1}',{2},'{3}')".format(1,'sam',90,'pass'))
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
