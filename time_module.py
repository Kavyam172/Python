import time

initial=time.time()#give value of time at any instant
n=0
while n<10:
    print(n)
    n+=1

print(f'while loop ran in {time.time()-initial} seconds')
initial2=time.time()
for i in range(10):
    print(i)
print(f'for loop ran in {time.time()-initial2} seconds')