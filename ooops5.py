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
    @classmethod#using classmethod as constructor('__init__' wala kaam)
    def constr(cls,string):#ye method ek string leta hai aur us mein se parameters leke oblect return krta hai
        return cls(*string.split('-'))#*args ka use krke saare parameters le liye


kavyam=Human('kavyam',5)
neetika=Human('neetika',18)
sarla=Human.constr('sarla-30')
print(sarla.__dict__)
