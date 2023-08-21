a = list(input())
x = set()
for i in range(1,len(a)-1):
    if a[i] != ',' and a[i] != ' ':
        x.add(a[i])

print(len(x))