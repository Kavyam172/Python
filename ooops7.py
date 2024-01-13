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

#inheritance    #inheritance mtlb jb hame ek class ke sari qualities(attributes and methods) dusri class mein chahiya
class Male(Human):#yahan hame Human class ki saari qualities(attributes and methods) Male class mein inherit krni hai
    def __init__(self,a,b,c):#mujhe Male class ke liye additional(a,b ek alava 1 aur) argument lena tha isliye constructor bnaya
        self.name = a#id constructor mein Human class vala hi kaam hai bas 1 aur argument daal diya
        self.age = b
        self.height=c

    def print_gender(self):
        print(f"{self.name} is a Male")
    pass



neetika=Human('neetika',18)
sarla=Human.constr('sarla-30')
kavyam=Male('kavyam',5,150)
print(neetika.details())
print(kavyam.details())
kavyam.print_gender()