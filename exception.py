try:
 c=234/0 # or put another expression to execute else part
except (ZeroDivisionError):
 print("Divided by zero")
else:
 print("No Error")
finally: 
 print("program executed")
