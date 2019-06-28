def upper(fun):
    def inner():
        str = fun()
        return str.upper()
    return inner


def split_(fun):
    def inner():
        str = fun()
        return str.split(" ")
    return inner

@split_                           #2 nd
@upper                            #1 st
def ordinary():
    return "good morning"


print(ordinary())