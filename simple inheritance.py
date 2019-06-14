class Animal:                      #parent class
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def eat(self):
        print("Eating")
class Display(Animal):               #child class
    def display(self):
        print("Name:",self.name)
        print("Colour:",self.colour)
dog=Display("Dog","Brown")
dog.display()
dog.eat()

cat=Display("Cat","Black")
cat.display()
dog.eat()
