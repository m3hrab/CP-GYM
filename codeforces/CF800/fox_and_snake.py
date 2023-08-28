def solve():
    n, m = map(int, input().split())
    temp = m - 1
    flag = True

    for i in range(n):
        if i%2==0:
            n = "#" * m
        else:
            if flag:
                n = ("." * temp) + "#"
                flag = False    
            else:
                n = "#" + ("." * temp)
                flag = True

        print(n)           
                        

if __name__ == "__main__":
    solve()