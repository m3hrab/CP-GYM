from tkinter import N


for i in range(int(input())):
    ln, q = map(int, input().split())
    n = list(map(int,input().split()))
    query = []
    for j in range(q):
        temp = list(map(int, input().split()))
        query.append(temp)

    for k in range(q):
        if query[k][0] == 0:
            for l in range(0,len(n)):
                if n[l]%2==0:
                    n[l] += query[k][1]
            print(sum(n))
        else:
            for l in range(0,len(n)):
                if n[l]%2==1:
                    n[l] += query[k][1]  

            print(sum(n))