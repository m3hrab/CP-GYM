def solve():
    a = input()
    b = input() 
    new = ''

    for i in range(len(a)):
        if a[i] != b[i]:
            new += '1'
        else:
            new += '0'
    print(new)

if __name__ == "__main__":
    solve()