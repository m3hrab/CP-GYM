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
    table_card = input()
    hand_card = list(input().split())

    flag = False
    for i in range(len(hand_card)):
        if hand_card[i][0] == table_card[0]:
            flag = True 
            break 

        if hand_card[i][1] == table_card[1]:
            flag = True 
            break 
    
    print_yes_no(flag)



if __name__ == '__main__':
    solve()