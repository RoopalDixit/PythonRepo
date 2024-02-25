from array import*
n=int(input("Enter the number of customers"))
m=int(input("Enter the number of banks"))
arr=[]
sum=[]
b=0
for i in range(0,n):
    arb=[]
    for j in range(0,m):
        a=int(input("Enter the money"))
        arb.append(a)
    arr.append(arb)
for i in arr:
    b=0
    for j in i:
        b=b+j
    sum.append(b)
max=sum[0]
z=0
for x in range(0,n):
    if(max<sum[x]):
        max=sum[x]
        z=x
print(" Richest person is ",z,"with wealth",max)