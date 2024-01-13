'''function ki copy bnana'''
# def fun1():
#     print('test')
#
# fun2=fun1#function ki copy bnali
# del fun1#deleting the function
# fun2()

'''returning function inside a function'''
# def ret(n):
#     if n==1:
#         return print
#     elif n==0:
#         return sum
# a=ret(1)
# b=ret(0)
# print(a,b)

'''function mein dusra function as argument lena'''
# def fun(func,a):
#     func(a)
# a='test'
# fun(print,a)

'''decorators'''
#ek function jo kisi function ko as argument leke use execute kre with enhanced command
# lekin us function ko permanently change na kre
def dec1(func):
    def test_new():
        print('Executing')
        func()
        print('Executed')
    return test_new

def test():
    print('test')

a=dec1(test)#yeh decorator hai
a()         #yahan agr test() ko likhu to normaly execute hoga,but use dec1 function se pass karva ke uska ek enhanced version bna liya

@dec1#decorators ko likhne ka dusra tarika
def test2():
    print('TEST')

test2()