"""
   composition is  part_of
   
"""
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_pay(self):
        return self.pay+self.bonus
class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay,bonus)
        
    def totalsalary(self):
        return  self.obj_salary.annual_pay()

emp = Employee("san",18,1200,100)
print(emp.totalsalary())
print(emp.name)
print(emp.obj_salary.pay)
