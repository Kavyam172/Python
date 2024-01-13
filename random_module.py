import random
n=random.randint(0,22)
print(n)
l=[1,2,3,4,5]
random.shuffle(l)
print(l)
print(random.choice(l))
l=random.sample(range(1,30),5)
print(l)