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
    a = read_int()
    b = read_int()
    c = read_int()

    if a == 0:
        ans = 0
    else:
        ans = 0 
        for i in range(a):
            if b > 1:
                b -= 2
                if c > 3:
                    c -= 4
                    ans += 7 
                else:
                    break 
            else:
                break 

        print(ans)



if __name__ == '__main__':
    solve()