import functools
def outer(fun):
    @functools.wraps(fun)                               # without this name gives inner now the output is greet
    def inner():
        str = fun()
        return str.upper()
    return inner

@outer
def greet():
    return "good morning"


print(greet())
print(greet.__name__)