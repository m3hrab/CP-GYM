import sys

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
        k = int(input())

        number = 1
        indx = 0
        while indx <= k:
            if number%3 != 0 and str(number)[-1] != '3':
                indx += 1
            if indx == k:
                break 
            number += 1

        print(number)

if __name__ == '__main__':
    solve()