for i in range(int(input())):
    n = int(input())
    s = input()
    temp = []
    new = ''
    for i in range(n):
        if i+1 < n:
            new = s[-(i+2)]+ s[-(i+1)]
            if new not in temp:
                temp.append(new)

    print(len(temp))
