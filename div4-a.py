from enum import Flag


for i in range(int(input())):
    n = list(map(int,input().split()))
    flag = True
    for i in range(len(n)):
        if n[i] == sum(n)-n[i]:
            ans = "YES"
            flag = False
            break
    if flag:
        ans = "NO"
    print(ans)
