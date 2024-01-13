#GENERAL FORMAT OF RANGE FUNTION
#range(start,stop,increment)
#'start'-->indicates starting point(by default 0)
#'stop'-->indicates where to stop(number itself not included)
#'increment'-->how much is increased after every number

a=range(6)
print(a)#print the range itself

for n in a:
    print(n)#for loop used with range()

b=range(3,6)
for n in b:
    print(n)

c=range(1,5,2)
for n in c:
    print(n)

d=range(5,0,-1)#negative increment
for n in d:
    print(n)