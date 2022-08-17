p = 0
c = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    p -= a
    p += b
    if p>c:
        c = p

print(c)