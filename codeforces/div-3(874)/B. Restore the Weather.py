for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(i, n):
            if abs(a[i]-b[j]) <= k:
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
                break
    
    for i in b:
        print(i, end= ' ')