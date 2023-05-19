for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    even = []
    odd = []

    for i in a:
        if a%2==0:
            even.append(i)
        else:
            even.append(i)
    
    if len(even)==0:
        flag = False
        for i in odd:
            if i<=0:
                flag = True
                break 
        if flag:
            print("NO")
        else:
            print("YES")
    elif(len(odd))==0:
        flag = False
        for i in even:
            if i<=0:
                flag = True
                break 
        if flag:
            print("NO")
        else:
            print("YES")
    else:
        even.sort()
        odd.sort()
        
