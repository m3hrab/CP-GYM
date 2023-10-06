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
        string = input()
        new = []
        count = 1
        previous = string[0]
        n = len(string)

        for i in range(1, n):
            if string[i] != previous:
                if count % 2 == 1:
                    if previous not in new:
                        new.append(previous)
                
                previous = string[i]
                count = 0
            
            count += 1

            if i == n-1:
                if count % 2 == 1:
                    if previous not in new:
                        new.append(previous)
        
        if len(string) == 1:
            new.append(string[0])

        print_array(sorted(new))




if __name__ == '__main__':
    solve()