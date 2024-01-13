print("enter 2 numbers")
a=input()
b=input()
try:
    print("sum=", int(a)+int(b))#will try to execute the 'try'function & if not possible will execute the 'except' part

except Exception as e:#catches the error and can print it as shown
    print(e)#we can also put any other function here
except:
    print("agar number nhi daloge toh sum kaise aayega")
print("this line will be printed regardless if 'try' function can or cannot be executed")