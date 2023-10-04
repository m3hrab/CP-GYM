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
        teams = read_int_list()
        temp = sorted(teams,reverse=True)
        
        mx = temp[0]
        mx2 = temp[1]

        ans = False
        if mx in teams[:2]:
            for i in teams[2:]:
                if i >= mx2:
                    ans = True
                    break 
        else:
            for i in teams[:2]:
                if i >= mx2:
                    ans = True 
                    break 
        
        print_yes_no(ans)


if __name__ == '__main__':
    solve()