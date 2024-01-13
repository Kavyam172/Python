class Human:
    def details(self):#defining funtion(called class attribute) in a class
        return self.__dict__#we use self to refer to the arguement we will take
kavyam=Human()
kavyam.name='kavyam'
kavyam.age=13

neetika=Human()
neetika.name='neetika'
neetika.age=18

print(kavyam.details())#can be used like this
#function automatically takes an arguement
print(neetika.details())