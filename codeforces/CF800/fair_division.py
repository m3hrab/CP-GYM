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
        a = read_int_list()
        new = []
        ans = False 

        if sum(a)%2==0:
            half = sum(a)//2
            if half % 2 == 0:
                temp = half//2 
                for i in range(temp):
                    if 2 in a:
                        a.remove(2)
                    else:
                        a.remove(1)
                        a.remove(1)
                
                if sum(a) == half:
                    ans = True 
            else:
                if a.count(1) != 0:
                    ans = True             

        print_yes_no(ans)



if __name__ == '__main__':
    solve()