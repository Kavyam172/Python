print("enter first number")
a=input()
print("first number=",a)
print("enter second number")
b=input()
print("second number=",b)
c=input("enter the operation")
if a=="45" and b=="3" and c=="*":
    print("solution=",555)
elif a=="56" and b=="9" and c=="+":
    print("solution=",77)
elif a=="56" and b=="6" and c=="/":
    print("solution=",4)
else:
    d1 = {"+": int(a) + int(b), "-": int(a) - int(b), "*": int(a) * int(b), "/": int(a) / int(b)}
    print("Solution=", d1[c])
