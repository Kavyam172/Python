print("Enter your age")
a= int(input())
if 7<=a<=100:
    if a > 18:
        print("You can drive")
    elif a == 18:
        print("You need to give driving test")
    else:
        print("You cannot drive")
else:
    print("entered age should be between 7 and 100")
