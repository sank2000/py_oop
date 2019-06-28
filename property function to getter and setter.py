class Students:
    def __init__(self,marks):
        self.__marks=marks
    def per(self):
        return  (self.__marks/600)*100
    def getter(self):
        print("getting values:",end=" ")
        return self.__marks  # getter
    def setter(self,mark):
        if mark<0 or mark>600:
            print("can't set values")
        else:
            print("setting values:",mark)
            self.__marks=mark
    mark=property(getter,setter)
s1 = Students(600)
print(s1.per(),"%")
s1.mark=500
print(s1.mark)
