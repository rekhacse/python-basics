a=[[0,0,0],[0,0,0],[0,0,0]]
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
 for j in range(3):
  a[i][j]=eval(input("Enter value:"))
  b[i][j]=eval(input("Enter value:"))
for i in range(3):
 for j in range(3):
  print(a[i][j],end=' ')
 print("\n")
for i in range(3):
 for j in range(3):
  print(b[i][j],end=' ')
 print("\n")
