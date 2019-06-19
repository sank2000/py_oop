class Person:
    def __init__(self,name):
        self.nme=name                  #instance variable
        name="san"                     #local variable
        print(name)
    def display(self):
        print("hello "+self.nme)
p1=Person("santhosh")
p1.display()
        
