for i in range(int(input())):
    n = int(input())
    s = list(input())
    s.sort()
    print(ord(s[-1])-96)