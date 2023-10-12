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
        n, m = read_ints()
        x = input()
        s = input()

        if s in x:
            print("0")
            continue 

        temp = set(s)
        ans = -1
        flag = True 
        for i in temp:
            if i not in x:
                flag = False
                break

        if flag:
            count = 0
            for i in range(m):
                x += x
                count += 1 
                if s in x:
                    ans = count 
                    break 
        
        print(ans)
                




if __name__ == '__main__':
    solve()