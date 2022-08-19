n, h = map(int, input().split())
f = list(map(int, input().split()))
w = 0
for i in f:
    if i > h:
        w += 2
    else:
        w += 1
print(w) 