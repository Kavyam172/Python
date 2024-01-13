# static method
class Human:
    dob='00-00-0000'
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def details(self):
        return self.__dict__
    @classmethod
    def DOB(cls,dat):
        cls.dob=dat
    @classmethod
    def constr(cls,string):
        return cls(*string.split('-'))
    @staticmethod#jab na instance ko aur na class ko argument lena ho
    def pr(string):#ek normal function jaisa hi ,ethod hai,except hm chahte hain ki yeh sirf iss class ke liye chale
        print(string,'Test')


kavyam=Human('kavyam',5)
neetika=Human('neetika',18)
sarla=Human.constr('sarla-30')
sarla.pr('Hello Sarla')
Human.pr('Hello Human')

