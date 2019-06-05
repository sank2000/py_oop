"""
    CLASS - EMPLOYEE DATABASE MANAGEMENT
        Author: KrishnaMoorthy12

"""

class Employee:
    increment = 1.05
    no_emps = 0

    @classmethod
    def create(cls, string):
        first, last, pay = string.split('-')
        pay = int(pay)
        return cls(first, last, pay)

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.number = 2000 + Employee.no_emps + 1
        self.NetPay = pay
        Employee.no_emps += 1

    def fullname(self):
        return self.fname + ' ' + self.lname

    def PayDetails(self):
        self.basic = 0.85 * self.NetPay
        self.insurance = 0.4 * self.NetPay
        self.attBonus = 0.3 * self.NetPay
        self.allow = 0.6 * self.NetPay
        self.deduc = 0.2 * self.NetPay

    def PrintDetails(self):
        self.PayDetails()
        print('========== Employee Details ==========')
        print('Name             :', self.fullname())
        print('Employee Number  :', self.number)
        print('Basic Pay        : $', self.basic)
        print('Insurance        : $', self.insurance)
        print('Attendace        : $', self.attBonus)
        print('Allowance        : $', self.allow)
        print('Deductions       : $', self.deduc)
        print('increment %      : {} %'.format(self.increment))
        print()

    def apply_raise(self):
        self.NetPay *= self.increment
        self.PayDetails()

    def change_inc_perc(self, new):
        self.increment = new

    @staticmethod
    def is_workday(date):
        if date == 5 or date == 6:
            return False
        return True

emp1 = Employee('Gary', 'Mayhem', 85000)
emp2 = Employee('Arnold', 'Schwerzeneger', 78000)
emp3 = Employee.create('John-Smith-56000')

emp1.PrintDetails()
emp2.PrintDetails()
emp3.PrintDetails()

emp1.change_inc_perc(1.08)
emp1.PrintDetails()

emp3.apply_raise()
emp3.PrintDetails()

import datetime
day = datetime.date(2019, 12, 15)
print(Employee.is_workday(day))
