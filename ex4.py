n=int(input("Enter an integer\n"))
i=int(input("enter 0 or 1\n"))
b=bool(i)

if b==False:
    while(True):
        if n!=0:
            print(n*"*")
            n=n-1
            continue
        else:
            break
elif b==True:
    a=1
    while(a<=n):
        print(a*"*")
        a=a+1
        continue

#ALTERNATE CODE
print("Pattern printing")
num = int(input("Enter num how many rows you want : \n"))
print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False : \n")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)

if bool_val=="0":
    for i in range(num,0,-1):
        print("*"* i)
