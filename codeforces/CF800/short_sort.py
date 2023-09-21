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
    # Sample input format for multiple test cases
    t = read_int()
    for _ in range(t):
        n = input()
        if n=='abc':
            print("YES")
            continue 
        else:
            new = n[1] + n[0] + n[2]
            new2 = n[2] + n[1] + n[0]
            new3 = n[0] + n[2] + n[1]

            if new == "abc" or new2 == 'abc' or new3 == 'abc':
                print("YES")
                continue
            else:
                print("NO")


if __name__ == '__main__':
    solve()