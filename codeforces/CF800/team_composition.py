def solve():
    a, b = map(int, input().split())
    s = (a + b)//4
    n = min(a,b)
    if s <= n:
        print(s)
    else:
        print(n)


if __name__ == "__main__":
    for i in range(int(input())):
        solve()