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
    n = read_int()
    points = read_ints()

    min_points = points[0]
    max_points = points[0]
    ans = 0
    for i in range(1,n):
        if points[i] < min_points:
            ans += 1
            min_points = points[i]
        elif points[i] > max_points:
            ans += 1
            max_points = points[i]

    print(ans)

if __name__ == '__main__':
    solve()