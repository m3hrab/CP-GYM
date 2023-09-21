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

def is_triangle(x, y, z):
    if x+y > z and x+z > y and y+z > x:
        return True
    return False

# Main Function
def solve():
    # Sample input format for multiple test cases
    t = read_int()
    for _ in range(t):
        a, b, c, d = read_ints()

        while True:
            x = a 
            z = c 
            y = c - a + 1

        print("%d %d %d"%(x,y,z))
if __name__ == '__main__':
    solve()