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
    arr = []
    for i in range(t):
        arr.append(read_int())

    new = []
    total = 0
    
    for i in arr:
        temp = i // 2
        new.append(temp)
        total += temp 
    
    total = abs(total)
    if total != 0:

        for i in range(len(arr)):
            if arr[i] % 2 != 0:   
                new[i] = arr[i]//2 + 1
                total -= 1 

            if total == 0:
                break 

    for i in new:
        print(i)
    
            


if __name__ == '__main__':
    solve()