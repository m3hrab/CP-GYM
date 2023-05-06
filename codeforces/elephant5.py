x = int(input())
temp = []
for i in range(5,0,-1):
    temp.append(x//i)
    x = x%i

print(sum(temp))    
