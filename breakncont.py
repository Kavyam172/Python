i=0
while(True):#'while(True)' or while(1) is an infinite loop
    if i<5:
        i=i+1
        continue
    print(i,end=" ")

    if i==44:
        break#stop the loop
    i = i + 1