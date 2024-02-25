from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
m = defaultdict(int)
for num in a:
    m[num] += 1
count = 0
max = 0
for key, value in m.items():
    if value == max:
        count += 1
    if value > max:
        max = value
        count = 1
print(count)