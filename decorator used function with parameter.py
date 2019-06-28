def div_decorator(fun):
    def inner(x,y):
        if y==0:
            return "give proper input"
        return  fun(x,y)
    return inner

@div_decorator
def div(a,b):
    return  a/b



print(div(4,0))