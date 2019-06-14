class Student:
    clg="xyz"                          #class variable
    def __init__(self,rno,name):
        self.name=name
        self.rollno=rno

    def display(self):
        print("\nName   :",self.name)
        print("Roll no:",self.rollno)
        print("Clg    :",Student.clg)

s1 = Student("12345","san")
s1.display()
s2 = Student("12346","vel")
s2.display()
