#definition of method can be overwritten 
class A:
    def display(self):
        print("This method belongs to Class A")
class B(A):
     def display(self):
        print("This method belongs to Class b")


c1=B()
c1.display()
