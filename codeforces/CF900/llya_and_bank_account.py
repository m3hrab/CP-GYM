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
        n = list(str(n))
        if len(n)>1:
            l1 = int(n[-1])
            l2 = int(n[-2])
            if l2 > l1:
                n.pop(-2)
            else:
                n.pop(-1)
        else:
            n.pop()

        ans = ''
        for i in n:
            ans += i 
        
        n = int(ans)

    print(n)




if __name__ == '__main__':
    solve()