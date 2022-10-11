n = int(input())
x = [i for i in range(1,n+1,2)]
y = [i for i in range(0,n+1,2)]
t = sum(y)-sum(x)
print(t)