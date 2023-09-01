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
    n = read_str()
    flag = False 
    
    zero_count = 0
    one_count = 0
    for i in range(len(n)):
        if int(n[i]) == 0 and zero_count < 7:
            zero_count += 1
            one_count = 0
        elif int(n[i]) == 1 and one_count < 7:
            one_count += 1
            zero_count = 0

        if max(zero_count,one_count) == 7:
            flag = True
            break 
    
    print_yes_no(flag)

if __name__ == '__main__':
    solve()