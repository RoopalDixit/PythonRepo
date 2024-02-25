target=int(input())
arr= list(map(int, input().split()))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)-2):
        sum=0
        sum=arr[i]+arr[j]
        if(sum==target):
            print(i,j)
    


