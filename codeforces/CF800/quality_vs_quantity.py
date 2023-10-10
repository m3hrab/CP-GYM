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
        arr = sorted(read_int_list())


        sum1 = arr[0] + arr[1]
        sum2 = arr[n-1]
        p1 = 2
        p2 = n - 2

        ans = False
        while p1 < p2:
            if sum2 > sum1:
                ans = True 
                break 
            else:
                sum1 += arr[p1]
                sum2 += arr[p2]
                p1 += 1 
                p2 -= 1 

        

        
        print_yes_no(ans)




if __name__ == '__main__':
    solve()