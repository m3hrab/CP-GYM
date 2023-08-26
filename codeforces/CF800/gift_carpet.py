def solve():
    n, m = map(int, input().split())
    carpet = []
    for i in range(n):
        carpet.append(list(input()))

    name = ['v','i','k','a']
    ind = 0
    flag = False
    for i in range(m):
        for j in range(n):
            if carpet[j][i] == name[ind]:
                if ind == 3:
                    flag = True
                    break 
                ind += 1
                break



    if flag:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    for i in range(int(input())):
        solve()