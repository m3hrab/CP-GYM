for i in range(int(input())):
    n = list(map(int, input().split()))
    n.sort()
    if sum(n[:3]) < n[3]:
        print("YES")
    else:
        print("NO")