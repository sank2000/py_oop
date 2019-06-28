class Students:
    def __init__(self,marks):
        self.__marks=marks
    def per(self):
        return  (self.__marks/600)*100

    @property
    def mark(self):
        return self.__marks  # getter
    @mark.setter
    def mark(self,mark):
        self.__marks=mark

s1 = Students(600)
print(s1.per(),"%")
s1.mark=500
print(s1.mark)
