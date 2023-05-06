for i in range(int(input())):
    s = input()
    n = "Yes"
    for i in s:
        if i not in n:
            print("NO")
            n = 'No'
            break
    
    if n=="No":
        continue
    else:
        for j in range(len(s)):
            if len(s) <= len(n)/2:
                break 
            else:
                n+="Yes"

        
        m1 = n.index(s[0])
        m2 = m1+len(s)

        if n[m1:m2]==s:
            print("YES")
        else:
            print("NO")

    