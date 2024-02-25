s=input()
length=len(s)
for i in range(0,length-1):
    if(s[i]!=s[i+1]):
        sep=i
if((sep+1)*3==length):
    print("Yes")
else:
    print("No")
