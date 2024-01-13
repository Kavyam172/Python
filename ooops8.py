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
    @staticmethod
    def pr(string):
        print(string,'Test')

class Animal:

    def __init__(self,name,type):
        self.name=name
        self.type=type

    def details_a(self):
        print(f'Animal name:{self.name},Animal type:{self.type}')


#multiple inheritance mein koi bhi method ya variable use krte hain to sbse pehle  1st class mein  check
# krega fir 2nd mein.
#Agr 1st mein mil gya to execute krega vrna 2nd mein dhundke execute krega .
# Agr 2nd mein bhi nhi mila to error dega
class Fantasy(Human,Animal):#yahan pehle Human mein dekhega fir Animal mein
    pass


neetika=Human('neetika',18)
sarla=Human.constr('sarla-30')
Horse=Animal('Light','Horse')
centaur=Fantasy('Kavyam',20)