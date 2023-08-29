import sys
from itertools import permutations
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
    uniform = []
    for i in range(n):
        temp = read_ints()
        uniform.append(temp)

    matches = permutations([_ for _ in range(n)],2)

    ans = 0
    for match in matches:
        if uniform[match[0]][0] == uniform[match[1]][1]:
            ans += 1

    print(ans)

    


if __name__ == '__main__':
    solve()