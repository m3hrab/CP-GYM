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
    s = list(input())

    ptr1 = 1
    ptr2 = 0
    for i in range(len(s)):
        
        if ptr2 == 0:
            ptr1 += 1
            ptr2 = ptr1 - 1 
        
        else:
            s[i] = ''
            ptr2 -= 1
        
    new = ''
    for i in s:
        if i != '':
            new += i

    print(new)


if __name__ == '__main__':
    solve()