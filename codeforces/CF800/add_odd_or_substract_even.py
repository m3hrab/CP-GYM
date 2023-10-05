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
        a, b = read_ints()

        if a==b:
            print("0")
        else:
            if (a%2==0 and b%2==0) or (a%2==1 and b%2==1):
                print("1")
            else:
                if abs(a-b) == 1:
                    print("1")
                else:
                    print("2")
                    


if __name__ == '__main__':
    solve()