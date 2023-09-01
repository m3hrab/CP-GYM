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
    n = read_int()
    arr = read_ints()

    temp = list(set(arr))
    temp.sort()
    count = 0
    flag = False
    for i in range(len(temp)-1):
        if (temp[i+1] - temp[i]) == 1:
            count += 1
            if count == 2:
                flag = True
                break 
        else:
            count = 0
            flag = False

    print_yes_no(flag)
        
if __name__ == '__main__':
    solve()