for i in range(int(input())):
    m , n = map(int, input().split()) # 3, 13
    b = list(map(int, input().split())) # 3, 1, 4
    total = 0
    i = 1

    while total < n:
        if i not in b:  
            b.append(i) #3 1 4 2 5 6
            total += i #13
        i += 1
    b2 = [i for i in range(1,len(b)+1)]
    b.sort()
    if n == total and b==b2:
        print("YES")
    else:
        print("NO")

