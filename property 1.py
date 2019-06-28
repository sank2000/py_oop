class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    #   self.msg=self.name + " has got a grade " + self.grade
    @property
    def msg(self):
        return self.name + " has got a grade " + self.grade
s1=Student("san",'b')
print(s1.msg)
s1.name="santhosh"
print(s1.msg)