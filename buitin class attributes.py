class Animal:
    '''Animal class'''
    def __init__(self,name,colour):                                     #parent class
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


print(Animal.__dict__)
print(Animal.__doc__)
print(Animal.__name__)
print(Animal.__module__)
print(Animal.__bases__)
print(Display.__bases__)
print(Display.__doc__)
