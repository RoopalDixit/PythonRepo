tag=input()
length=len(tag)
c=0
print(length)
for i in range(0,length-1):
    print(tag[i])
    sum=0
    if (tag[i].isdigit()) and (tag[i+1].isdigit()):
        sum=int(tag[i])+int(tag[i+1])
        if(sum%2!=0):
            print("Invalid")
            break
        else:
            c=c+1
    elif (tag[i].isalpha()):
        if(tag[i]=="A" or tag[i]=="E" or tag[i]=="I" or tag[i]=="O" or tag[i]=="U" or tag[i]=="Y"):
            print("Invalid")
            break
        else:
            c=c+1
    else:
        c=c+1
print(c)

if(c==length-1):
    print("Valid")
    

    
            






    