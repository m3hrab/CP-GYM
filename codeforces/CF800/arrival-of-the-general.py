n = int(input())
a = list(map(int, input().split()))
first = max(a) 
last = min(a)

c = (a.index(first)-0)
if a.count(last)>1: 
    d = 0
    for i in range(n-1, -1,-1):
        if a[i] == last:
            break
        d += 1

else:
    i
    d = n - 1 - a.index(last)

if a.index(first) > a.index(last):
    print(c+d-1)
else:
    print(c+d)    