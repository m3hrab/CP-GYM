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
    s = input()

    ans = iter(list("hello"))
    current = next(ans)
    nxt = None
    flag = False

# ahhelllloou

    for i in s:
        if nxt != None:
            if i == current:
                if i == nxt and i=='l':
                    current = nxt
                    nxt = next(ans)
                else:
                    continue 
            elif i == nxt:
                current = nxt
                if current == 'o':
                    flag = True 
                    break
                else:
                    nxt = next(ans)

        else:
            if i == current:
                nxt = next(ans)
        
        
    print_yes_no(flag)

if __name__ == '__main__':
    solve()

