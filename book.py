a=[2,5,7,8]
b=[]
p=[]
carry=0
for i in range(len(a)-1,0,-1):
    c=a[i]*b
    c=c+carry
    if(c<10):
        p.append(c)
    else:
        rem=c%10
        p.append(rem)
        carry=int(c/10)
p.append((a[i-1]*b)+carry)
print(p)
    

    




    




     
