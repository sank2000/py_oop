class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def msg(self):
        print(self.name + " got " + self.mark)
    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(mark)/600)*100))
    @staticmethod
    def check_age(age):
        if age > 17:
            print("Eigible")
        else:
            print("Not eligible")


s1 = Student("san","72")
mark = "500"
name ="vel"
#marks2=str((int(mark)/600)*100)
s2 = Student.get_per("vel","500")
s2.msg()
s2.check_age(19)