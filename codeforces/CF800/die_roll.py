import math
a, b = map(int, input().split())
n = 7 - max(a,b)

temp = math.gcd(n,6)
x = n//temp 
y = 6//temp

print("%d/%d"%(x,y))