class Student:
    clg="xyz"                          #class variable
    def __init__(self,rno,name):
        self.name=name
        self.rollno=rno

    def display(self):
        print("\nName   :",self.name)
        print("Roll no:",self.rollno)
        print("Clg    :",self.clg)

s1 = Student("12345","san")
s1.display()
s2 = Student("12346","vel")
s2.display()

try:
    s2.clg = 'AUBIT'
    print('clg: ', s2.clg)

except Exception as e:
    print('Error occured!', e)
