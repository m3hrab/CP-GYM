x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

if (x+y+z) <= (a+b+c):
    if x<=a:
        a = a - x
        temp = (a+b)
        if y <= temp:
            temp = temp - y

            if (temp + c) >= z:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

    else:
        print("NO")
else:
    print("NO")

