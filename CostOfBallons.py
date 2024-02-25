n=int(input())
for i in range(0,n):
    cost= list(map(int, input().split()))
    if((i+1)%2==1):
        green=cost[0]
        purple=cost[1]
    if((i+1)%2==0):
        green=cost[1]
        purple=cost[0]
    people=int(input())
    count_green=0
    count_purple=0
    sum=0
    for i in range(0,people):
        arr= list(map(int, input().split()))
        first=arr[0]
        second=arr[1]
        if(second==1):
            count_purple=count_purple+1
        if(first==1):
            count_green=count_green+1
    print(count_purple,count_green)
    sum=sum+count_green*green+count_purple*purple
    print(sum)


