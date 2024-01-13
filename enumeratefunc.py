l=[1,2,3,4]
for i,a in enumerate(l):#enumerate function returns both elements(as a) and their index(as i)
    if a%2==0:
        print(f'index is {i},element is {a}')