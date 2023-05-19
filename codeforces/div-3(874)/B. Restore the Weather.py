for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(n):
        flag = True
        for j in range(i, n):
            if abs(a[i]-b[j]) <= k:
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
                flag = False 
                break 
        if flag:
            
    
    for i in b:
        print(i, end= ' ')