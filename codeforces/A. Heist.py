n = int(input())
a = sorted(list(map(int, input().split())))

count = 0
for i in range(n-1):
    temp = abs(a[i]-a[i+1])
    if temp>1:
        count += temp-1
print(count)
