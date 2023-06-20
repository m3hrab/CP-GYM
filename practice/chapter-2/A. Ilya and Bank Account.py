n = list(input())
if n < 0:
    if len(n) >= 2:
        if n[-1] > n[-2]:
            n[-1] = ' '

