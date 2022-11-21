for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    final = []
    for x in range(len(s)):
        temp = s[x]
        s[x] = s[-1]
        s[-1] = temp 
        final.append(temp-max(s[:-1]))
    
    
    for n in final:
        print(str(n),end=' ')
    print()