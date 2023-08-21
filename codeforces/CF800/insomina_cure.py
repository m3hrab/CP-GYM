def solve():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())

    if k==1 or l==1 or m==1 or n==1:
        print(d) 
    else:
        count = 0
        for i in range(1, d+1):
            if i%k != 0 and i%l != 0 and i%m != 0 and i%n !=0:
                count += 1

        print(abs(d - count))


if __name__ == "__main__":
    solve()