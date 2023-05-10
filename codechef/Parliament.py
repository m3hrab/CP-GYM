for i in range(int(input())):
    n, x = map(int, input().split())
    if x==0:
        print("NO")
    elif x*100/n >= 50:
        print("YES")
    else:
        print("NO")
