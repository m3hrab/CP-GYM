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
    n = read_int()
    a = read_ints()

    min_unit = [[]]
    diff = INF

    for i in range(n-1):
        temp_diff = abs(a[i]-a[i+1])
        if temp_diff < diff:
            diff = temp_diff
            min_unit[0] = [i+1,i+2]

    # anticlock
    if abs(a[0] - a[-1]) < diff:
        min_unit[0] = [n, 1] 

    
    print_array(min_unit[0])

if __name__ == '__main__':
    solve()