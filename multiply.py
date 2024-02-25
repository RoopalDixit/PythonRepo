a=[2,5,7,8]
b=[4,2]
carry=0
first=[]
sum=[0]*(len(a)+len(b))
for i in range(len(b)-1,-1,-1):
    carry=0
    for j in range(len(a)-1,-1,-1):
        m=b[i]*a[j]
        m=m+carry
        print(m)
        if(m<10 or j==0):
            first.append(m)
        else:
            rem=m%10
            first.append(rem)
            carry=int(m/10)
        
    
print(sum)
        



