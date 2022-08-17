n, t = map(int, input().split())
s = list(input())
temp = s[:]
for i in range(t):
    for j in range(len(s)-1):
        if s[j] == 'B' and s[j+1] == 'G':
            temp[j] = 'G'
            temp[j+1] = 'B'
    s = temp[:]
n = ''.join(s)
print(n)