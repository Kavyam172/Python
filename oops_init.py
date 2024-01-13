class Human:
    def __init__(self,a,b):#'__init__' function helps to take input with help of class
        self.name=a
        self.age=b
    def details(self):
        return self.__dict__
kavyam=Human('kavyam',5)
print(kavyam.details())