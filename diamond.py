a=int(input("Enter a number:"))
for i in range(a):
 for j in range(i,a):
  print(" ",end='')
 for k in range(i):
  print(" *",end='')
 print()
for i in range(a):
 for j in range(i):
  print(" ",end='')
 for k in range(i,a):
  print(" *",end='')
 print()
