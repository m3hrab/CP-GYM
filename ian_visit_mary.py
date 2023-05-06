t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    n = 0
    if a != b:
        n = 2
        x1 = a
        y1 = 0
        x2 = 0
        y2 = b
    else:
        n = 1
        x1 = a
        y1 = b

    print(n)
    print(x1, y1)
    if n == 2:
        print(x2, y2)
