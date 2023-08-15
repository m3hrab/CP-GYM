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

def print_list(arr):
    sys.stdout.write(''.join(map(str, arr)) + '\n')
    sys.stdout.flush()

# Main function
def main():
    s = read_str()
    vowels = list("AOYEUIaoyeui")
    s1 = list()
    for i in range(len(s)):
        if s[i] not in vowels:
            s1.append(s[i].lower())

    for i in range(len(s1)*2-1):
        if i%2==0:
            s1.insert(i,'.')

    print_list(s1)
if __name__ == "__main__":
    main()
