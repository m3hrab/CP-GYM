import sys

# Define constants
INF = float('inf')
MOD = 10**9 + 7

# Define input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    return sys.stdin.readline().strip()

def read_strs():
    return list(sys.stdin.readline().split())

# Define output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def solve():
    m, n = map(int, sys.stdin.readline().split())
    a = read_ints()

    temp = []
    max = 0
    indx = 0
    for i in range(m):
        x = a[i]//n
        if a[i]%n != 0:
            x += 1
        if x >= max:
            max = x
            indx = i+1
        temp.append(x)

    print(indx)


if __name__ == '__main__':
    solve()