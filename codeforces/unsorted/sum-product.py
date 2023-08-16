from collections import Counter
from math import sqrt

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    d = Counter(map(str, a))
    result = []

    for i in range(int(input())):
        x, y = map(int, input().split())
        if x * x - 4 * y < 0:
            result.append(0)
            continue
        D = int(sqrt(x * x - 4 * y))
        x1 = (x + D) // 2
        x2 = (x - D) // 2
        if x1 + x2 != x or x1 * x2 != y:
            result.append(0)
            continue
        if x1 != x2:
            result.append(d[str(x1)] * d[str(x2)])
        else:
            result.append(d[str(x1)] * (d[str(x1)] - 1) // 2)
    print(*result)
