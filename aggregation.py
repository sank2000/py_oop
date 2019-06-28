"""
   aggregation  is  Has-A
   
"""
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_pay(self):
        return self.pay+self.bonus
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.obj_salary=salary
        
    def totalsalary(self):
        return  self.obj_salary.annual_pay()
salary = Salary(1200,100)
emp = Employee("san",18,salary)
print(emp.totalsalary())
print(emp.name)
print(emp.obj_salary.pay)
