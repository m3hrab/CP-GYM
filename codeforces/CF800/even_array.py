def solve():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        if n % 2:
            print((n // 2) + 1)
        else:
            print(n // 2)

if __name__ == "__main__":
    solve()
