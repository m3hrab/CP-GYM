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
    n = read_int()
    a = read_ints()
    m = max(a)
    count = 0
    for i in range(n):
        count += (m - a[i])

    print(count)
if __name__ == '__main__':
    solve()