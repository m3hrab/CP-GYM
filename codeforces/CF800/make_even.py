def solve():
    n = input()
    if int(n)%2==0:
        print(0)
    else:
        flag = 0
        if int(n[0])%2==0:
            print("1")
        else:
            for i in range(1,len(n)):
                if int(n[i])%2==0:
                    flag = 1
                    break 

            if flag:
                print("2")
            else:
                print("-1")

if __name__ == "__main__":
    for i in range(int(input())):
        solve()