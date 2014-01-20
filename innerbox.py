for i in range(7):
 for j in range(7):
  if(i==6 or j==6 or i==0 or j==0 ):
   print(" *",end='')
  elif((i==2 or i==4 ) & (j==2 or j==3 or j==4)):
    print(" *",end='')
  elif((i==3) & (j==2 or j==4)):
    print(" *",end='')
  else:
   print("  ",end='')
 print()


