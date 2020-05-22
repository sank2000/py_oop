"""
    CLASS WITH MORE METHODS [PART 2]
        Author: KrishnaMoorthy12

"""

class Employee:
    def __init__(self, first, last, num, pay):
        self.fname = first
        self.lname = last
        self.number = num
        self.NetPay = pay

    def fullname(self):
        return self.fname + ' ' + self.lname

    def PayDetails(self):
        self.basic = 0.85 * self.NetPay
        self.insurance = 0.4 * self.NetPay
        self.attBonus = 0.3 * self.NetPay
        self.allow = 0.6 * self.NetPay
        self.deduc = 0.2 * self.NetPay

emp1 = Employee('Gary', 'Mayhem', 2001, 85000)
emp2 = Employee('Arnold', 'Schwerzeneger', 2002, 78000)

print('======= Employee Details =======')
print('Name             :', emp1.fullname())
print('Employee Number  :', emp1.number)

try:
    #without calling PayDetails fn.
    print('Basic Pay    :', emp1.basic)
    print('Insurance    :', emp1.insurance)
    print('Attendace    :', emp1.attBonus)
    print('Allowance    :', emp1.allow)
    print('Deductions   :', emp1.deduc)

except Exception as wtf:
    print('wtf! Error occured:', wtf)

    #callinf PayDetails for emp2
    emp2.PayDetails()
    print('======= Employee Details =======')
    print('Name             :', emp2.fullname())
    print('Employee Number  :', emp2.number)
    print('Basic Pay        :', emp2.basic)
    print('Insurance        :', emp2.insurance)
    print('Attendace        :', emp2.attBonus)
    print('Allowance        :', emp2.allow)
    print('Deductions       :', emp2.deduc)
