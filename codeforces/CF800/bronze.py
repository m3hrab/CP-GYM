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
    l = read_str()

    if "--" in l:
        l = l.replace("--","2")
    if "-." in l:
        l = l.replace("-.","1")
    if "." in l:
        l = l.replace(".","0")
    
    print(l)

if __name__ == '__main__':
    solve()