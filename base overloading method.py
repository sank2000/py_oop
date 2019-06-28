class Person:
    def __init__(self,mark):
        self.mark = mark
    def display(self):
        print("hi Class is created")
    def __repr__(self):
        return "{obj:san}"
    def __str__(self):
        return "san obj"   #if str is not present then  repr will be executed
    def __del__(self):
        print("visit again")


p1=Person(20)      #creating class object
p1.display()
print(p1)
print(str(p1))
print(repr(p1))