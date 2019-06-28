def str_upper(fun):
    def inner():
        str=fun()
        return str.upper()
    return inner
@str_upper
def print_str():
    return "good morning"

print(print_str())

#a = str_upper(print_str)
#print(a())                                          /instead of this we can use decorator