class Car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print("drive")
    def __updatesoftware(self):
        print("updating software")
        self.drive()
blackcar=Car()
