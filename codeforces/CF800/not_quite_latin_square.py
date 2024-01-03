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

def find_missing_letter(arr1, arr2):
    if 'A' in arr1 or 'A' in arr2:
        if 'B' in arr1 or 'B' in arr2:
            return 'C'
        else:
            return 'B'
    else:
        return 'A'
    
# Main Function
def solve():
    t = read_int()
    for _ in range(t):
        grid = []
        grid.append(list(input()))
        grid.append(list(input()))
        grid.append(list(input()))

        loc = list()

        # Find the ? location
        for i in range(3):
            for j in range(3):
                if grid[i][j] == '?':
                    loc.append(i)
                    loc.append(j)
                    break 

        
        # Generate arr1 
        arr1 = []
        for i in range(3):
            arr1.append(grid[loc[0]][i])
        
        # Generate arr2
        arr2 = []
        for j in range(3):
            arr2.append(grid[j][loc[1]])

        # print(arr1)
        # print(arr2)
        n = find_missing_letter(arr1, arr2)
        print(n)





if __name__ == '__main__':
    solve()