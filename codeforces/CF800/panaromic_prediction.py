import sys

# Define constants
INF = float('inf')
MOD = 10**9 + 7

# Define input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    return sys.stdin.readline().strip()

def read_strs():
    return list(sys.stdin.readline().split())

# Define output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def is_prime(n):
    if n==2 or n==3:
        return True 
    for i in range(2,(n//2)+1):
        if n%i == 0:
            return False
    return True

def solve():
    n, m = map(int, input().split())
    i = n + 1
    flag = False
    while True:
        if is_prime(i):
            if i==m:
                flag = True 
            else:
                flag = False 
            break
        i += 1

    print_yes_no(flag)

            

if __name__ == '__main__':
    solve()