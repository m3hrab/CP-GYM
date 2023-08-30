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


def solve():
    num = read_ints()
    n = num[0]
    k = num[1]

    if n%2==1:    
        temp = (n//2) + 1
    else:
        temp = n//2
    
    if temp >= k:
        print((2*(k-1))+1)
    else:
        k = abs(temp-k) 
        print(2*k)    


if __name__ == '__main__':
    solve()