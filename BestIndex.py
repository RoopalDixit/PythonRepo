n=int(input())
a = list(map(int, input().split()))
length=len(a)
b=[]
sum=0
for i in range(0,length):
    sum=0
    sum=sum+a[i]
    p=i
    for j in range(2, length):
        if(p+j<length):
            for l in range(p+1,j+p+1):
                sum=sum+a[l]
        else:
            break
        p=l
    b.append(sum)
max=0
for c in b:
    if(c>=max):
        max=c
print(max)
    
        
