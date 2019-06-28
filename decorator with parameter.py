def outer(name):
    def sec_inner(fun):
        def inner():
            return fun() + name
        return inner
    return sec_inner


@outer("san")
def ordinary():
    return "good morning "


print(ordinary())