n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 0:
        temp = a[:i]
        temp.reverse()
        for j in range(len(temp)):
            a[j] = temp[j]
    
for i in a:
    print("%d"%i, end=' ')
print()