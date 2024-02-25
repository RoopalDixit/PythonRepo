str=input()
b=""
for i in range(len(str)-1,-1,-1):
    b=b+str[i]
if(str==b):
    print("Yes")
else:
    print("No")

