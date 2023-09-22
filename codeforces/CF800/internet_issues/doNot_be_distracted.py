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
        
        current = None 
        tasks_started = []
        ans = True
        
        for i in range(n):
            if s[i] == current:
                continue
            else:
                if s[i] in tasks_started:
                    ans = False 
                else:
                    tasks_started.append(s[i])
                    current = s[i]

        print_yes_no(ans)


if __name__ == '__main__':
    solve()