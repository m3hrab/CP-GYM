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
        arr = read_int_list()

        evens = []
        ev_ind = []
        odds = []
        odd_ind = []

        if arr[0] % 2 == 0:
            is_even = True 
        else:
            is_even = False

        for i in range(n):
            if arr[i]%2==0:
                evens.append(arr[i])
                ev_ind.append(i)
            else:
                odds.append(arr[i])
                odd_ind.append(i)

        evens.sort()
        ev_ind.sort()
        odds.sort()
        odd_ind.sort()

        ans = [0 for i in range(n)]

        for i in range(len(evens)):
            ans[ev_ind[i]] = evens[i]
            
        for i in range(len(odds)):
            ans[odd_ind[i]] = odds[i]

        flag = True
        for i in range(n-1):
            if ans[i] > ans[i+1]:
                flag = False
                break
        
        print_yes_no(flag)



            


if __name__ == '__main__':
    solve()