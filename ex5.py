import datetime
ct=datetime.datetime.now()

def fun():
    name = input("Enter your file name.\n")
    a = input("What do you want to do(Add Entry(enter 1) or Read Entries(enter 2))\n")
    if a == "1":
        f = open(f"{name}.txt", "a")
        while True:
            w = input("Type your entry.\n")
            f.write(f'{ct}:\t{w}\n')
            q2 = input('do you want to add another entry?(yes or no)\n')
            if q2.lower() == 'yes':
                continue
            elif q2.lower() == 'no':
                break
        f.close()
    elif a == "2":
        f = open(f"{name}.txt", "r")
        r = f.read()
        print(r)
        f.close()

def health_management():
    q=input("Do you want to create a file(Enter 1) or Open an existing file(Enter 2).\n")
    try:
        if q.lower()=="1":
            name=input("Enter your file name.\n")
            f=open(f"{name}.txt","x")
            f.close()
            health_management()
        elif q.lower()=="2":
            fun()
    except FileExistsError:
        print('File already exists.')

def again(func):
    ques=input('Do you want to run the program again?(yes or no)\n')
    if ques.lower()=='yes':
        func()
    elif ques.lower()=='no':
        print('Thank You.See You Next Time')
health_management()
again(health_management)