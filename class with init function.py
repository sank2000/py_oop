class Person:
    def __init__(self,num):
        self.number=num
        print("The constructor is successfully worked\n")
    def display(self):
        print("The value in number is",self.number)
        
p1=Person(10)
p1.display()
