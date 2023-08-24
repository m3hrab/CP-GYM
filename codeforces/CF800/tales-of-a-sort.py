def solve():
    n = int(input())
    a = list(map(int, input().split()))
    sorted_a = a[:]
    sorted_a.sort()
    flag = n
    for i in range(n-1,-1,-1):
        if(a[i]==sorted_a[i]):
            flag -= 1
        else:
            break 

    if flag == 0:
        print(0)
    else:
        print(max(a[:flag]))


if __name__ == "__main__":
    for i in range(int(input())):
        solve()