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

#1426A
#1371A
for i in range(int(input())):
    n, x = map(int, input().split())
    
    if n <= 2:
        print(1)
    else:
        result = (n - 3) // x + 2
        print(result)
