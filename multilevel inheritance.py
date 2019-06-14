class Grandpa:                           #base class
    def display1(self):
        print("I has a land")
        
class Father(Grandpa):                  #derived class 1
    def display2(self):
        print("I has a Car")
        
class Child(Father):                    #derived class 2
    def display3(self):
        print("I has a bike")


obj=Child()
obj.display1()
obj.display2()
obj.display3()
