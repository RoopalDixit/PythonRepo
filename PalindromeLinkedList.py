n= int(input("Enter the number"))
arr=[]
for i in range(0,n):
    x=int(input("Enter the number"))
    arr.append(x)
a=len(arr)
print("Length of array",a)
c=0
b=int(a/2)
print("Midpoint",b)
for i,j in zip(range(b,-1,-1),range(b+1,a)):
    print("i",i,"j",j)
    if(arr[i]==arr[j]):
        print("Arr[i]",arr[i],"Arr[j]",arr[j])
        c=c+1

if(c==b):
    print("Palindrome Linked List")
else:
    print("Palindrome Not Linked List")





