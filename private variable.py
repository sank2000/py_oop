class Car:
    __name=""
    __maxspeed=0
    def __init__(self,speed,name):
        self.__name=name
        self.__maxspeed=speed
    def drive(self):
        print(self.__name,"driving at max speed of",self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed=speed
c1=Car(100,"ola")
c1.drive()


c1.setspeed(1000)

c1.drive()
 
