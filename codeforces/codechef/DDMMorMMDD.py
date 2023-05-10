for i in range(int(input())):
    s = input()
    t1 = int(s[:2])
    t2 = int(s[3:5])
    if t1<=12 and t2<=12:
        print("BOTH")
    elif t1>12:
        print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")