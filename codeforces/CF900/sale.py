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
    n, m = map(int, sys.stdin.readline().split())
    a = read_ints()

    temp = []
    for i in range(n):
        if a[i] < 0:
            temp.append(-a[i])

    temp.sort(reverse=True)
    print(sum(temp[:m]))
        
if __name__ == '__main__':
    solve()