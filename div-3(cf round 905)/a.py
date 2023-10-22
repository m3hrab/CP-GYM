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
    numbers = "1234567890"
    for _ in range(t):
        pin = input()
        n = len(pin)
        current = 1

        temp = numbers.index(pin[0])
        count = temp + 1

        for i in range(n - 1):
            temp = abs(numbers.index(pin[i]) - numbers.index(pin[i+1])) + 1
            count += temp 

        print(count)

if __name__ == '__main__':
    solve()