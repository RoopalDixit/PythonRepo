n=int(input())
str=input()
grid=[]
for a in str:
    grid.append(a)
c=0

for i in range(0,n-1):
    if(grid[i]=="H" and grid[i+1]=="H"):
        c=1
        break
    elif(grid[i]=="H" and grid[i+1]!="H"):
        grid[i+1]='B'
    elif(grid[i]!="H"):
        grid[i]="B"
if(grid[n-1]!="H"):
    grid[n-1]="B"
if(c==0):
    print("YESS")
    str=''.join(grid)
    print(str)
else:
    print("NO")

        
        
    
