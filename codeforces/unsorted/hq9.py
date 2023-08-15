p = input()
hq = ['H','Q','9']
flag = True
for letter in p:
    if letter in hq:
        print("YES")
        flag = False
        break 

if flag:
    print("NO")