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
    n, k = read_ints()
    a = read_int_list()

    a = list(enumerate(a))
    a = sorted(a, key=lambda x: x[1])

    
    values = [element for _, element in a]
    indexes = [index+1 for index, _ in a]

    for i in range(n,-1,-1):
        if sum(values[:i]) <= k:
            ans = indexes[:i]
            break

    
    if len(ans)==0:
        print("0")
    else:
        print(len(ans))
        print_array(ans)

if __name__ == '__main__':
    solve()