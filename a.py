def remover(temp):
    temp = list(temp)
    count = temp.count('X')

    if 'S' in temp:
        value = 1
    elif 'M' in temp:
        value = 2
    else:
        value = 3
    n = [count, value]

    return n


for i in range(int(input())):
    a, b = input().split()
    a = remover(a)
    b = remover(b)
    if a[1] > b[1]:
        print(">")
    elif a[1] < b[1]:
        print("<")
    else:
        if a[1] != 1:
            if a[0] > b[0]:
                print(">")
            elif a[0] < b[0]:
                print("<")
            else:
                print("=")
        else:
            if a[0] > b[0]:
                print("<")
            elif a[0] < b[0]:
                print(">")
            else:
                print("=")