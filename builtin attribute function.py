class Person:
    def __init__(self,mark):
        self.mark = mark
    def display(self):
        print("hi Class is created")


p1=Person(20)      #creating class object
p1.display()
print(getattr(p1,"mark"))
print(p1.mark)

setattr(p1,"name","san")
print(p1.name)


delattr(p1,"name")

print(hasattr(p1,"name"))