for i in range(int(input())):
    n, k = map(int, input().split())
    m = 96+k
    x = 97
    str = ''
    for i in range(n):
        if x > m:
            x = 97
        str += chr(x)
        x += 1
    print(str)