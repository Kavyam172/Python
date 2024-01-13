class Dad:
    a=1
    def dad(self):
        print('Test')
    pass
class Son(Dad):
    b=1

    def pr(self):
        print(self.b,'=b',self.a,'=a')
    pass

#MULTILEVEL INHERITANCE

class Grandson(Son):#Dad ke gun Son mein aaye aur Son ke gun(including Dad ke gun) Grandson mein aaye
    b=5#there is a same variable in Son so the function will be override in Grandson
    def pr(self):#there is a same function in Son so the function will be override in Grandson
        print(self.b,'=b',self.a,'=a','Tester')

    pass

sarla=Dad()
neetika=Son()
kavyam=Grandson()

print(sarla.a)
print(neetika.a,neetika.b)
print(kavyam.a,kavyam.b)
sarla.dad()
neetika.pr()
neetika.dad()
kavyam.pr()
kavyam.dad()