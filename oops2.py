class Human:
    scientific_name='homosapien'#instance for the class in general. it is common for all objects in this class
    pass
kavyam=Human()
print(kavyam.scientific_name)
print(Human.scientific_name)
kavyam.scientific_name='homo sapien sapien'#can be changed for a particular object or the class itself
print(kavyam.scientific_name)
print(Human.scientific_name)#class ka general instance abhi bhi vhi hai