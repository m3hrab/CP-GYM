def solve():
    n = int(input())
    l = list(map(int, input().split()))

    recurit = 0
    untreated = 0
    for i in l:
        if i>0:
            recurit += i
        else:
            if (recurit - 1)<0:
                untreated += 1
            else:
                recurit -= 1
            


    print(untreated)


if __name__ == "__main__":
    solve()

