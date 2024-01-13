li=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]#4*4(4 rows,4 columns) 2D list
a=li[1][1]#2nd row, 2nd column
b=li[3][2]#4th row,3rd column
print(a,b)
li[0][2]="three"#changing elements in 2D list
print(li)

#JAGGED LISTS
#2D lists where column size is not the same
li1=[[1,2,3],[4,5],[6,7,8,9,0]]

#TAKING INPUT OF 2D LISTS
a=input().split()
n,m=int(a[0]),int(a[1])#n---> no. of rows,m--->no. of columns
l2d=[[int(j) for j in input().split()] for i in range(n)]
print(l2d)
#for input of jagged lists m is not needed

b=input().split()
n2,m2=int(b[0]),int(b[1])
inp=input().split()
l2d_2=[[int(inp[m*i+j]) for j in range(m2)] for i in range(n2) ]
#(m*i+j)-->formula for nth element in input if input is in a single line
print(l2d_2)

#if n,m,input all are given in a single line
b2=input().split()
n3,m3=int(b2[0]),int(b2[1])
inp2=b2[2:]
l2d_3=[[int(inp2[m3*i+j]) for j in range(m3)] for i in range(n3) ]
print(l2d_3)

#printing 2d lists
dl=[[1,2],[33,4],[5,6666]]
for i in dl:
    print(" ".join([str(j) for j in i]))
print()