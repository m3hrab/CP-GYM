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
    n = read_int()
    a = read_int_list()
    count = 0
    subsegment = []
    for i in range(n-1):
        if a[i] >= a[i+1]:
            count += 1
        else:
            subsegment.append(count)
            count = 0

    if n == 1:
        subsegment.append(1)
    print(max(subsegment))




if __name__ == '__main__':
    solve()