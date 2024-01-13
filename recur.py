#RECURSION---function calling itself inside the function
def factorial_recursive(n):#recursive function
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
n=int(input())
print(factorial_recursive(n))

def factorial_iterative():#iterative function
    n=int(input())
    a=1
    for i in range(1,n+1):
        a*=i
    print(a)
factorial_iterative()
