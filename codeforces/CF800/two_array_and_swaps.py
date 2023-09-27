# CP Template 0.2
# Author: Mehrab (@to0th_less)

import sys
from math import gcd, sqrt
from itertools import combinations, permutations

# Constants
INF = float('inf')
MOD = 1000000007

# Faster Input Shortcut
def read_int():
    return int(sys.stdin.readline().strip())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

# Faster Output Shortcut
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))

# Main Function
def solve():
    t = read_int()
    for _ in range(t):
        n, k = read_ints()
        a = sorted(read_int_list())
        b = sorted(read_int_list(),reverse=True)

        i = 0
        count = 0
        while i<n and k!=0:
            if b[i]>a[i]:
                a[i] = b[i]
                count += 1
                if count == k:
                    break
            i += 1

        print(sum(a))


if __name__ == '__main__':
    solve()