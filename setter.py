 class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    #   self.msg=self.name + " has got a grade " + self.grade       /  it gives a error in msg
    @property
    def msg(self):
        return self.name + " has got a grade " + self.grade
    @msg.setter
    def msg(self,sen):
        temp=sen.split(" ")
        self.name=temp[0]
        self.grade=temp[-1]
s1=Student("san",'b')
print(s1.msg)
s1.msg="vel has got a grade a"
print(s1.name)
print(s1.grade)