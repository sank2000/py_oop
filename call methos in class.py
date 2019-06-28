class Printing:
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print("Entered user name is:",self.name)


p1=Printing("san")
p1()