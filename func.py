a=5
b=1
c=sum((a,b))# built in function
print(c)

def func1():
    print("Hey there")
func1()

def func2(a,b):
    print(a+b)
func2(5,1)

def func3(a,b):
    """This function is used to find average of 2 numbers"""
    avg=(a+b)/2
    print(avg)
    return avg#return is used to rturn the value from the function
#v=func3(5,1)#'return' returns the value of avg fron the function and saves it in v
#print(v)
func3(5,1)
print(avg)
def f(a,b,c="f"):
    print(a)
    print(b)
    print(c)