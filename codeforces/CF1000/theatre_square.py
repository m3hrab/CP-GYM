import sys

# Constants
INF = float('inf')
MOD = 1000000007

# Faster Input
def read_int():
    return int(sys.stdin.readline())

def read_n_int():
    return map(int, sys.stdin.readline().split())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))


# Faster Output
def print_yes_no(condition):
    print('YES' if condition else 'NO')
    
def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


# Main Function
def solve():
    n, m, k = read_n_int()

    # vartical axis
    if m%k==0:
        count = m//k
    else:
        count = m//k + 1 


    if n%k==0:
        count2 = n//k 
    else:
        count2 = n//k + 1

    print(count*count2)
if __name__ == '__main__':
    solve()
