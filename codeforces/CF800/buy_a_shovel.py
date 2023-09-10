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
    k, r = map(int, input().split())
    x = 1

    while True:
        if (k*x)%10 == 0 or (k*x)%10==r:
            break
        x += 1


    print(x)
if __name__ == '__main__':
    solve()