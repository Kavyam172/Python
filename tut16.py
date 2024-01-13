list=["kavyam","neetika","sarla","manya"]
for a in list:
    print(a)#can also be used for 'list in list' format
for a in list:
    if a.endswith("a"):#can also use 'if' within the loop
        print(a)

list_in_list=[["hulk","green"],["flash","red"],["thor","idk"]]
for a in list_in_list:
    print(a)
for a,b in list_in_list:
    print(a,b)
for a, b in list_in_list:#different ways to use for loop in 'list in list' format
    print(a,"is", b)

d= {"me":"my","he":"his","she":"her"}
for a in d:#prints only keys
    print(a)
for a,b in d.items():#d.items required to print both keys and values
    print(a,b)
for e in range(1,20):#range funtion in 'for' loop
    print(e)