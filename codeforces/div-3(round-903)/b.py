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
        arr = read_int_list()
        mn = min(arr)
        mx = max(arr)


        ans = False 
        if len(set(arr)) == 1:
            ans = True 

        else:
            for i in range(3):

                if (mx - mn) < mn or (mx-mn) <= 0:
                    break 
                else:
                    arr.append(mn)
                    arr.append(mx-mn)
                    arr.remove(mx)
                    mx = max(arr)

                if len(set(arr)) == 1:
                    ans = True 
                    break 
            
        if len(set(arr)) != 1:
            ans = False 
            
        print_yes_no(ans)


if __name__ == '__main__':
    solve()