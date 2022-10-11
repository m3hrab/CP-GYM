import math
for i in range(int(input())):
    count = 0
    n = int(input())
    for i in range(1,n+1):
        for j in range(1,n+1):
            if math.lcm(i,j)/math.gcd(i,j) > 3:
                count -= 1
            count += 1
    print(count)
            