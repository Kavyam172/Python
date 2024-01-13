with open('ks.txt','r') as f:
    print(f.readlines())
    f.seek(0)
    print(f.tell())#used to tell location of file pointer
    print(f.readline())
    print(f.tell())
    f.seek(10)#to tell the file pointer to go to a specific position
    print(f.readline())
    print(f.tell())
