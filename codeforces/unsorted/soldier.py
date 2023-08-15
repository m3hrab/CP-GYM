k, n, w = map(int, input().split())
total = 0
for i in range(1,w+1):
    total += i*k

b = total - n

if b>0:
    print(b)
else:
    print("0")