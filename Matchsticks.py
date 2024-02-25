def determine(a):
    no=0
    match={"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
    for i in a:
        no=no+match.get(i)
    if(no%2==0):
        print("1"*int((no/2)))
        
    else:
        print("7"+("1"*int(((no-3)/2))))

n=int(input())
for i in range(0,n):
    a=input()
    determine(a)
    
