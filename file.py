f=open("C:/Python33/ag/temp.txt","r")#r- refers to read mode
str=f.read()
print(str)
print(f.name)
print(f.mode)
f.close()
print(f.closed)
