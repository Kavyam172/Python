li=[1,2,3,4]
li_new=[x**2for x in li]#code for creating a new list of squares from given list

li_new_even=[x**2 for x in li if x%2==0]#square of only even numbers

l1=[x**2 for x in li if x%2==0 or x%3==0]

l2=[x**2 for x in li if x%2==0 if x>2]#multiple ifs

l3=[x*y for x in li for y in range(3) if x>2]#multiple for loops

l4=[x if x>3 else x**2 for x in li]#using if else condition

s="neetika"
ls=[i for i in s]#list from string

li2=[1,2,3,4]
l5=[[x for x in li] for y in li2]#2D lists from 2 lists

a=["kavyam","neetika","sarla"]
l6=[[i for i in j]for j in a]#2D list from 1 list
print(ls)