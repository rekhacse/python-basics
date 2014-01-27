class student:
     name=""
     mark=0
     def __init__(self,name,mark):
      self.name=name
      self.mark=mark
      print("constructor called")
     def display(self):
         print("Student name is {0} \n student mark is {1}".format(self.name,self.mark))
std=student('x',78)
std1=student('rekha',187)
std.display()
std1.display()
