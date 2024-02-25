rows=int(input())
columns=int(input())
matrix=[]
a=[]
for i in range(0,rows):
    a= list(map(str, input().split()))
    matrix.append(a)
print(matrix)
max=0
for i in range(0,rows):
    a=matrix[i]
    count=0
    for j in range(0,columns-1):
        if(a[j]=="#" and a[j+1]=="#"):
            count=count+1
            

        

        

