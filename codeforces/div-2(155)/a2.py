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
        a = []
        for i in range(n):
            a.append(read_int_list())

        
        flag = True
        for i in range(1, n):
            if a[i][0] >= a[0][0] and a[i][1] >= a[0][1]:
                flag = False
                break 
        
        if flag:
            print(a[0][0])
        else:
            print("-1")



if __name__ == '__main__':
    solve()