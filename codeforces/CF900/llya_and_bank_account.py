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
    if n < 0:
        n = abs(n)
        l1 = n%10
        l2 = ((n-l1)//10)%10
        if l2>l1:
            n = (((n-l1)//10) - l2) + l1
        else:
            n = (n-l1)//10

        n = - n
    print(n)




if __name__ == '__main__':
    solve()