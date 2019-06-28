class Land(object):
    def __init__(self):
        print("in land")
    def display(self):
        print("I can live in Land")
        
class Water:
    def __init__(self):
        print("in Water")
    def display(self):
        print("I can live in Water")

class Frog(Water,Land):
    
    def __init__(self):
         print("i am a frog\n")
         super().__init__()
         super().display()

obj=Frog()
