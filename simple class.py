class Person:
    def display(self):
        print("hi Class is created")


p1=Person()      #creating class object
p1.display()

print(Person)     #<class '__main__.Person'>
print(Person())   #<__main__.Person object at 0x7fd247fa5f28>
print(p1)         #<__main__.Person object at 0x7f2083fbbd68>



p2=Person()
p2.display()



print(Person)              #<class '__main__.Person'>
print(Person())            #<__main__.Person object at 0x7fe22416a7f0>
print(p2)                   #<__main__.Person object at 0x7fe2240f8e80>
