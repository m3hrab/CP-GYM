def solve():
    n = int(input())
    bills = [100, 20, 10, 5, 1]
    ans = 0

    for i in range(5):
        m = n // bills[i]
        if m != 0:
            ans += m

        n = n % bills[i]

    print(ans)


if __name__ == "__main__":
    solve()
        

