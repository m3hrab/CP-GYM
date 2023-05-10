n = int(input())
s = input()
if n>=11:
    if s.count('8') >= n//11:
        print(n//11)
    elif s.count('8') < n//11:
        print(s.count('8'))
else:
    print('0')