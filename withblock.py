with open('kavyam.txt','a') as f:#using with block to open files
    f.write('my name is kavyam.')#there is no need for 'f.close' after with block

with open('k_s.txt','r') as f2:
    a=f2.readlines()
    print(a)
print(f.closed)#checking if file is closed, return True or False as output