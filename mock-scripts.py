n= int(input())
a = list(map(int, input().split()))
length=len(a)
b=0
c=[]
for i in range(0,length):
    b=0
    s=0
    for j in range(1,length):
        s=0
        s=s+j+i
        if(s<=(length)):
            b=sum(a[i:s])
            print("Length",i,a[i:length])
        else:
            break
    c.append(b)
print(c)
print(max(c))
    





