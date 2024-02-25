str=input()
dict={')':"(",'}':'{',']':'['}
b=[]
last=-1
count=0
for char in str:
    if(char in dict.keys()):
        if(last!=-1 and b[last]==dict[char]):
            count=count+2
            last=last-1  
    else:
        b.append(char)
        last=last+1
print(count)

