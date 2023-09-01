def solve():
    n, m = map(int, input().split())

    ans = ""

    if n > m:
        for i in range(m):
            ans += "BG"
        for i in range(m,n):
            ans += "B"
    elif n < m:
        for i in range(n):
            ans += "GB"
        for i in range(n,m):
            ans += "G"
    else:
        for i in range(n):
            ans += "GB"

    print(ans)    

if __name__ == '__main__':
    solve()