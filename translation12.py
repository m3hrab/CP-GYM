s = input()
t = input()
n = ''
for i in range(len(s)-1,-1,-1):
    n += s[i]

if n==t:
    print("YES")
else:
    print("NO")