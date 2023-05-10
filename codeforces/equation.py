def is_composite(n):
    flag = False
    for j in range(2,n):
        if n%j==0:
            flag = True
            break 
    return flag           


n = int(input())

for i in range(n,1000000000):
    if is_composite(i) and is_composite(i+n):
        print("%d %d"%(i+n,i))
        break

