'''a=0--->n=1
b=1---->n=2
n=2
loop n=2---->n<n:
    c=a+b
    a=b
    b=c
else:
    print(c)'''
'''a=0,b=1,c=0+1'''
def fibonaci_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci_recursive(n-1)+fibonaci_recursive(n-2)
#LOGIC
'''n=1--->0
n=2---->1
we want (n-1)th + (n-2)th elements'''