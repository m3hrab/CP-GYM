s = input()

upper = 0
lower = 0
for i in range(len(s)):
    if ord(s[i]) < 91:
        upper += 1
    elif ord(s[i]) > 96:
        lower += 1

if upper > lower:
    print(s.upper())
else:
    print(s.lower())