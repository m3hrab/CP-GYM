for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    ans = "YES"
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            ans = "NO"
            break 
    
    print(ans)