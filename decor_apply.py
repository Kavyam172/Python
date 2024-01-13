import time
def calculate_time(fun):
    def func():
        a=time.time()
        fun()
        b=time.time()
        print('Execution time:',b-a)
    return func

@calculate_time
def code1():
    s=0
    for i in range(1,200000000):
        s+=i
    print(s)


code1()