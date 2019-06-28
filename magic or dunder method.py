class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.pay = salary
    def __len__(self):
        return len(self.name)
    def __add__(self, other):
        return self.pay+other.pay

e1 = Employee("san",10000)
print(len(e1))
e2 = Employee("vel",20000)
print(len(e2))
print(e1+e2)
print(e1.__add__(e2))