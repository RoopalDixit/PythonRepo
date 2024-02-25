import math
n=int(input())
arr = list(map(int, input().split()))
mul=1
for i in arr:
    mul=mul*i
result=mul%(math.pow(10,9)+7)
print(result)