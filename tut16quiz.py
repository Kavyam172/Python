list=["kavyam","neetika","sarla","manya",1,2,7,8,9]
for a in list:
    if type(a)==int and a>6:
        print(a)
#ALTERNATE PROGRAM FOR ABOVE
list=[int,float,"ff",56,2,65,1,3,78,8]
for a in list:
    if str(a).isnumeric():#can also use 'str(a).isdigit' here
        print(a)