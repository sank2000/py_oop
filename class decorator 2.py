class Check_div:
    def __init__(self,fun):
        self.fun = fun
    def __call__(self, *args):
        list1=[]
        list1=args[1:]
        for i in list1:
            if i == 0:
                return "you cannot divide change the input!!"
        else:
            return self.fun(*args)

@Check_div
def div(a,b):
    return a/b

@Check_div
def div2(a,b,c):
    return a/b/c

print(div(3,3))
print(div2(9,0,3))