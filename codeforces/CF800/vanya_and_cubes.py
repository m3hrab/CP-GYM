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

def nsum(n):
    return (n*(n+1))//2
# Main Function
def solve():
    n = read_int()
    a = []
    for i in range(1,n+2):
        a.append(nsum(i))
        if sum(a)==n:
            ans = i
            break 
        elif sum(a)>n:
            if sum(a) + nsum(i+1) >= n:
                ans = i + 1
            else:
                ans = i
            break 
    if n==1:
        print("1")
    elif n==2:
        print('3')
    else:
        print(ans)
    


if __name__ == '__main__':
    solve()