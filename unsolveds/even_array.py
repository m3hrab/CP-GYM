from math import gcd, sqrt

def prime(z):
    for k in range(2, int(sqrt(z))+1):
        if z % k == 0:
            return False
    else:
        return True

for i in range(int(input())):
    l, r = map(int, input().split())

    if l != r:
        for x in range(l, r+1):
            if x % 2 == 0:
                p = x//2
                if (2*p <= r) and (2*p >= l):
                    if p != 1:
                        print(p, p)
                        break
                if 2*p > r:
                    print(-1)
                    break
        else:
            print(-1)
    else:
        if prime(l):
            print(-1)
        else:
            for i in range(2, r):
                j = r-i
                if gcd(i, j) > 1:
                    print(i, j)
                    break
            else:
                print(-1)