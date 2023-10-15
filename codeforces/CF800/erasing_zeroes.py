# # CP Template 0.2
# # Author: Mehrab (@to0th_less)

# import sys
# from math import gcd, sqrt
# from itertools import combinations, permutations

# # Constants
# INF = float('inf')
# MOD = 1000000007

# # Faster Input Shortcut
# def read_int():
#     return int(sys.stdin.readline().strip())

# def read_ints():
#     return map(int, sys.stdin.readline().split())

# def read_int_list():
#     return list(map(int, sys.stdin.readline().split()))

# # Faster Output Shortcut
# def print_yes_no(condition):
#     print('YES' if condition else 'NO')

# def print_array(arr, sep=' '):
#     print(sep.join(map(str, arr)))

# # Main Function
# def solve():
#     t = read_int()
#     for _ in range(t):
#         s = input()
#         cnt = 0
#         start = False

#         n = s.count("1")
#         for i in s:
#             if i=='1':
#                 start = True
#                 n -= 1
#             else:
#                 if n <= 0:
#                     break 
#                 if start:
#                     cnt += 1 

#         print(cnt)

# if __name__ == '__main__':
#     solve()

# Solution 2  
for i in range(int(input())):
    print(input().strip('0').count('0'))