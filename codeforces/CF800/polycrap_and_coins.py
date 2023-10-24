for i in range(int(input())):
    n = int(input())

    temp = n // 3
    a = b = temp

    if n%3 == 1:
        a += 1
    elif n%3 == 2:
        b += 1

    print("%d %d"%(a,b))