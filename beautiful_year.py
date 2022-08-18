s = str(int(input())+1)
flag = False
while True:
    for i in s:
        if s.count(i) > 1:
            flag = True 
            break
    if flag:
        s = str(int(s)+1)
        flag = False
    else:
        print(s)
        break        