import math
a,b,d = map(int, input().split())

x = math.acos(d) - math.asin(d)
y = math.asin(d) + math.acos(d)
print("%f %f"%(x,y))