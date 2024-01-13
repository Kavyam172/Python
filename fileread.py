file=open("ks.txt","r")#the second argument in open() is mode of file mentioned in file_io_basics
body=file.read()
print(body)
#body=file.read(3)
#print(body)
#body=file.read(5)
#print(body)
#print(file.readline())
#print(file.readlines())
#for line in file:
    #print(line)
#a=file.flush()
#print(a)
file.close()