def solve():
    n = int(input())
    crews = []
    crews_status = []
    for i in range(n):
        name, status = input().split() 
        if status == 'rat':
            status = 1
        elif status == 'woman' or status == 'child':
            status = 2
        elif status == 'man':
            status = 3 
        elif status == 'captain':
            status = 4

        crews.append(name)
        crews_status.append(status)

    indx = [_ for _ in range(n)]
    for i in range(n):
        swaped = False
        for j in range(n-i-1):
            if crews_status[j] > crews_status[j+1]:
                crews_status[j], crews_status[j+1] = crews_status[j+1], crews_status[j]
                indx[j], indx[j+1] = indx[j+1], indx[j]
                swaped = True

        if swaped == False:
            break 
    

    for i in indx:
        print("%s"%(crews[i]))

if __name__ == "__main__":
    solve()