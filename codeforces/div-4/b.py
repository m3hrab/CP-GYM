for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    blank_spc = 0
    if a[0] == 0:
        blank_spc += 1

    max_spc = blank_spc    
    for i in range(1, n):
        if a[i]==0:
            blank_spc += 1
            if blank_spc > max_spc:
                max_spc = blank_spc
        else:
            blank_spc = 0

    print(max_spc)