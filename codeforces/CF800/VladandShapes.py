for i in range(int(input())):
    n = int(input())
    grid = []
    for j in range(n):
        grid.append(list(input()))

    flag = []
    for row in grid:
        n = row.count('1')
        if n != 0:
            flag.append(n)

    if len(flag) == int(flag[0]):
        print("SQUARE")
    else:
        print("TRIANGLE")
