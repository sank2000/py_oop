class Cat:
    def sound(self):
        print("meow meow")
class Dog:
    def sound(self):
        print("bow bow")
def makesound(animaltype):
    animaltype.sound()

catobj=Cat()
dogobj=Dog()
makesound(dogobj)

makesound(catobj)
