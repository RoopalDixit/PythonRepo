arr = list(map(int, input().split()))
l=arr[0]
r=arr[1]
k=arr[2]
count=0
for i in range(l,r+1):
    if(i%k==0):
        count=count+1
print(count)

