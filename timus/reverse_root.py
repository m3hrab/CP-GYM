import math
numbers = []
while True:
    try:
        line = list(map(int, input().split()))
        for n in line:
            numbers.append(n)
        
    except EOFError:
        break

for i in range(len(numbers)-1,-1,-1):
    print("%.4f"%(math.sqrt(numbers[i])))
