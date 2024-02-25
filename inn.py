test=int(input())
for x in range(0,test):
    dim= list(map(str, input().split()))
    rows=dim[0]
    colums=dim[1]
    matrix=[]
    for i in range(0,rows):
        a= list(map(str, input()))
        matrix.append(a)
    max=0
    for j in range(0,rows):
        a=matrix[j]
        count=1
        for i in range(0,colums-1):
            if(a[i]=="#" and a[i+1]=="#"):
                count=count+1
            if(max<count):
                max=count
    print(max)


