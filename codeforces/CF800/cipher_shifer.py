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
        n = read_int()
        s = input()

        p1 = 0
        p2 = 1 
        message = ''
        while p2 < n:
            if s[p1] == s[p2]:
                message += s[p1]
                if (p2 + 2) <= n-1:
                    p1 = p2+1
                    p2 += 2
                    continue
            
            p2 += 1

        print(message)
    



if __name__ == '__main__':
    solve()