mat=[]
m=int(input("Enter the number of rows"))
n=int(input("Enter the number of columns"))
for i in range(0,m):
    arr=[]
    for j in range(0,n):
        a=int(input("Enter 0 or 1"))
        arr.append(a)
    mat.append(arr)
print(mat)
s=0
sum=[]
for i in mat:
    s=0
    for j in i:
        s=s+j
    sum.append(s)
print("Sum",sum)
max=0
row=0
for i in range(0,m):
    print("Row :",i,":",sum[i])
for i in range(0,len(sum)):
    if(max<=sum[i]):
        max=sum[i]
        row=i
print("Strongest row",row," sum",max)




# def kWeakestRows(self, mat, k):
#     sum=[]
#     for i in mat:
#      s=0
#      for j in i:
#         s=s+j
#     sum.append(s)
#     print("Sum",sum)
#     max=0
#     row=0
#     for i in range(0,m):
#         print("Row :",i,":",sum[i])
#     for i in range(0,len(sum)):
#         if(max<=sum[i]):
#             max=sum[i]
#             row=i
#     print("Strongest row",row," sum",max)

    
