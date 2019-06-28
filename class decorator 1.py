class Decorator:
    def __init__(self,fun):
        self.fun = fun
        print(self)
    def __call__(self):
        str1 = self.fun()
        return str1.upper()

@Decorator
def greeting():
    return "good morning"

print(greeting())
