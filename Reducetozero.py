n=int(input("Enter the number"))
c=0
while(n>0):
    n=int(n/2)
    c=c+1
    if(n%2!=0):
        n=n-1
        c=c+1
print("Number of steps",c)
