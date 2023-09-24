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
        
        athelets = []
        for i in range(n):
            athelets.append(read_int_list())
        

        new = []
        new.append(athelets[0])

        for i in range(1,n):
            if athelets[i][0] >= new[0][0]:
                new.append(athelets[i])
        
        if len(new) > 1:
            flag = False
            for i in range(1,len(new)):
                if new[i][1] >= new[0][1]:
                    flag = True 
                    break 
            
            if flag:
                print("-1")
            else:
                print(new[0][0])

        else:
            print(new[0][0])




if __name__ == '__main__':
    solve()