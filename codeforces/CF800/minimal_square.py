for _ in range(int(input())):
    a, b = map(int, input().split())

    mx = max(a,b)
    mn = min(a,b)

    temp = (mx * 2) * mn
    ans = (mx * 2) ** 2

    if ans < temp:
        i = 1 
        n = mx * 2
        while ans < temp:
            ans = (n + i)  