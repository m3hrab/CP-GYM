import sys

INF = float('inf')

# input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

# output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def solve():
    n, k = map(int, input().split()) 
    count = 0
    ans = 0
    for i in range(1,n+1):
        count += 5*i
        if (k+count) <= 240:
            ans += 1

    print(ans)

    

if __name__ == '__main__':
    solve()