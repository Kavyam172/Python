def printkav(a):
    return f'the argument is {a}'
def sume(a,b):
    return a+b
print(f'the value of __name__ is {__name__}.')#original file main '__name__' ki value '__main__' hoti hai
#value of '__name__' in above line becomes 'tutmain2' when file is imported in tutmain1
if __name__ == '__main__':#used so that this part is not executed when this file is imported into another file
    print(printkav('kavyam'))
    print(sume(5,6))

