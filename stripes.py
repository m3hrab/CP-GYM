for i in range(int(input())):
    b=0
    r=0
    for j in range(8):
        n = list(input())
        b += n.count('B')
        r += n.count('R')

        if n.count("B")!=0 or n.count("R") != 0:
            m = n[:]

    if b == r:
        if m.count("B")>=1:
            print("B")
        else:
            print("R")
        
    elif b>r:
        print("B")
    else:
        print("R")

