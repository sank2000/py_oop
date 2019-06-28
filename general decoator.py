def div_decorator(fun):
    def inner(*args):
        list1 =[]
        list1 = args[1:]
        for i in list1:
            if (i == 0):
                return  "Give a proper input!!!"
        return fun(*args)
    return inner

@div_decorator
def div1(a,b):
    return a/b


@div_decorator
def div2(a,b,c):
    return a/b/c


print(div1(3,0))

print(div2(9,0,3))