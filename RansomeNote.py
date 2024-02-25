a= input("Enter the string")
b= input("Enter the refrence string")
c=0
for i in b:
    # print("i",i)
    for j in a:
        # print("j",j)
        if(i==j):
            c=c+1
            break
        # print("c",+c)
if(c>=len(a)):
    print("Ransome Note")
else:
     print("Not ransome note")

        