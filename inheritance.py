#python supports multiple inheritance, use comma
class student:
     name="rekha"
     mark=100
     def display(self):
        print("Student name is {0} \n student mark is {1}".format(self.name,self.mark))
class sport(student):
 game="running"
 rank=34
 def display(self):
  print("plays the game",self.game)
  print("rank",self.rank)
s=sport()
s.display()
#s.play()
#if parent  class and child class has same function name and if we call the function, the function in child class will be called. this is called method overloading.
