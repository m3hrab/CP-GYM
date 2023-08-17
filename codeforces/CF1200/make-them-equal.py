def main():
    t = int(input())
    for _ in range(t):
        n,c = input().split()
        n = int(n)
        s = input().strip()

        ans = []
        ok = True
        for x in s:
            if x != c:
                ok = False
        
        if not ok:
            for i in range(1, n + 1):
                ok = True
                j = i
                while j <= n:
                    ok &= (s[j - 1] == c)
                    j += i

                if ok:
                    ans.append(i)
                    break

            if not ok:
                ans.extend([n, n - 1])
        
        print(len(ans))
        if len(ans)!=0:
            print(*ans)

if __name__ == "__main__":
    main()
