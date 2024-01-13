#WRITE MODE
f=open("ksm.txt","w")#agar ks.txt likha toh vo pehle file ko khali karega fir f.write() wali line likhega
                    #"w" for write ,"a" for append
a=f.write("long time no see")#ksm.txt ban gaya hai aur f.write() wali line likh di hai
print(a)#number of characters hamne file mein dale f.write() se
f.close()

#READ AND WRITE BOTH
fl=open("k_s.txt","r+")#already existing file ko hi open kr skta hai
print(fl.read())
b=fl.write("morning")
print(b)
fl.close()