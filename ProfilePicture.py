l=int(input())
n=int(input())
for i in range(0,n):
    a = list(map(int, input().split()))
    w=a[0]
    h=a[1]
    if(w<l or h<l):
        print("UPLOAD ANOTHER")
    elif(w==l and h==l):
        print("ACCEPTED")
    else:
        print("CROP IT")

