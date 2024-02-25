str=input()
dict={')':'(','}':'{',']':'['}
b=[]
last=-1

for char in str:
        if(char in dict.keys()):
            if(last==-1):
                print("False",char,"not nested properly")
                break
            if(last!=-1 and b[last]!=dict[char]):
                print("False",char,"Nest properly")
                break
            if(last!=-1 and b[last]==dict[char]):
                last=last -1
        else:
            b.append(char)
            last=last+1
if(last!=-1):
     print("False",b[last],"wrongly nested")
else:
    print("True")


        






    


