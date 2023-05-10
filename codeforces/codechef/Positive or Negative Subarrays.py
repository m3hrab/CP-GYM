def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


for i in range(int(input())):
    n = int(input())
    a = []
    b = list(map(int, input().split()))
    for i in range(n):
        a.append(pow(2,i))

    c = []
    for i in range(n):
        c.append(a[i]*b[i])
    
    c = subsets(c)
    
    positive = 0
    negative = 0
    for i in c:
        if len(i)!=0 and len(i)!=4:
        if sum(i)>0:
            positive +=1
        else:
            negative +=1
    
    print(abs(positive-negative))




