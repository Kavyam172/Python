a=12#GLOBAL VARIBLE
def f():
    b=14#LOCAL VARIABLE
    global c#declaring a global variable
    c=10
    print(b)
    return b
print(a)
a=f()
print(a)
print(c)
#program variable ko pehle local scope mein dhoondta hai phir global scope mein
'''global variable ko ek function mein use kr skte hain alter nhi, uske liye pehle global keyword 
 use karna padega'''