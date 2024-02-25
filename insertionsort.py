arr=[13,2,45,3,7]    # why set instead of list/array
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1   # where is J declared/defined
    while(j>=0 and key<arr[j]):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print(arr)