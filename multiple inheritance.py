class Land:
    def display(self):
        print("I can live in Land")
        
class Water:
    def printing(self):
        print("I can live in Water")

class Frog(Land,Water):
    print("i am a frog\n")



obj=Frog()
obj.display()
obj.printing()
