''' function objects that remember values in the enclosing scope even if they are not present in the memory'''
def outer():
    x= 3   #enclosing scope variable
    def inner():
        y=4
        result =  x + y
        return  result
    return inner

#inner()    / error
print(outer)
a = outer()
print(a)
print(a.__name__)
print(a())

