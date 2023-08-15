# Reuseable Python Template for CP 
# created by Mehrab (codeforces-> @to0th_less )
import sys
import math
import bisect
import heapq
import string
import re
from decimal import Decimal
from collections import defaultdict, Counter, deque

# Fast input reading
def read_str():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def read_int_list_minus_one():
    return list(map(lambda x: int(x) - 1, input().split()))

# Fast output writing
def print_str(s):
    sys.stdout.write(s + '\n')
    sys.stdout.flush()

def print_int(n):
    sys.stdout.write(str(n) + '\n')
    sys.stdout.flush()

def print_int_list(arr):
    sys.stdout.write(' '.join(map(str, arr)) + '\n')
    sys.stdout.flush()

# Main function
def main():
    # Input reading
    n = read_int()
    arr = read_int_list()

    # Your code here

if __name__ == "__main__":
    main()
