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

def print_array(arr, sep=''):
    print(sep.join(map(str, arr)))

# Main Function
def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        matrix = []
        for i in range(n):
            s = list(input())
            matrix.append(s)
        
        # Rotate 90 degree 
        r_matrix = [] 
        for i in range(n):
            temp = []
            for j in range(n-1,-1,-1):
                temp.append(matrix[j][i])
            
            r_matrix.append(temp)

        for i in r_matrix:
            print_array(i)

if __name__ == '__main__':
    solve()