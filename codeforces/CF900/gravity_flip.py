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
    a = read_int_list()

    column = n
    row = max(a)

    box = []
    for i in range(column):
        temp = []
        for j in range(row):
            temp.append(0)
        
        box.append(temp)

    for i in range(column):
        for j in range(a[i]):
            box[i][j] = 1

    for b in box:
        print_array(b)
    
    print(box)


if __name__ == '__main__':
    solve()