class Student:
    __counter=0
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        Student.__counter = Student.__counter + 1
    def msg(self):
        print(self.name + " got " + self.mark)
    @classmethod
    def count(cls):
        return cls.__counter
s1 = Student("san","72")
s2 = Student("sam", "92")
s3 = Student("vel", "82")
s1.msg()
print(Student.count())
print(s1.count())
