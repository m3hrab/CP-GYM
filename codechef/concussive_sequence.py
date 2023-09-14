# Main Function
def solve():
    for i in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        
        if len(set(a)) == 1:
            print("-1")
        else:
            a.sort()
            if n%2==0:
                x = n//2 
            else:
                x = n//2 + 1
            a1 = a[:x]
            a2 = a[x:]
            cnt1 = len(a1)
            cnt2 = len(a2)
            tempa2 = a2[:]
            new = []
            flag = False
            for i in range(min(len(a1),len(a2))):
                if a1[i] == a2[i]:
                    flag = True 
                    break 
                else:
                    new.append(a1[i])
                    new.append(a2[i])
                    cnt1 -= 1
                    cnt2 -= 1

            if flag:
                print("-1") 
            else:
                if cnt1 > 0:
                    new.append(a1[-1])
                if cnt2 > 0:
                    new.append(a2[-1])

                print(*new)


if __name__ == '__main__':
    solve()
