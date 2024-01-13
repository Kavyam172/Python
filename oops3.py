#classmethod
class Human:
    dob='00-00-0000'
    def __init__(self,a,b):#'__init__' function helps to take input with help of class
        self.name=a
        self.age=b
    def details(self):
        return self.__dict__
    @classmethod#decorator
    def DOB(cls,dat):#'cls' value aa gyi self ki jgh @classmethod ki vajah se
        cls.dob=dat#seedha class mein change hoga,agr 'dob' exists to uski value change krega vrna 'dob' creat krega

kavyam=Human('kavyam',5)
neetika=Human('neetika',18)
print(kavyam.details())
neetika.DOB('11-11-1111')
print(kavyam.dob)