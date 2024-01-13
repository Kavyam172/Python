#SETS
set1={1,2,3,4}
sete=set()#empty set
set2={4,5,6,7,8}
print(set1)
print(set1.union(set1,set2))
print(set1.__and__(set2))
set1.update("5")
print(set1)