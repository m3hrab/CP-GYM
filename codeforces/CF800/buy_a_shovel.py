import sys

INF = float('inf')

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def print_yes_no(condition):
    print('YES' if condition else 'NO')

def solve():
    k, r = map(int, input().split())
    count = 0
    i = 1
    temp = k*i
    while True:
        if temp%10==0 or (temp-r)%10==0:
            if count == 0:
                count = 1
            break 
        temp = k*i 
        i += 1
        count += 1


    print(count)
if __name__ == '__main__':
    solve()