class Grandpa:                           #base class
    def display(self):
        print("I has a land")
        
class Father(Grandpa):                  #derived class 1
    def display(self):
        print("I has a Car")
        
class Child(Father):                    #derived class 2
    def display3(self):
        print("I has a bike")
        Father.display(self)
        self.display()
        super().display()
        print(self.__dict__)
obj=Child()
print(obj.__dict__)
obj.display3()

