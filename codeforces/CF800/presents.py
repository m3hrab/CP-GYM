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

def print_int_list(arr):
    sys.stdout.write(' '.join(map(str, arr)) + '\n')
    sys.stdout.flush()

# Main function
def main():
    # Input reading
    n = read_int()
    arr = read_int_list()
    result = []
    for i in range(1,n+1):
        result.append(arr.index(i)+1)

    print_int_list(result)

if __name__ == "__main__":
    main()
