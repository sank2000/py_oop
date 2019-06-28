def check_name(fun):
    def inner(name_ref):
        if name_ref.name == "san":
            print("Hey you entered the user name!!")
        else:
            fun(name_ref)
    return inner

class Printing:
    def __init__(self,name):
        self.name = name
    @check_name
    def print_name(self):
        print("enter user name is :",self.name)


p1=Printing("vel")
p1.print_name()