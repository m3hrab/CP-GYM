import sys
import math
from itertools import combinations_with_replacement
INF = float('inf')

# input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

# output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def solve():
    for i in range(int(input())):
        n = read_ints()
        s = sum(n)
        pairs = combinations_with_replacement(list(_ for _ in range(1,s+1)),2)
        flag = False
        for pair in list(pairs):
            a = pair[0]
            b = pair[1]
            if sum(pair) >= n[0] and sum(pair) <= n[1]:
                if math.gcd(a,b) != 1:
                    flag = True 
                    temp = [a,b]
                    break

        if flag:
            print(*temp)
        else:
            print("-1")
if __name__ == '__main__':
    solve()